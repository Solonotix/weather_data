from .Radius import Radius


class Station(Radius):
    def __init__(self, station_id: str, miles: int, limit: int = None):
        super().__init__(station=station_id, miles=miles, limit=None)
