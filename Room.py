from Sensor import Sensor
from exceptions.room_exceptions import SensorNotInitializedError, ZombieAdditionError

class Room:
    def __init__(self, floor_number, room_number):
        self.floor_number = floor_number
        self.room_number = room_number
        self.has_zombies = False
        self.sensor = Sensor()
        self.is_blocked = False
    
    def add_zombie(self):
        try:
            if not self.can_add_zombie():
                return False
            
            return self.perform_zombie_addition()
        except SensorNotInitializedError as e:
            return self.handle_sensor_error(e)
        except Exception as e:
            return self.handle_general_error(e)

    def can_add_zombie(self):
        return not self.is_blocked and not self.has_zombies

    def perform_zombie_addition(self):
        self.has_zombies = True
        self.validate_sensor()
        self.sensor.set_alert()
        return True

    def validate_sensor(self):
        if self.sensor is None:
            raise SensorNotInitializedError("Room sensor not properly initialized")

    def handle_sensor_error(self, error):
        print(f"Sensor error: {error}")
        self.has_zombies = False
        raise

    def handle_general_error(self, error):
        print(f"Unexpected error: {error}")
        self.has_zombies = False
        raise ZombieAdditionError(f"Failed to add zombie: {str(error)}")
    
    def remove_zombie(self):
        try:
            if self.has_zombies:
                self.has_zombies = False
                self.sensor.reset() 
                return True
            return False
        except Exception as e:
            print(f"Error removing zombie: {e}")
            return False
    
    def block_room(self):
        self.is_blocked = True
    
    def unblock_room(self):
        self.is_blocked = False
    
    def __str__(self):
        status = "🧟" if self.has_zombies else "  "
        blocked = "🔒" if self.is_blocked else "  "
        return f"Habitación {self.room_number}: {status} | Sensor: {self.sensor} {blocked}"