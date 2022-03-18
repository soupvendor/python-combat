from python_combat.core.skill import Skill
from python_combat.core.vocation import Vocation
from python_combat.core.stats import CANNIBAL_STATS, BUTCHER_STATS

#  Crazed Cannibal
cannibal_skills = [
    Skill("Ravenous Bite", "A violent bite driven by insatiable hunger."),
    Skill("Haunting Gaze", "Crazed eyes peer with violent intent, lowering player defense."),
    Skill("Frenzy", "Relentless strikes that inflict damage several times, however lowering its defense."),
]
cannibal = Vocation("Crazed Cannibal", **CANNIBAL_STATS, skills=cannibal_skills)

#  Undead Butcher
butcher_skills = [
    Skill("Savage Cleave", "An impactful swing meant to dismember whatever it contacts."),
    Skill("Rancid Scraps", "The Undead Butcher flings unknown, rotten meat scraps, lowering attack."),
    Skill(
        "Evil Which Lurks", "The air thickens with an unholy aura as The Undead Butcher taps into its source of evil."
    ),
]
butcher = Vocation("Undead Butcher", **BUTCHER_STATS, skill=butcher_skills)
