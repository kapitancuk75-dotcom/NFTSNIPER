import random


def analyze_nft(name, price, floor):

    score = 0

    # недооценка
    if price < floor * 0.4:
        score += 5

    elif price < floor * 0.6:
        score += 3

    elif price < floor * 0.8:
        score += 1

    rare_words = [
        "Diamond",
        "Gold",
        "Legendary",
        "Epic",
        "Rare"
    ]

    for word in rare_words:

        if word.lower() in name.lower():
            score += 2

    score += random.randint(0,2)

    if score >= 7:
        return "STRONG BUY"

    if score >= 5:
        return "BUY"

    if score >= 3:
        return "WATCH"

    return "IGNORE"
