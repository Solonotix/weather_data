from .Radius import Radius


class Coordinates(Radius):
    def __init__(self, latitude: float, longitude: float, miles: int, limit: int = None):
        super().__init__(latitude=latitude, longitude=longitude, miles=miles, limit=limit)
