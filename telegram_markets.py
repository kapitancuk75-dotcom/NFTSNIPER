from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

API_ID = 123456
API_HASH = "YOUR_API_HASH"

markets = [
    "PortalsMarketBot",
    "TonnelRelayerBot"
]


async def scan_markets():

    client = TelegramClient("session", API_ID, API_HASH)

    await client.start()

    results = []

    for market in markets:

        try:

            history = await client(GetHistoryRequest(
                peer=market,
                limit=50,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            for msg in history.messages:

                text = msg.message

                if text:

                    results.append(text)

        except:

            pass

    return results
