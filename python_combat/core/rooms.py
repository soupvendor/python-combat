class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def print(self):
        print(self.name)
        print()
        print(self.desc)


rooms = [
    Room(
        "Bloodied Hallway",
        "You find yourself in a hallway, circled by the light of your lantern. Past the purview of your glow, there is a nothingness staring at you."
        "\n"
        "Once you break the gaze of the abyss, you glance around your surroundings to find a grusome scene lining the walls."
        "\n"
        "You notice blood trickling down the wall, indicating that it's fresh. Soon after this realization, something approaches from the dark..."
    ),
    Room(
        "Dark Chamber",
        " "
    ),
    Room(
        "Moon-lit Field",
        " "
    )
]
