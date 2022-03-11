class Game:
    def __init__(self):
        self.rooms = {"1d": "Bloodied Hallway", "2d": "Dark Chamber", "3d": "Moon-lit Field"}

    def intro_room(self, room):
        if room == self.rooms["1d"]:
            print(
                "You find yourself in a hallway, circled by the light of your lantern. Past the purview of your glow, there is a nothingness staring at you."
                "\n"
                "Once you break the gaze of the abyss, you glance around your surroundings to find a grusome scene lining the walls."
                "\n"
                "You notice blood trickling down the wall, indicating that it's fresh. Soon after this realization, something approaches from the dark..."
            )
        if room == self.rooms["2d"]:
            print("")
        if room == self.rooms["3d"]:
            print("")
