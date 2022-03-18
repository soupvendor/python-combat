from python_combat.core.vocation import Vocation
import textwrap


class Character:
    def __init__(self, name: str, vocation: Vocation) -> None:
        self.name = name
        self.vocation = vocation
        self.health = vocation.max_health
        self.stamina = vocation.max_stamina
        self.attack = vocation.max_attack
        self.defense = vocation.max_defense
        self.skills = vocation.skills.copy()

    def __repr__(self) -> str:
        return textwrap.dedent(
            f"""
            Name: {self.name}
            Health: {self.health}
            Stamina: {self.stamina}
            Attack: {self.attack}
            Defense: {self.defense}
            Skills: {", ".join([str(skill) for skill in self.skills])}"""
        )
