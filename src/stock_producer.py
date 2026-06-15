import requests
import json
import time

from datetime import datetime

from config import API_KEY
from config import STOCK_SYMBOLS


def get_stock_data(symbol):

    url = (
        f"https://finnhub.io/api/v1/quote"
        f"?symbol={symbol}"
        f"&token={API_KEY}"
    )

    response = requests.get(url)

    return response.json()


def save_data(record):

    with open(
        "data/raw/stocks.json",
        "a"
    ) as file:

        json.dump(record, file)

        file.write("\n")


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
                    "timestamp": datetime.utcnow().isoformat()
                }

                print(record)

                save_data(record)

            except Exception as e:

                print(
                    f"Error for {symbol}: {e}"
                )

        time.sleep(10)


if __name__ == "__main__":
    main()