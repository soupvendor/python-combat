from python_combat.core.vocation import Vocation


class Player():
    
    def __init__(self, name: str, class_: Vocation) -> None:
        self.name = name
        self.class_ = class_
        self.health = class_.max_health
        self.stamina = class_.max_stamina
        self.attack = class_.max_attack
        self.defense = class_.max_defense

    def show_stats(self):
        print(self.name, self.vocation, self.max_health, self.max_stamina, self.max_attack, self.max_defense)

    def pick_vocation(self, vocation):
        vocation = vocation.lower()
        vocations = ["mage", "warrior", "thief"]
        while vocation not in vocations:
            vocation = input("Choose a valid vocation: Mage, Warrior, or Thief. ")
        if vocation == vocations[0]:  # Mage
            self.max_health = 75
            self.max_stamina = 75
            self.max_attack  # 25 default
            self.max_defense = 35
            self.vocation = "Mage"
            self.skills = ["Ember Beam", "Arcane Shield", "Brittle Armor", "Soul for a Soul"]
        elif vocation == vocations[1]:  # Warrior
            self.max_health = 150
            self.max_stamina = 75
            self.max_attack = 35
            self.max_defense = 15
            self.vocation = "Warrior"
            self.skills = ["Bloodlust", "Immortal Stand", "Cripple Armor", "Decapitate"]
        elif vocation == vocations[2]:  # Thief
            self.max_health = 80
            self.max_stamina = 100
            self.max_attack = 45
            self.max_defense = 5
            self.vocation = "Thief"
            self.skills = ["Hidden Blade", "Display of Powder", "Immobilizing Slash", "Blanket of Blades"]
        self.health = self.max_health
        self.stamina = self.max_stamina
        self.attack = self.max_attack
        self.defense = self.max_defense

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
