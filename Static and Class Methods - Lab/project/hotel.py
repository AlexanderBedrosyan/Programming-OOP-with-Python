from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = ''
        for i in range(len(self.rooms) - 1, - 1, - 1):
            if self.rooms[i].number == room_number:
                result = self.rooms[i].take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        result = ''
        room_guests = 0
        for i in range(len(self.rooms) - 1, - 1, - 1):
            if self.rooms[i].number == room_number:
                room_guests = self.rooms[i].guests
                result = self.rooms[i].free_room()

        if result:
            return result

        self.guests -= room_guests

    def status(self):
        free_rooms = []
        taken_rooms = []
        for obj in self.rooms:
            if obj.is_taken:
                taken_rooms.append(obj.number)
            else:
                free_rooms.append(obj.number)
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(ch) for ch in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(ch) for ch in taken_rooms)}"
