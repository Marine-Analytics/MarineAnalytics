import requests
import time
import os

LOCAL_SERVER_URL = os.environ["LOCAL_SERVER_URL"]
EXTERNAL_SERVER_URL = os.environ["EXTERNAL_SERVER_URL"]

while True:
    try:
        data = requests.get(LOCAL_SERVER_URL + "/sensors").json()
        requests.post(EXTERNAL_SERVER_URL + "/", json=data)
    except:
        print("could not send data")

    time.sleep(2)
