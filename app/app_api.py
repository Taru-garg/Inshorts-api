"""
A lot to be done here.
1. Template for the start
2. Start page
3. Electron for making it an app
"""

from flask import Flask
import api

app = Flask(__name__)
app.secret_key = "vjfubvnwiojbtg[[;[;wfhweufiwubke"


@app.route("/home")
@app.route("/")
def index():
    return "Welcome to News and Weather app"


@app.route("/news")
def news_home():
    return api.fetch_all()


@app.route("/news/<category>")
def news(category):
    return api.fetch_category(category)


if __name__ == "__main__":
    app.run()