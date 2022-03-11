from python_combat.core.game import Game
from python_combat.characters.player import Player
from python_combat.characters.enemy import Enemy
from python_combat.core.battle import Battle

if __name__ == "__main__":
    game = Game()
    player1 = Player()
    enemy = Enemy()
    battle = Battle(player1, enemy)
    player1.name = input("What is your name? ")
    player1.pick_vocation(input("What is your vocation? Mage, Warrior, or Thief? "))
    player1.show_skills()
    game.intro_room("Bloodied Hallway")
    enemy.summon_monster("Agalageli")
    battle.print_stuff()
    battle.turn()
