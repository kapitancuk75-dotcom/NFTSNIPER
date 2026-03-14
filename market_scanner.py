import requests
from config import TONAPI_KEY

API_URL = "https://tonapi.io/v2/nfts/items"


def get_new_nfts():

    headers = {
        "Authorization": f"Bearer {TONAPI_KEY}"
    }

    params = {
        "limit": 50
    }

    try:

        r = requests.get(API_URL, headers=headers, params=params)

        if r.status_code != 200:
            print("TONAPI error:", r.status_code)
            return []

        data = r.json()

        return data.get("nft_items", [])

    except Exception as e:

        print("API error:", e)
        return []
