class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def print_stuff(self):
        print(self.player.name, self.enemy.name)

    def show_info(self, Player, Enemy):
        print(
            f"You have {Player.health} health, {Player.stamina} stamina, {Player.attack}, and {Player.defense} defense."
        )
        print(
            f"The {Enemy.name} has {Enemy.health} health, {Enemy.stamina} stamina, {Enemy.attack} attack, and {Enemy.defense} defense. "
        )

    def turn(self):
        print(self.player.skills)
