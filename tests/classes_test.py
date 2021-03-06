from pyerewolf.classes import *

def test_Role_description():
    werewolf = Role(0)
    villager = Role(1)
    seer = Role(2)
    doctor = Role(3)
    drunk = Role(4)
    witch = Role(5)
    alpha = Role(6)

    assert werewolf.description() == "The goal of the werewolves is to decide together on one villager to secretly kill off during the night, while posing as villagers during the day so they're not killed off themselves. One by one they'll kill off villagers and win when there are either the same number of villagers and werewolves left, or all the villagers have died. This role is the hardest of all to maintain, because these players are lying for the duration of the game."
    assert villager.description() == "The most commonplace role, a simple Villager, spends the game trying to root out who they believe the werewolves (and other villagers) are. While they do not need to lie, the role requires players to keenly sense and point out the flaws or mistakes of their fellow players. Someone is speaking too much? Could mean they're a werewolf. Someone isn't speaking enough? Could mean the same thing. It all depends on the people you're playing with, and how well you know them."
    assert seer.description() == "The Seer, while first and foremost a villager, has the added ability to 'see' who the werewolves are once night falls. When called awake by the Moderator, the Seer can point to any of their fellow players and the Moderator must nod yes or no as to whether or not they are indeed a Werewolf. The Seer can then choose to keep this information a secret during the day, or reveal themselves as the Seer and use the knowledge they gained during the night in their defense or to their advantage during the day. The strategy here is up to you."
    assert doctor.description() == "Also a villager, the Doctor has the ability to heal themselves or another villager when called awake by the Moderator during the night. Should they heal themselves, then will be safe from being killed by the werewolves, or should they want to prove themselves the Doctor or fear the death of a fellow villager, can opt to heal them instead. Again, the strategy here is up to you."
    assert drunk.description() == "This role, while first and foremost taking on all the elements of a regular Villager throughout the game, also has the additional burden of only being able to communicate with gestures or noises. They may not talk during the day at all, and if they do, automatically die during that night. It may be the strategy of others (Werewolves, for instance) to pretend to be the Drunk, as the role is so unique and easily recognized."
    assert witch.description() == "This role, while first and foremost taking on all the elements of a regular Villager throughout the game, also has the additional powers of one potion and one poison, which they may use at any point throughout the game. When the Witch is added, the Moderator will wake them up separately during the night with, “The Witch comes awake…” and follows this with “The Witch brings someone back to life.” and “The Witch poisons someone.” The Witch will then point to the person they want to poison or bring back to life. While the Witch can only use their potion and poison once, each action must be said each night to retain anonymity as to what has been done. They can only use one per evening until both are gone, and have the ability to save them until a point in the game they deem fit."
    assert alpha.description() == "This role, while first and foremost taking on all the elements of a regular Werewolf throughout the game, also has the additional burden of saying the word “Werewolf” at least once during the day. This is a challenge, because everyone playing will need to actively avoid saying the word “Werewolf” in an attempt to root out the Alpha Werewolf, who must say it at least once. In order for the Moderator to know which of the Werewolfs is the Alpha, we recommend having that person raise their hand the first time the Werewolves come awake at night, and making a note. If the Alpha Werewolf fails to say “Werewolf” during the day, they automatically die the next night."

def test_Game_set_roles():
    """Validates the Game.set_roles() method.

    Notes
    -----
    Since there are 5 players there should be two werewolfs (one an alpha), a seer
    a doctor, and one other rando.
    """
    p1 = Player("Kieran")
    p2 = Player("James")
    p3 = Player("Frank")
    p4 = Player("Megan")
    p5 = Player("Janice")

    for player in [p1,p2,p3,p4, p5]:
        assert player.role == False

    game = Game(p1)
    game.players = game.set_roles([p1,p2,p3,p4, p5])

    seer = False
    doctor = False
    alpha = False
    werewolf = False

    for player in game.players:
        assert player.role != False # Make sure player has a role

        print(player.role.name)

        if player.role.value == 0:
            werewolf = True

        if player.role.value == 2:
            seer = True
        
        if player.role.value == 3:
            doctor = True

        if player.role.value == 6:
            alpha = True

    # Check each role has been assigned
    for label, role in zip(["seer", "doctor", "alpha", "werewolf"], [seer, doctor, alpha, werewolf]): 
        print(label, role)
        assert role == True 
