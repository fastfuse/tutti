from flask import Flask, jsonify
import os, requests


app = Flask(__name__)

SERVICE_1_URL = os.environ.get("SERVICE_1_URL")
SERVICE_2_URL = os.environ.get("SERVICE_2_URL")



@app.route("/")
def index():
    return jsonify(message="Success", service="app_3")


@app.route("/s1")
def service_1():
    r = requests.get(SERVICE_1_URL)

    return jsonify(r.json())


@app.route("/s2")
def service_2():
    r = requests.get(SERVICE_2_URL)

    return jsonify(r.json())
