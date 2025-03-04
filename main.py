from Simulation import Simulation
import os
import time

def main():
    simulation = Simulation()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if simulation.building.floors:
            print(f"=== SIMULACIÓN ZOMBI - TURNO {simulation.turn} ===")
            print(simulation.building)
        else:
            print("=== SIMULACIÓN ZOMBI ===")
            print("Edificio no inicializado. Por favor configure el edificio.")
        
        print("\nOPCIONES:")
        print("1. Configurar edificio")
        print("2. Mostrar estado del edificio")
        print("3. Avanzar simulación")
        print("4. Limpiar habitación")
        print("5. Bloquear habitación")
        print("6. Desbloquear habitación")
        print("7. Resetear sensor")
        print("8. Guardar estado")
        print("9. Cargar estado")
        print("10. Salir")
        
        option = input("\nSeleccione una opción: ")
        
        if option == "1":
            try:
                floors = int(input("Número de pisos: "))
                rooms = int(input("Habitaciones por piso: "))
                zombies = int(input("Número inicial de zombis: "))
                
                if floors <= 0 or rooms <= 0 or zombies <= 0:
                    print("Por favor ingrese valores positivos")
                    time.sleep(2)
                    continue
                
                simulation.setup_building(floors, rooms, zombies)
                print(f"Edificio creado con {floors} pisos y {rooms} habitaciones por piso")
                print(f"Se han añadido {zombies} zombis iniciales")
                time.sleep(2)
            except ValueError:
                print("Por favor ingrese números válidos")
                time.sleep(2)
        
        elif option == "2":
            simulation.display_status()
            input("\nPresione Enter para continuar...")
        
        elif option == "3":
            if not simulation.building.floors:
                print("Primero debe configurar el edificio")
                time.sleep(2)
                continue
            
            expansion_type = input("Tipo de propagación (1: Expansión, 2: Movimiento): ")
            exp_type = "expansion" if expansion_type != "2" else "movement"
            
            new_infections = simulation.advance_turn(exp_type)
            print(f"Turno avanzado. {new_infections} nuevas habitaciones infectadas.")
            time.sleep(2)
        
        elif option == "4":
            if not simulation.building.floors:
                print("Primero debe configurar el edificio")
                time.sleep(2)
                continue
            
            try:
                floor = int(input("Número de piso: "))
                room = int(input("Número de habitación: "))
                simulation.clean_room(floor, room)
                time.sleep(2)
            except ValueError:
                print("Por favor ingrese números válidos")
                time.sleep(2)
        
        elif option == "5":
            if not simulation.building.floors:
                print("Primero debe configurar el edificio")
                time.sleep(2)
                continue
            
            try:
                floor = int(input("Número de piso: "))
                room = int(input("Número de habitación: "))
                simulation.block_room(floor, room)
                time.sleep(2)
            except ValueError:
                print("Por favor ingrese números válidos")
                time.sleep(2)
        
        elif option == "6":
            if not simulation.building.floors:
                print("Primero debe configurar el edificio")
                time.sleep(2)
                continue
            
            try:
                floor = int(input("Número de piso: "))
                room = int(input("Número de habitación: "))
                simulation.unblock_room(floor, room)
                time.sleep(2)
            except ValueError:
                print("Por favor ingrese números válidos")
                time.sleep(2)
        
        elif option == "7":
            if not simulation.building.floors:
                print("Primero debe configurar el edificio")
                time.sleep(2)
                continue
            
            try:
                floor = int(input("Número de piso: "))
                room = int(input("Número de habitación: "))
                simulation.reset_sensor(floor, room)
                time.sleep(2)
            except ValueError:
                print("Por favor ingrese números válidos")
                time.sleep(2)
        
        elif option == "8":
            simulation.save_state()
            time.sleep(2)
        
        elif option == "9":
            simulation.load_state()
            time.sleep(2)
        
        elif option == "10":
            print("¡Gracias por jugar!")
            break
        
        else:
            print("Opción no válida")
            time.sleep(1)
            
            
            
if __name__ == "__main__":
    main()