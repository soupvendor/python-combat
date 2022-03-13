class Skill:
    def __init__(self, name: str, desc: str) -> None:
        self.name = name
        self.desc = desc

    def __repr__(self) -> str:
        return self.name
