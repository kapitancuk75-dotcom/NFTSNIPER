import requests
from config import TONAPI_KEY

BASE_URL = "https://tonapi.io/v2/nfts/items"


def get_new_nfts():

    headers = {
        "Authorization": f"Bearer {TONAPI_KEY}"
    }

    params = {
        "limit": 50,
        "offset": 0
    }

    try:

        r = requests.get(BASE_URL, headers=headers, params=params, timeout=10)

        # ---------- ERROR 401 ----------
        if r.status_code == 401:
            print("TONAPI error 401: неверный API ключ")
            return []

        # ---------- ERROR 404 ----------
        if r.status_code == 404:
            print("TONAPI error 404: endpoint не найден")
            return []

        # ---------- ERROR 400 ----------
        if r.status_code == 400:
            print("TONAPI error 400: неправильные параметры запроса")
            return []

        # ---------- OTHER ERRORS ----------
        if r.status_code != 200:
            print("TONAPI unknown error:", r.status_code)
            return []

        data = r.json()

        if "nft_items" not in data:
            return []

        return data["nft_items"]

    except requests.exceptions.Timeout:

        print("TONAPI timeout")

    except requests.exceptions.ConnectionError:

        print("TONAPI connection error")

    except Exception as e:

        print("TONAPI unexpected error:", e)

    return []
