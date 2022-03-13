from python_combat.core.room import rooms


class Game:
    def __init__(self):
        self.rooms = rooms

    def show_room(self, room_id: int) -> None:
        room = self.rooms[room_id]
        room.print()
