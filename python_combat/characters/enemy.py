from python_combat.characters.character import Character


class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.monster_type = None

    def show_stats(self):
        print(self.name, self.maxhealth, self.maxstamina, self.maxattack, self.maxdefense, self.monster_type)

    def summon_monster(self, monster):
        monsters = ["Walgag", "Bonborito", "Agalageli"]

        if monster == monsters[0]:  # Walgag
            self.name = "Walgag"
            self.maxhealth = 200
            self.maxstamina = 100
            self.maxattack = 15
            self.maxdefense = 30
        if monster == monsters[1]:  # Bonborito
            self.name = "Bonborito"
            self.maxhealth = 100
            self.maxstamina = 50
            self.maxattack = 10
            self.maxdefense = 50
        if monster == monsters[2]:  # Agalageli
            self.name = "Agalageli"
            self.maxhealth = 300
            self.maxstamina = 300
            self.maxattack = 20
            self.maxdefense = 0
        self.health = self.maxhealth
        self.stamina = self.maxstamina
        self.attack = self.maxattack
        self.defense = self.maxdefense
