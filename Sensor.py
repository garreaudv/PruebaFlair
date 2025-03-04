from SensorState import SensorState

class Sensor:
    def __init__(self):
        self.state = SensorState.NORMAL
    
    def set_alert(self):
        self.state = SensorState.ALERT
    
    def reset(self):
        self.state = SensorState.NORMAL
    
    def __str__(self):
        return f"{self.state.value}"