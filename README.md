# Simulador de Infección Zombi

Una simulación de la propagación de zombis en un edificio, implementada en Python.

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/your-username/PruebaFlair.git
cd PruebaFlair
```

2. No se requieren dependencias adicionales, solo Python 3.x

## Ejecución

Para iniciar la simulación:
```bash
python main.py
```

## Arquitectura

El proyecto está organizado en las siguientes clases:

- **Building**: Representa el edificio y gestiona la estructura de pisos y habitaciones
- **Floor**: Maneja un piso individual y sus habitaciones
- **Room**: Representa una habitación con su estado (zombis, bloqueo) y sensor
- **Sensor**: Monitorea el estado de una habitación (NORMAL/ALERT)
- **Simulation**: Controla la lógica de la simulación y la propagación de zombis
- **SensorState**: Enumeración para los estados posibles del sensor

### Diagrama de Clases Simplificado
```
Building
 ├── Floor[]
      ├── Room[]
           ├── Sensor
                ├── SensorState
```

## Uso

La aplicación presenta un menú interactivo con las siguientes opciones:

1. **Configurar edificio**
   - Define el número de pisos
   - Define habitaciones por piso
   - Establece cantidad inicial de zombis

2. **Mostrar estado del edificio**
   - Visualiza el estado actual de todas las habitaciones
   - 🧟 indica presencia de zombis
   - 🔒 indica habitación bloqueada

3. **Avanzar simulación**
   - Elige entre dos tipos de propagación:
     - Expansión: Los zombis se mantienen en su habitación original
     - Movimiento: Los zombis se mueven a nuevas habitaciones

4. **Limpiar habitación**
   - Elimina zombis de una habitación específica

5. **Bloquear habitación**
   - Previene que los zombis entren o salgan

6. **Desbloquear habitación**
   - Permite nuevamente el movimiento de zombis

7. **Resetear sensor**
   - Restablece el sensor a estado NORMAL

8. **Guardar estado**
   - Guarda el estado actual de la simulación en un archivo JSON

9. **Cargar estado**
   - Recupera una simulación guardada previamente

10. **Salir**
    - Termina la simulación

## Persistencia

La simulación puede guardarse y cargarse usando archivos JSON. El estado guardado incluye:
- Número de turno actual
- Estado de cada habitación (zombis, bloqueos, sensores)
- Estructura completa del edificio

Los archivos se guardan por defecto como `simulation_state.json`.