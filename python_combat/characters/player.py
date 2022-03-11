from python_combat.characters.character import Character


class Player(Character):
    def character_create(self):
        self.name = None
        self.vocation = None

    def show_stats(self):
        print(self.name, self.vocation, self.maxhealth, self.maxstamina, self.maxattack, self.maxdefense)

    def pick_vocation(self, vocation):
        vocation = vocation.lower()
        vocations = ["mage", "warrior", "thief"]
        while vocation not in vocations:
            vocation = input("Choose a valid vocation: Mage, Warrior, or Thief. ")
        if vocation == vocations[0]:  # Mage
            self.maxhealth = 75
            self.maxstamina = 75
            self.maxattack  # 25 default
            self.maxdefense = 35
            self.vocation = "Mage"
            self.skills = ["Ember Beam", "Arcane Shield", "Brittle Armor", "Soul for a Soul"]
        elif vocation == vocations[1]:  # Warrior
            self.maxhealth = 150
            self.maxstamina = 75
            self.maxattack = 35
            self.maxdefense = 15
            self.vocation = "Warrior"
            self.skills = ["Bloodlust", "Immortal Stand", "Cripple Armor", "Decapitate"]
        elif vocation == vocations[2]:  # Thief
            self.maxhealth = 80
            self.maxstamina = 100
            self.maxattack = 45
            self.maxdefense = 5
            self.vocation = "Thief"
            self.skills = ["Hidden Blade", "Display of Powder", "Immobilizing Slash", "Blanket of Blades"]
        self.health = self.maxhealth
        self.stamina = self.maxstamina
        self.attack = self.maxattack
        self.defense = self.maxdefense

    def show_skills(self):
        skill_desc = {
            "Ember Beam": "A beam of ember",
            "Arcane Shield": "Exactly what you think",
            "Brittle Armor": "Cold snap that reduces enemy armor",
            "Soul for a Soul": "An execute ability where the soul of the caster and enemy duel; whichever soul is weaker dies",
            "Bloodlust": "A high stamina, powerful attack",
            "Immortal Stand": "An extreme boost to defense",
            "Cripple Armor": "A blunt blow reducing armor",
            "Decapitate": "A gruesome execute ability leaving the user exposed. If the execute fails, you die",
            "Hidden Blade": "An unexpected strike, avoiding enemy defense",
            "Display of Powder": "A smoke screen that makes the thief nearly invincible",
            "Immobilizing Slash": "A defense reducing slash",
            "Blanket of Blades": "An execute ability that instantly kills an enemy of equal or less health. If the execute fails, you die",
        }
        try:
            for skill in self.skills:
                if skill in skill_desc:
                    print(f"{skill}: {skill_desc[skill]}.")
        except Exception:
            # TODO: Fix exception
            print("out to lunch fix later")
