from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Success", service="service_1")
