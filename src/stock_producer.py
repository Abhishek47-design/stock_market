import requests
import json
import time
import os 

from datetime import datetime, UTC

from config import API_KEY
from config import STOCK_SYMBOLS
from kafka_utils import send_to_kafka


def get_stock_data(symbol):

    url = (
        f"https://finnhub.io/api/v1/quote"
        f"?symbol={symbol}"
        f"&token={API_KEY}"
    )

    response = requests.get(url)

    return response.json()


def save_data(record):

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    filename = (
        f"data/raw/"
        f"{record['symbol']}_"
        f"{datetime.now(UTC).strftime('%Y%m%d_%H%M%S_%f')}.json"
    )

    with open(filename, "w") as file:
        json.dump(record, file)


def main():

    while True:

        for symbol in STOCK_SYMBOLS:

            try:

                stock = get_stock_data(symbol)

                record = {
                    "symbol": symbol,
                    "current_price": stock["c"],
                    "high_price": stock["h"],
                    "low_price": stock["l"],
                    "open_price": stock["o"],
                    "previous_close": stock["pc"],
                    "timestamp": datetime.now(UTC).isoformat()
                }

                print(record)

                send_to_kafka(record)

                save_data(record)

            except Exception as e:

                print(
                    f"Error for {symbol}: {e}"
                )

        time.sleep(10)


if __name__ == "__main__":
    main()