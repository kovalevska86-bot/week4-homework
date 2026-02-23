import json
import os

FILENAME = "shopping.json"
PRICES_FILE = "prices.json"

def load_list():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)

def load_prices():
    if not os.path.exists(PRICES_FILE):
        return {} 
    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_prices(prices):
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=4, ensure_ascii=False)

def get_price(name):
    prices = load_prices()
    return prices.get(name)

def set_price(name, price):
    prices = load_prices()
    prices[name] = price
    save_prices(prices)