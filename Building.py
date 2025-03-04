from Floor import Floor
import random
from SensorState import SensorState

class Building:
    def __init__(self, floors_count=0, rooms_per_floor=0):
        self.floors = []
        if floors_count > 0 and rooms_per_floor > 0:
            self.initialize(floors_count, rooms_per_floor)
    
    def initialize(self, floors_count, rooms_per_floor):
        self.floors = [Floor(i, rooms_per_floor) for i in range(floors_count)]
    
    def get_all_rooms(self):
        all_rooms = []
        for floor in self.floors:
            all_rooms.extend(floor.rooms)
        return all_rooms
    
    def get_room(self, floor_number, room_number):
        if 0 <= floor_number < len(self.floors):
            floor = self.floors[floor_number]
            if 0 <= room_number < len(floor.rooms):
                return floor.rooms[room_number]
        return None
    
    def get_adjacent_rooms(self, floor_number, room_number):
        adjacent_rooms = []
        if 0 <= floor_number < len(self.floors):
            adjacent_rooms.extend(self.floors[floor_number].get_adjacent_rooms(room_number))
            
            if floor_number > 0 and room_number < len(self.floors[floor_number-1].rooms):
                adjacent_rooms.append(self.floors[floor_number-1].rooms[room_number])
            
            if floor_number < len(self.floors) - 1 and room_number < len(self.floors[floor_number+1].rooms):
                adjacent_rooms.append(self.floors[floor_number+1].rooms[room_number])
        
        return adjacent_rooms
    
    def add_initial_zombies(self, count=1):
        all_rooms = self.get_all_rooms()
        if not all_rooms:
            return False
        
        available_rooms = [room for room in all_rooms if not room.has_zombies and not room.is_blocked]
        if not available_rooms:
            return False
        
        for _ in range(min(count, len(available_rooms))):
            room = random.choice(available_rooms)
            room.add_zombie()
            available_rooms.remove(room)
        
        return True
    
    def count_zombies(self):
        return sum(1 for room in self.get_all_rooms() if room.has_zombies)
    
    def __str__(self):
        if not self.floors:
            return "Edificio no inicializado"
        
        total_rooms = sum(len(floor.rooms) for floor in self.floors)
        zombie_count = self.count_zombies()
        
        result = f"Edificio con {len(self.floors)} pisos y {total_rooms} habitaciones\n"
        result += f"Estado actual: {zombie_count} habitaciones con zombis\n"
        
        for floor in self.floors:
            result += f"{floor}\n"
        
        return result

    def to_dict(self):
        return {
            'floors': [
                {
                    'floor_number': floor.floor_number,
                    'rooms': [
                        {
                            'floor_number': room.floor_number,
                            'room_number': room.room_number,
                            'has_zombies': room.has_zombies,
                            'is_blocked': room.is_blocked,
                            'sensor_state': room.sensor.state.value
                        } for room in floor.rooms
                    ]
                } for floor in self.floors
            ]
        }

    @classmethod
    def from_dict(cls, data):
        building = cls()
        if not data['floors']:
            return building
        
        # Initialize with the first floor's room count
        floors_count = len(data['floors'])
        rooms_per_floor = len(data['floors'][0]['rooms'])
        building.initialize(floors_count, rooms_per_floor)
        
        # Restore state
        for floor_data, floor in zip(data['floors'], building.floors):
            for room_data, room in zip(floor_data['rooms'], floor.rooms):
                room.has_zombies = room_data['has_zombies']
                room.is_blocked = room_data['is_blocked']
                room.sensor.state = SensorState(room_data['sensor_state'])
        
        return building