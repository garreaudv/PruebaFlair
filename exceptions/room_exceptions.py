class RoomError(Exception):
    """Base exception class for Room-related errors"""
    pass

class SensorNotInitializedError(RoomError):
    """Raised when a room's sensor is not properly initialized"""
    pass

class ZombieAdditionError(RoomError):
    """Raised when there's an error adding a zombie to a room"""
    pass 