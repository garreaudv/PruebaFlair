from Sensor import Sensor

class Room:
    def __init__(self, floor_number, room_number):
        self.floor_number = floor_number
        self.room_number = room_number
        self.has_zombies = False
        self.sensor = Sensor()
        self.is_blocked = False
    
    def add_zombie(self):
        if not self.is_blocked and not self.has_zombies:
            self.has_zombies = True
            self.sensor.set_alert()
            return True
        return False
    
    def remove_zombie(self):
        if self.has_zombies:
            self.has_zombies = False
            return True
        return False
    
    def block_room(self):
        self.is_blocked = True
    
    def unblock_room(self):
        self.is_blocked = False
    
    def __str__(self):
        status = "🧟" if self.has_zombies else "  "
        blocked = "🔒" if self.is_blocked else "  "
        return f"Habitación {self.room_number}: {status} | Sensor: {self.sensor} {blocked}"