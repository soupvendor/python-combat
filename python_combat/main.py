from python_combat.core.game import Game
from python_combat.core.character import Character
from python_combat.core.battle import Battle
from python_combat.core.vocation import vocations, Vocation


def pick_vocation() -> Vocation:
    vocation = None
    vocation_names = [v.name.lower() for v in vocations]

    while vocation not in vocation_names:
        vocation = input("Please choose Warrior, Rogue, or Mage. ")
        vocation = vocation.lower()
    for voc in vocations:
        if vocation == voc.name.lower():
            return voc


if __name__ == "__main__":
    game = Game()
    vocation = pick_vocation()
    player1 = Character("tory", vocation)
    print(player1)
