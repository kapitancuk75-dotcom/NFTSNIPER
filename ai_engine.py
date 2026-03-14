import random


def analyze_nft(name, price, floor):

    score = 0

    # дешёвый NFT
    if price < floor * 0.5:
        score += 4

    elif price < floor * 0.7:
        score += 2

    # редкие слова
    rare = [
        "Diamond",
        "Gold",
        "Legendary",
        "Epic",
        "Rare"
    ]

    for r in rare:

        if r.lower() in name.lower():
            score += 2

    # случайный фактор рынка
    score += random.randint(0,2)

    if score >= 6:
        return "STRONG BUY"

    if score >= 4:
        return "BUY"

    if score >= 3:
        return "WATCH"

    return "IGNORE"
