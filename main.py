from flask import Flask
from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def hello():
    return {"msg":"Hello, World!"}


@app.route("/x/info")
def info():
    first_name = request.args.get("first_name")
    return first_name.upper()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
