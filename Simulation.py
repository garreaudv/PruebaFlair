from Building import Building
import os
import random
import json

class Simulation:
    def __init__(self):
        self.building = Building()
        self.turn = 0
    
    def setup_building(self, floors_count, rooms_per_floor, initial_zombies=1):
        self.building = Building(floors_count, rooms_per_floor)
        self.building.add_initial_zombies(initial_zombies)
        self.turn = 0
    
    def advance_turn(self, expansion_type="expansion"):
        """Advance the simulation by one turn."""
        self.turn += 1
        zombie_rooms = self._get_zombie_rooms()
        new_infections = self._calculate_new_infections(zombie_rooms)
        
        if expansion_type == "movement":
            self._clear_original_zombie_rooms(zombie_rooms)
        
        self._infect_new_rooms(new_infections)
        return len(new_infections)
    
    def _get_zombie_rooms(self):
        """Return list of rooms containing zombies."""
        return [room for room in self.building.get_all_rooms() if room.has_zombies]
    
    def _calculate_new_infections(self, zombie_rooms, propagation_probability=0.7):
        """Calculate which new rooms will be infected by zombies."""
        new_infections = []
        for room in zombie_rooms:
            available_rooms = self._get_available_adjacent_rooms(room)
            new_infections.extend(
                room for room in available_rooms 
                if random.random() < propagation_probability
            )
        return new_infections
    
    def _get_available_adjacent_rooms(self, room):
        """Get adjacent rooms that can be infected."""
        adjacent_rooms = self.building.get_adjacent_rooms(room.floor_number, room.room_number)
        return [adj for adj in adjacent_rooms if not adj.has_zombies and not adj.is_blocked]
    
    def _clear_original_zombie_rooms(self, zombie_rooms):
        """Remove zombies from their original rooms during movement."""
        for room in zombie_rooms:
            room.remove_zombie()
    
    def _infect_new_rooms(self, rooms_to_infect):
        """Add zombies to newly infected rooms."""
        for room in rooms_to_infect:
            room.add_zombie()
    
    def display_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== SIMULACIÓN ZOMBI - TURNO {self.turn} ===")
        print(self.building)
    
    def clean_room(self, floor_number, room_number):
        room = self.building.get_room(floor_number, room_number)
        if room:
            if room.remove_zombie():
                print(f"Habitación limpiada en piso {floor_number}, habitación {room_number}")
                return True
            else:
                print("Esta habitación no tiene zombis")
        else:
            print("Habitación no encontrada")
        return False
    
    def block_room(self, floor_number, room_number):
        room = self.building.get_room(floor_number, room_number)
        if room:
            if not room.is_blocked:
                room.block_room()
                print(f"Habitación bloqueada en piso {floor_number}, habitación {room_number}")
                return True
            else:
                print("Esta habitación ya está bloqueada")
        else:
            print("Habitación no encontrada")
        return False
    
    def unblock_room(self, floor_number, room_number):
        room = self.building.get_room(floor_number, room_number)
        if room:
            if room.is_blocked:
                room.unblock_room()
                print(f"Habitación desbloqueada en piso {floor_number}, habitación {room_number}")
                return True
            else:
                print("Esta habitación no está bloqueada")
        else:
            print("Habitación no encontrada")
        return False
    
    def reset_sensor(self, floor_number, room_number):
        room = self.building.get_room(floor_number, room_number)
        if room:
            if not room.has_zombies:
                room.sensor.reset()
                print(f"Sensor reseteado en piso {floor_number}, habitación {room_number}")
                return True
            else:
                print("No se puede resetear el sensor mientras hay zombis en la habitación")
        else:
            print("Habitación no encontrada")
        return False

    def save_state(self, filename="simulation_state.json"):
        state = {
            'turn': self.turn,
            'building': self.building.to_dict()
        }
        try:
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
            print(f"Estado guardado en {filename}")
            return True
        except Exception as e:
            print(f"Error al guardar el estado: {e}")
            return False

    def load_state(self, filename="simulation_state.json"):
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            self.turn = state['turn']
            self.building = Building.from_dict(state['building'])
            print(f"Estado cargado desde {filename}")
            return True
        except FileNotFoundError:
            print("No se encontró archivo de guardado previo")
            return False
        except Exception as e:
            print(f"Error al cargar el estado: {e}")
            return False