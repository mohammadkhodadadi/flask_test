from flask import Flask
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def check_and_inject_to_header():
    return {"name":"mohammad"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
