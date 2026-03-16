from flask import Flask, render_template, jsonify
from simulator import generate_vehicle_data
from ids_model import detect_intrusion
from encryption import encrypt_data, decrypt_data
from blockchain import blockchain

import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "intrusion_log.csv"


# create log file if it does not exist
if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=[
        "time",
        "speed",
        "engine_temp",
        "rpm",
        "intrusion"
    ])
    df.to_csv(LOG_FILE, index=False)


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/data")
def data():

    # generate vehicle telemetry
    vehicle_data = generate_vehicle_data()

    print("RAW DATA:", vehicle_data)

    # encryption
    encrypted = encrypt_data(vehicle_data)
    print("ENCRYPTED DATA:", encrypted)

    # decryption
    decrypted = eval(decrypt_data(encrypted))
    print("DECRYPTED DATA:", decrypted)

    # IDS detection
    intrusion = detect_intrusion(decrypted)
    decrypted["intrusion"] = intrusion

    print("INTRUSION:", intrusion)

    log_row = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "speed": decrypted["speed"],
        "engine_temp": decrypted["engine_temp"],
        "rpm": decrypted["rpm"],
        "intrusion": intrusion
    }

    # append log to CSV
    df = pd.DataFrame([log_row])
    df.to_csv(LOG_FILE, mode="a", header=False, index=False)

    # add intrusion event to blockchain
    if intrusion:
        blockchain.add_block(log_row)
        print("BLOCK ADDED TO BLOCKCHAIN")

    return jsonify(decrypted)


@app.route("/logs")
def logs():
    df = pd.read_csv(LOG_FILE)
    return df.tail(10).to_json(orient="records")


@app.route("/chain")
def chain():

    chain_data = []

    for block in blockchain.chain:
        chain_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "hash": block.hash
        })

    return jsonify(chain_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)