import requests
import csv
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

CSV_FILE = "crypto_prices.csv"


def get_crypto_data():
    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        print("CoinGecko API connected successfully!")
        print("Total records received:", len(data))

        return data

    except requests.exceptions.RequestException as error:
        print("API Error:", error)
        return []


def save_to_csv(data):

    if not data:
        print("No data available.")
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Rank",
            "Cryptocurrency",
            "Symbol",
            "Current Price (USD)",
            "24h Change (%)",
            "Market Cap (USD)",
            "24h Volume (USD)",
            "Last Updated"
        ])

        for rank, coin in enumerate(data, start=1):

            writer.writerow([
                rank,
                coin.get("name"),
                coin.get("symbol", "").upper(),
                coin.get("current_price"),
                coin.get("price_change_percentage_24h"),
                coin.get("market_cap"),
                coin.get("total_volume"),
                current_time
            ])

    print("--------------------------------")
    print("CSV file created successfully!")
    print("Saved as:", CSV_FILE)
    print("Records saved:", len(data))


def main():

    print("Cryptocurrency Price Tracker")
    print("--------------------------------")

    data = get_crypto_data()

    save_to_csv(data)


if __name__ == "__main__":
    main()
    