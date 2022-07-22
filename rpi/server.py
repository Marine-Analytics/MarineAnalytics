# lsusb to check device name
# dmesg | grep "tty" to find port name

import flask
import serial
import time
import os
import time
import threading

arduino1 = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
arduino2 = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)

controllers = (arduino1, arduino2)

app = flask.Flask(__name__)

data = (0, 0, 0)


def send_request(index):
    global controllers
    c = controllers[index]

    if c.isOpen():
        while c.inWaiting() == 0:
            pass
        if c.inWaiting() > 0:
            answer = c.readline()
            c.flushInput()
            return str(answer, encoding="utf-8")
    else:
        raise "Controller is disconnected"


def poll_data():
    global data
    while True:
        data = tuple(
            list(map(int, send_request(0).split("|"))) + [int(send_request(1))]
        )
        time.sleep(1)


@app.after_request
def cors(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/sensors", methods=["GET"])
def get_stats():
    res = {
        "vessel_id": 1,
        "date": int(time.time()),
        "sensors": [
            {"id": 1, "value": data[0]},
            {"id": 2, "value": data[1]},
        ],
    }

    if data[2] != -1:
        res["sensors"].append({"id": 3, "value": data[2]})

    return flask.jsonify(res), 200


if __name__ == "__main__":
    time.sleep(3)

    threading.Thread(target=poll_data).start()

    try:
        app.run(host="0.0.0.0", port=3000)
    except KeyboardInterrupt:
        for c in controllers:
            c.close()
