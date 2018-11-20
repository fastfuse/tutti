from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Success", service="service_1")



# import requests, os


# def download_static_data(url, dest=None):
#     """
#     Function to download static data zip
#     """
#     filename = url.split('/')[-1]

#     dest_path = os.path.join(dest, filename) if dest else filename

#     r = requests.get(url, stream=True)

#     with open(dest_path, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:
#                 f.write(chunk)

#     return dest_path
