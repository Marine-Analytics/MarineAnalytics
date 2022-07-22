import sqlite3
import time
import requests
import json
import os

db = sqlite3.connect("../sensors_data_local.db", isolation_level=None)
cur = db.cursor()

SERVER_URL = os.environ["SERVER_URL"]

cur.execute(
    """CREATE TABLE IF NOT EXISTS sensors_data
              (date INT, vibro INT, oxygen INT, temperature INT)"""
)

try:
    while True:
        raw = requests.get(SERVER_URL + "/sensors").text
        data = json.loads(raw)

        date, vibro, oxygen, temperature = (
            int(time.time()),
            data["vibro"],
            data["oxygen"],
            data["temperature"],
        )

        cur.execute(
            "INSERT INTO sensors_data VALUES (?, ?, ?, ?)",
            (date, vibro, oxygen, temperature),
        )

        time.sleep(3)
except KeyboardInterrupt:
    db.close()
