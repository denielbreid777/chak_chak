from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", joke=requests.get("https://api.chucknorris.io/jokes/random"))






app.run(debug=True)
