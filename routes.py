"""The primary entrypoint for werewolf; what you run to play the game

This file handles the Flask side of things, which is the routing and
template rendering.
"""

from flask import *
from secrets import token_urlsafe
from pyerewolf.classes import Game, Player
app = Flask(__name__, static_folder='pyerewolf/static/', template_folder="pyerewolf/templates")

game = False
app.secret_key = token_urlsafe(128)
@app.route('/')
@app.route("/home")
@app.route("/index")
def homepage():
    """The main homepage of the game"""
    global game
    if not game:
        return redirect("/create")
    else:
        return redirect(f'/join/{game.token}')

@app.route('/join', methods=['GET', 'POST'])
def join(token):
    """Allows players to join the game"""
    if request.method == 'POST':
        pass
    else:
        return render_template('join.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Instantiates global game instance"""
    global game
    if request.method == 'POST':
        session['username'] = request.form['username']
        p1 = Player(request.form['username'])
        game = Game(p1)
        return redirect(f"/lobby/{game.token}")  
    else:
        return render_template("create.html")



@app.route('/lobby/<token>')
def lobby(token):
    """Where players go to after being added to the game"""
    global game
    if game.token == token:
        return f"{token} <br><br>{[player.name for player in game.players]}"
    else:
        return "rip"

if __name__ == '__main__':
    app.run()