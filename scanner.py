import asyncio

from market_scanner import get_new_nfts
from ai_engine import analyze_nft
from telegram_sender import send_message
from config import MAX_PRICE

seen = set()


async def scan():

    while True:

        nfts = get_new_nfts()

        for nft in nfts:

            address = nft.get("address")

            if not address:
                continue

            if address in seen:
                continue

            seen.add(address)

            metadata = nft.get("metadata", {})

            name = metadata.get("name", "Unknown NFT")

            sale = nft.get("sale")

            if not sale:
                continue

            price = sale.get("price", {}).get("value")

            if not price:
                continue

            price = float(price) / 1e9

            if price > MAX_PRICE:
                continue

            floor = price * 1.5

            decision = analyze_nft(name, price, floor)

            if decision in ["BUY","STRONG BUY"]:

                link = f"https://getgems.io/nft/{address}"

                message = f"""
🚨 NFT SNIPER AI SIGNAL

NFT:
{name}

Цена:
{price} TON

AI сигнал:
{decision}

Ссылка:
{link}
"""

                send_message(message)

        await asyncio.sleep(5)


async def main():

    print("NFT SNIPER AI 10.0 STARTED")

    send_message("🤖 NFT SNIPER AI 10.0 запущен")

    await scan()


asyncio.run(main())
