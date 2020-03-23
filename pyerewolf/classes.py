"""This file contains all the classes used in the game. Primary game logic
is defined in server.py

Classes
---------
Game:
    TODO

Player:
    TODO

Functions
---------
TODO

References
----------
* Werewolf Rules:  https://www.playwerewolf.co/rules

Examples
--------
TODO
"""
from secrets import token_urlsafe as token_generator

class Player:
    def __init__(self):
        self.living = True
        pass

class Game:
    def __init__(self, players:tuple):
        self.token = token_generator(128)
        self.players = players
        pass

    def day(self):
        pass

    def night(self):
        pass

    def to_lynch(self, player:Player, votes:int):
        pass