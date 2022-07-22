import flask
from flask import request, jsonify
import sqlite3
import time
import requests


app = flask.Flask(__name__)
app.config["JSON_AS_ASCII"] = False

db = sqlite3.connect(
    "../sensors_data_cloud.db", isolation_level=None, check_same_thread=False
)


@app.after_request
def cors(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/vessels")
def get_vessels():
    c = db.cursor()
    res = c.execute("SELECT * FROM vessels").fetchall()

    return jsonify([{"id": r[0], "name": r[1]} for r in res])


@app.route("/full_info")
def get_history():
    vessel_id = request.args.get("vessel_id")

    c = db.cursor()

    vessel = c.execute("SELECT * FROM vessels WHERE id = ?", (vessel_id)).fetchone()
    if not vessel:
        return "", 404

    sensors = c.execute(
        "SELECT * FROM sensors WHERE vessel_id = ?", (vessel_id)
    ).fetchall()

    data = {"sensors": []}
    
    def get_values(vid, sid):
        res = c.execute("SELECT value FROM sensors_history WHERE vessel_id = ? AND sensor_id = ? ORDER BY DATE DESC LIMIT 30", (vid, sid)).fetchall()
        return [i[0] for i in res]

    predict = None
    if vessel_id == '2':
        req_data = {
            'values_speed': get_values(2, 1),
            'values_frequency': get_values(2, 2),
            'values_vibration': [i * 10 for i in get_values(2, 3)],
            'values_left_bak': get_values(2, 4),
            'values_right_bak': get_values(2, 5)
        }
        res = requests.post('http://localhost:6000/vodnik_predict', json=req_data).json()
        predict = [res['speed_predict'], res['frequency_predict'] / 10, res['vibration_predict'], res['left_bak_predict'], res['right_bak_predict']]

    if vessel_id == '1':
        req_data = {
            'vibro': [round(i * 0.029296875) for i in get_values(1, 1)],
            'oxygen': [round(i * 0.0419921875) for i in get_values(1, 2)],
            'temperature': get_values(1, 3)
        }
        res = requests.post('http://localhost:6000/stend_predict', json=req_data).json()
        print(res)
        predict = [round(res['vibro_predict'] * 0.029296875), round(res['oxygen_predict'] * 0.0419921875), res['temperature_predict']]

    for i, s in enumerate(sensors):
        history = c.execute(
            "SELECT * FROM sensors_history WHERE vessel_id = ? AND sensor_id = ? ORDER BY DATE DESC LIMIT 100",
            (vessel_id, s[1]),
        ).fetchall()

        data["sensors"].append(
            {
                "name": s[2],
                "normal": {
                    "min": s[3],
                    "max": s[4],
                },
                "history": [{"date": h[3], "value": h[2]} for h in history],
                "predict": predict[i] if predict != None else None
            }
        )

    c.close()
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)
