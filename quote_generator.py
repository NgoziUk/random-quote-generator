import random

print("Quote Generator Started")

quotes = ["Stay positive", "Keep going", "You got this"]


def get_quote():
    return random.choice(quotes)

print(get_quote())
