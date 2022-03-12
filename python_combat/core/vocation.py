from python_combat.core.stats import WARRIOR_STATS, ROGUE_STATS, MAGE_STATS
import textwrap


class Vocation:
    def __init__(
        self,
        name: str,
        max_health: int,
        max_stamina: int,
        max_attack: int,
        max_defense: int,
        skills: list = [],
    ) -> None:
        self.name = name
        self.max_health = max_health
        self.max_stamina = max_stamina
        self.max_attack = max_attack
        self.max_defense = max_defense
        self.skills = skills

    def __repr__(self) -> str:
        return textwrap.dedent(
            f"""
            Class: {self.name}
            Health: {self.health}
            Stamina: {self.stamina}
            Attack: {self.attack}
            Defense: {self.defense}"""
        )


warrior = Vocation("Warrior", **WARRIOR_STATS, skills=[])
rogue = Vocation("Rogue", **ROGUE_STATS, skills=[])
mage = Vocation("Mage", **MAGE_STATS, skills=[])
