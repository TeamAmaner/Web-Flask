from flask import Flask, redirect, url_for, render_template

import os
import yaml

from lib.database import Database

# with open('input.yaml') as file:
#     obj = yaml.safe_load(file)

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    return render_template(
        '/pages/index.html',
        title="Amaner",
        )

@app.route("/Vocaleague/")
def Vocaleague():
    return render_template(
    "/pages/vocaleague.html",
    title="Vocaleague",
    )

@app.route("/Servers/")
def Servers():
    return render_template(
    "/pages/servers.html",
    title="Servers",
    server_list=db.get_guilds(),
    )

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
