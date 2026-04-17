
import requests
import pandas as pd
import time
import os
from datetime import datetime

INPUT_PATH = "/content/crypto-streaming-pipeline/data/input_data"

os.makedirs(INPUT_PATH, exist_ok=True)

for i in range(5):

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    data = requests.get(url).json()

    rows = []

    for coin in data:

        # SAFE CHECK
        if isinstance(data[coin], dict) and "usd" in data[coin]:

            rows.append({
                "timestamp": str(datetime.now()),
                "asset": coin,
                "price": data[coin]["usd"]
            })

    df = pd.DataFrame(rows)

    file_name = f"{INPUT_PATH}/crypto_{int(time.time())}.csv"
    df.to_csv(file_name, index=False)

    print("Created:", file_name)

    time.sleep(5)
