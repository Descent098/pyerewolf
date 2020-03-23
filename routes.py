"""The primary entrypoint for werewolf; what you run to play the game

This file handles the Flask side of things, which is the routing and
template rendering.
"""

from flask import Flask, render_template
app = Flask(__name__, static_folder='pyerewolf/static/', template_folder="pyerewolf/templates")

@app.route('/')
@app.route("/home")
@app.route("/index")
def homepage():
    return render_template("index.html")

@app.route('/join/<token>')
def join(token):
    return token

@app.route('/join/user/<username>')
def join_user(username):
    return username

if __name__ == '__main__':
    app.run()