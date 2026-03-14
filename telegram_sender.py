import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "disable_web_page_preview": False
    }

    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram error:", e)
