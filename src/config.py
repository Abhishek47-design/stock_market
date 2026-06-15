import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("F_API_KEY")
STOCK_SYMBOLS = [
    "AAPL",
    "GOOGL",
    "MSFT",
    "AMZN",
    "TSLA",
    "FB",
    "NVDA",
]