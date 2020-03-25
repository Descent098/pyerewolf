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
from enum import Enum, unique
from copy import deepcopy
from random import choice, shuffle
from secrets import token_urlsafe as token_generator

class Player:
    def __init__(self, name:str):
        self.living = True
        self.role = False
        pass

class Game:
    def __init__(self):
        self.token = token_generator(128)
        self.players = ()


    def set_roles(self) -> tuple:
        """Goes through each player and sets there role
        based on the rules for what roles are available.
        
        Returns
        -------
        tuple
            Players with their roles assigned
        """

        remaining_players = deepcopy(self.players)
        shuffle(remaining_players) # Put players in random order

        seer = False # Changed to True once seer role has been assigned
        doctor = False # Changed to True once doctor role has been assigned
        drunk = False # Changed to True once drunk role has been assigned
        witch = False # Changed to True once witch role has been assigned
        alpha = False # Changed to True once alpha role has been assigned

        for counter, player in enumerate(remaining_players): 
            if counter <= len(self.players)//2: # Make half the players werewolfs
                if not alpha: # No alpha assigned yet
                    player.Role(6)
                    alpha = True

                else: # Assign player werewolf role
                    player.role = Role(0)

            # Primary villager roles

            elif not doctor:  # No doctor assigned yet
                player.role = Role(3)
                doctor = True

            elif not seer:  # No seer assigned yet
                player.role = Role(2)
                seer = True

            else: # Villagers and secondary roles
                selection = choice([1, 4, 5]) # Which role to choose of options left

                if selection == 4 and not drunk: # Drunk is chosen and it hasn't been assigned yet
                    player.role = Role(4)
                    drunk = True
                
                elif selection == 5 and not witch: # Witch is chosen and it hasn't been assigned yet
                    player.role = Role(5)
                    witch = True
                
                else:
                    player.role = Role(1)

        return remaining_players

    def day(self):
        pass

    def night(self):
        pass

    def to_lynch(self, player:Player, votes:int):
        pass

@unique # Forces all enumerator values to be unique
class Role(Enum):
    """Signifies the role of the player
    
    """
    werewolf = 0
    villager = 1
    seer = 2
    doctor = 3
    drunk = 4
    witch = 5
    alpha = 6

    def description(self) -> str:
        """Uses the current instance value to return the correct
        role description
        
        Returns
        -------
        str
            The description of what the role is

        Notes
        -----
        * Descriptions from: https://www.playwerewolf.co/rules/roles

        Examples
        --------
        Create a werewolf and drunk instance and print their descriptions
        ```
        >> werewolf = Role(0)
        
        >> print(werewolf.description()) # prints: The goal of the werewolves is to decide together on one villager...

        >> drunk = Role(4)

        >> print(drunk.description()) # prints: This role, while first and foremost taking on all the elements of a regular ...
        ```
        """
        descriptions = ["The goal of the werewolves is to decide together on one villager to secretly kill off during the night, while posing as villagers during the day so they're not killed off themselves. One by one they'll kill off villagers and win when there are either the same number of villagers and werewolves left, or all the villagers have died. This role is the hardest of all to maintain, because these players are lying for the duration of the game.",
            "The most commonplace role, a simple Villager, spends the game trying to root out who they believe the werewolves (and other villagers) are. While they do not need to lie, the role requires players to keenly sense and point out the flaws or mistakes of their fellow players. Someone is speaking too much? Could mean they're a werewolf. Someone isn't speaking enough? Could mean the same thing. It all depends on the people you're playing with, and how well you know them.",
            "The Seer, while first and foremost a villager, has the added ability to 'see' who the werewolves are once night falls. When called awake by the Moderator, the Seer can point to any of their fellow players and the Moderator must nod yes or no as to whether or not they are indeed a Werewolf. The Seer can then choose to keep this information a secret during the day, or reveal themselves as the Seer and use the knowledge they gained during the night in their defense or to their advantage during the day. The strategy here is up to you.",
            "Also a villager, the Doctor has the ability to heal themselves or another villager when called awake by the Moderator during the night. Should they heal themselves, then will be safe from being killed by the werewolves, or should they want to prove themselves the Doctor or fear the death of a fellow villager, can opt to heal them instead. Again, the strategy here is up to you.",
            "This role, while first and foremost taking on all the elements of a regular Villager throughout the game, also has the additional burden of only being able to communicate with gestures or noises. They may not talk during the day at all, and if they do, automatically die during that night. It may be the strategy of others (Werewolves, for instance) to pretend to be the Drunk, as the role is so unique and easily recognized.",
            "This role, while first and foremost taking on all the elements of a regular Villager throughout the game, also has the additional powers of one potion and one poison, which they may use at any point throughout the game. When the Witch is added, the Moderator will wake them up separately during the night with, “The Witch comes awake…” and follows this with “The Witch brings someone back to life.” and “The Witch poisons someone.” The Witch will then point to the person they want to poison or bring back to life. While the Witch can only use their potion and poison once, each action must be said each night to retain anonymity as to what has been done. They can only use one per evening until both are gone, and have the ability to save them until a point in the game they deem fit.",
            "This role, while first and foremost taking on all the elements of a regular Werewolf throughout the game, also has the additional burden of saying the word “Werewolf” at least once during the day. This is a challenge, because everyone playing will need to actively avoid saying the word “Werewolf” in an attempt to root out the Alpha Werewolf, who must say it at least once. In order for the Moderator to know which of the Werewolfs is the Alpha, we recommend having that person raise their hand the first time the Werewolves come awake at night, and making a note. If the Alpha Werewolf fails to say “Werewolf” during the day, they automatically die the next night.",
        ]
        return descriptions[self.value]
