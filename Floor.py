from Room import Room

class Floor:
    def __init__(self, floor_number, rooms_count):
        self.floor_number = floor_number
        self.rooms = [Room(floor_number, i) for i in range(rooms_count)]
    
    def get_adjacent_rooms(self, room_number):
        adjacent_rooms = []
        if room_number > 0:
            adjacent_rooms.append(self.rooms[room_number - 1])
        if room_number < len(self.rooms) - 1:
            adjacent_rooms.append(self.rooms[room_number + 1])
        return adjacent_rooms
    
    def __str__(self):
        result = f"Piso {self.floor_number}:\n"
        for room in self.rooms:
            result += f"  {room}\n"
        return result