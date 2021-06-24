import random
from model import puppyUrlList
from flask import Flask, render_template

app = Flask(__name__)
puppyList = puppyUrlList


@app.route("/")
def hello_world():
    global puppyList
    return render_template(
        "welcome.html",
        puppyurl1=puppyList[random.randint(0, len(puppyList)-1)],
        puppyurl2=puppyList[random.randint(0, len(puppyList)-1)]
    )
