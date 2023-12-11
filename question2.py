#2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/redirect-external", methods=["GET"])
def redirect_external():
    return redirect("https://sentry.io/", code=302)


@app.route("/redirect-internal", methods=["GET"])
def redirect_internal():
    return redirect("/landing", code=302)


@app.route("/landing", methods=["GET"])
def landing():
    return "Internal redirect."


@app.route("/", methods=["GET"])
def index():
    return '<a href="/redirect-internal">Internal redirect</a>' \
           '<br>' \
           '<a href="/redirect-external">External redirect</a>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
