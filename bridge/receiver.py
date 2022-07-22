import flask
from flask import request
import sqlite3


app = flask.Flask(__name__)


db = sqlite3.connect(
    "../sensors_data_cloud.db", isolation_level=None, check_same_thread=False
)


@app.after_request
def cors(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/", methods=["POST"])
def receive():
    data = request.json

    c = db.cursor()
    for i in data["sensors"]:
        c.execute(
            "INSERT INTO sensors_history VALUES (?, ?, ?, ?)",
            (data["vessel_id"], i["id"], i["value"], data["date"]),
        )

    return "", 201


app.run(host="0.0.0.0", port=4000)
