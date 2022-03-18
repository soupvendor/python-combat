from python_combat.core.skill import Skill
from python_combat.core.vocation import Vocation
from python_combat.core.stats import WARRIOR_STATS, ROGUE_STATS, MAGE_STATS

#  Warrior
war_skills = [
    Skill("Bloodlust", "A high stamina, powerful attack."),
    Skill("Immortal Stand", "An extreme boost to defense."),
    Skill("Shatter Armor", "A blunt blow reducing armor."),
    Skill("Decapitate", "A gruesome execute ability leaving you vulnerable. If the execute fails, you die."),
]
warrior = Vocation("Warrior", **WARRIOR_STATS, skills=war_skills)

#  Rogue
rogue_skills = [
    Skill("Hidden Blade", "An unexpected strike, avoiding enemy defense."),
    Skill("Display of Powder", "A smoke screen that makes the thief nearly invincible."),
    Skill("Immobilizing Slash", "A defense reducing slash."),
    Skill(
        "Blanket of Blades",
        "An execute ability that instantly kills an enemy of equal or less health. If the execute fails, you die",
    ),
]
rogue = Vocation("Rogue", **ROGUE_STATS, skills=rogue_skills)

#  Mage
mage_skills = [
    Skill("Ember Beam", "A beam of ember"),
    Skill("Arcane Shield", "Exactly what you think"),
    Skill("Brittle Armor", "Cold snap that reduces enemy armor"),
    Skill(
        "Soul for a Soul",
        "An execute ability where the soul of the caster and enemy duel; whichever soul is weaker dies",
    ),
]
mage = Vocation("Mage", **MAGE_STATS, skills=mage_skills)

vocations = [mage, warrior, rogue]
