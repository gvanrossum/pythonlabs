import logging

from flask import Flask, request

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    full_path = request.full_path.rstrip("?")
    referer = request.headers.get("Referer")
    if referer:
        logging.info("Request %s from %s", full_path, referer)
    else:
        logging.info("Request %s", full_path)
    return "Not found", 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
