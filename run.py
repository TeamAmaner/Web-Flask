from flask import Flask, redirect, url_for, render_template, request

import os
import yaml
import asyncio

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
    s_list = db.get_guilds()
    return render_template(
    "/pages/servers.html",
    title="Servers",
    server_list=s_list,
    count=len(s_list)
    )

@app.route("/Registration/")
def Reg():
    return render_template(
    "/pages/registration.html",
    title="Registration",
    )

@app.route("/Check/", methods=['POST'])
def Check():
    des = request.form["Server Description"]
    url = request.form['Server Invitation']
    name = request.form['Server Name']
    ret = db.create_guild(des, url, name)
    return render_template(
    "/pages/check.html",
    title="Check",
    server=ret,
    )


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
