from flask import Flask, redirect, url_for, render_template
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized

import os
import yaml

# with open('input.yaml') as file:
#     obj = yaml.safe_load(file)

app = Flask(__name__)

discord = DiscordOAuth2Session(app)



# @app.route("/login/")
# def login():
#     return discord.create_session()
#
# @app.route("/logout/")
# def logout():
#     discord.revoke()
#     return redirect(url_for("index"))
#
# @app.route("/callback/")
# def callback():
#     discord.callback()
#     return redirect(url_for("user"))
#
#
# @app.errorhandler(Unauthorized)
# def redirect_unauthorized(e):
#     return redirect(url_for("login"))
#
#
# @app.route("/user/")
# @requires_authorization
# def user():
#     user = discord.fetch_user()
#     return render_template(
#     'pages/user.html',
#     auth=True
#     )



@app.route('/')
def index():
    return render_template(
        '/pages/index.html',
        title="Amaner",
        )

# <page_name>でアドレスに変数を用いて一般化している
# @app.route('/pages/<page_name>.html', methods=['GET'])
# def hello_function(page_name):
#     return render_template(
#         '/pages/%s.html' %page_name,
#         title=title,
#         name0=page_name,
#         )

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
    )

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
