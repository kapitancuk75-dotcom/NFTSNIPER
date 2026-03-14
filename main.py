import asyncio

from tonapi_scanner import get_new_nfts
from floor_checker import get_floor_price
from ai_engine import analyze_nft
from telegram_sender import send_message

seen = set()


async def scan():

    while True:

        try:

            nfts = get_new_nfts()

            if not nfts:
                await asyncio.sleep(5)
                continue

            for nft in nfts:

                address = nft.get("address")

                if not address:
                    continue

                if address in seen:
                    continue

                seen.add(address)

                metadata = nft.get("metadata", {})

                name = metadata.get("name","Unknown NFT")

                sale = nft.get("sale")

                if not sale:
                    continue

                price = sale.get("price", {}).get("value")

                if not price:
                    continue

                price = float(price) / 1e9

                collection = nft.get("collection", {}).get("address")

                floor = get_floor_price(collection)

                decision = analyze_nft(name, price, floor)

                if decision in ["BUY","STRONG BUY"]:

                    link = f"https://getgems.io/nft/{address}"

                    message = f"""
🚨 NFT SNIPER AI SIGNAL

NFT:
{name}

Цена:
{price} TON

Floor:
{floor} TON

AI сигнал:
{decision}

Ссылка:
{link}
"""

                    send_message(message)

        except Exception as e:

            print("Scanner error:", e)

        await asyncio.sleep(5)


async def main():

    print("NFT SNIPER AI 12.0 STARTED")

    send_message("🤖 NFT SNIPER AI 12.0 запущен")

    await scan()


asyncio.run(main())
