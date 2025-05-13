from flask import Flask, render_template, request, make_response
import requests
from random import randint


app = Flask(__name__)




@app.route("/")
def home():
    response = make_response(render_template("index.html", joke=requests.get("https://api.chucknorris.io/jokes/random")))
    
    if  request.cookies.get("id"):
        response.set_cookie("bal",  str(int(request.cookies.get("bal")) + 1), httponly=True)
        
    else:
        response.set_cookie("id", str(randint(1000, 2000)), httponly=True)
        response.set_cookie("bal", str(0), httponly=True)

    return response


app.run(debug=True)
