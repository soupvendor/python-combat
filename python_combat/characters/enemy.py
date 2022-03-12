from python_combat.characters.character import Character


class Enemy():
    def __init__(self):
        super().__init__()
        self.monster_type = None

    def show_stats(self):
        print(self.name, self.max_health, self.max_stamina, self.max_attack, self.max_defense, self.monster_type)

    def summon_monster(self, monster):
        monsters = ["Walgag", "Bonborito", "Agalageli"]

        if monster == monsters[0]:  # Walgag
            self.name = "Walgag"
            self.max_health = 200
            self.max_stamina = 100
            self.max_attack = 15
            self.max_defense = 30
        if monster == monsters[1]:  # Bonborito
            self.name = "Bonborito"
            self.max_health = 100
            self.max_stamina = 50
            self.max_attack = 10
            self.max_defense = 50
        if monster == monsters[2]:  # Agalageli
            self.name = "Agalageli"
            self.max_health = 300
            self.max_stamina = 300
            self.max_attack = 20
            self.max_defense = 0
        self.health = self.max_health
        self.stamina = self.max_stamina
        self.attack = self.max_attack
        self.defense = self.max_defense
