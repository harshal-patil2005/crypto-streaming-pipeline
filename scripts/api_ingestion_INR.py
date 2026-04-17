import requests
import json

url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)
data = response.json()

rate = 83  # fallback

if "rates" in data and "INR" in data["rates"]:
    rate = data["rates"]["INR"]

print("Live USD → INR:", rate)

# SAVE TO FILE (IMPORTANT)
with open("/content/crypto-streaming-pipeline/data/inr_rate.json", "w") as f:
    json.dump({"inr_rate": rate}, f)
