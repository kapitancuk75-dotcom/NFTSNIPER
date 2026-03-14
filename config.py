import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TONAPI_KEY = os.getenv("TONAPI_KEY")

MAX_PRICE = float(os.getenv("MAX_PRICE", "5"))
PROFIT_PERCENT = float(os.getenv("PROFIT_PERCENT", "50"))
