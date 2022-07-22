from joblib import load
from flask import Flask
from multiprocessing import Process
import datetime
import time
import requests
import pandas as pd
import signal
import sys
import os
from api.utils import data_preprocessing


def create_app():
    app = Flask(__name__)

    from api import api

    app.register_blueprint(api)

    return app

def start_app():
    app = create_app()
    cfg = {"host": "0.0.0.0", "debug": True}
    app.run(**cfg)


def start_emulator():
    while True:
        df = pd.read_csv("./data/data_new.csv")
        df = df[df['state'] == 'movement'].drop_duplicates(subset=['data_time'])
        model = load('./models/mov_state_model.joblib')
        for index, row in df.iterrows():
            # предсказание вероятности
            '''
            data_to_predict = pd.DataFrame(row.to_dict(), index=[0]).drop('state_boat', axis=1)
            data_to_predict = data_preprocessing(data_to_predict)
            predict = model.predict_proba(data_to_predict)[: , 1]
            print(predict[0])
            '''
            # ^^^^^^^^^^^^^^^^^

            print('sending data...')
            data = {
                "vessel_id": 2,
                "date": int(time.mktime(datetime.datetime.strptime(row[0], "%d.%m.%Y %H:%M").timetuple())),
                "sensors": [
                    {"id": 1, "value": row[1]},
                    {"id": 2, "value": row[3]},
                    {"id": 3, "value": row[5]},
                    {"id": 4, "value": row[7]},
                    {"id": 5, "value": row[9]},
                ],
                "metrics": [
                    {"id": 1, "value": row[2]},
                    {"id": 2, "value": row[4]},
                    {"id": 3, "value": row[6]},
                    {"id": 4, "value": row[8]},
                    {"id": 5, "value": row[10]},
                    {"id": 6, "value": row[11]},
                ],
            }
            try:
                r = requests.post('http://87.244.7.150:4000/', json=data)
            except (requests.exceptions.ConnectionError) as e:
                print(e)
            time.sleep(2)


def signal_handler(sig, frame):
    print("Terminated")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    server_proc = Process(
        target=start_app,
    )
    server_proc.daemon = True
    server_proc.start()
    os.environ['SERVER_PID'] = str(server_proc.pid)


    #emulator_proc = Process(
    #    target=start_emulator,
    #    )
    #emulator_proc.daemon = True
    #emulator_proc.start()
    #os.environ['EMULATOR_PID'] = str(emulator_proc.pid)

    #print(server_proc.pid, emulator_proc.pid)

    while True:
        time.sleep(10)
    
