from flask import Flask, request, Response, jsonify
from jsonrpcserver import method, dispatch


app = Flask(__name__)

@method
def ping():
    return "pong"

@method
def add(a, b):
    return a + b

@app.route("/", methods=["POST"])
def index():
    req = request.get_data().decode()
    response = dispatch(req)

    return Response(str(response), response.http_status)

if __name__ == "__main__":
    app.run()
