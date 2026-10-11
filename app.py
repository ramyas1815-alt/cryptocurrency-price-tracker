
from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false"
}

cached_data = []


def get_crypto_data():
    global cached_data

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        cached_data = response.json()

        print("Live crypto data updated!")
        print("Records:", len(cached_data))

    except Exception as error:
        print("API Error:", error)


@app.route("/")
def home():

    # Get live data
    get_crypto_data()

    # Current time
    current_time = datetime.now().strftime("%H:%M:%S")

    return render_template(
        "live_crypto.html",
        crypto_data=cached_data,
        current_time=current_time
    )


if __name__ == "__main__":

    print("Cryptocurrency Price Tracker started!")
    print("Open: http://127.0.0.1:5000")

    app.run(debug=True)
