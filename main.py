from flask import Flask, render_template, request, make_response
import requests
from random import randint


app = Flask(__name__)


total_get = 0
total_post = 0


@app.route("/", methods=["GET", "POST"])
def home():

    global total_get, total_post

    # GET/POST підщот
    if request.method == "GET":
        total_get += 1
    elif request.method == "POST":
        total_post += 1

    response = make_response(render_template("index.html", joke=requests.get("https://api.chucknorris.io/jokes/random"), get=total_get, post=total_post))
    
    if  request.cookies.get("id"):
        response.set_cookie("bal",  str(int(request.cookies.get("bal")) + 1))
        
    else:
        response.set_cookie("id", str(randint(1000, 2000)))
        response.set_cookie("bal", str(0))

    @app.route("/category/<cat>")
    def by_category(cat):
        return render_template("category.html", joke=f"https://api.chucknorris.io/jokes/random?category={cat}")



    return response


app.run(debug=True)
