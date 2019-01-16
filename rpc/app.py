from flask import Flask, request, Response
from jsonrpcserver import dispatch

from methods import *

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    """
    Main endpoint to accept calls
    """
    req = request.get_data().decode()
    response = dispatch(req)

    return Response(str(response), response.http_status)


if __name__ == "__main__":
    app.run()
