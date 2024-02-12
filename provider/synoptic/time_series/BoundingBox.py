class BoundingBox(object):
    def __init__(self, longitude_min: int, latitude_min: int, longitude_max: int, latitude_max: int):
        self.longitude_min = longitude_min
        self.latitude_min = latitude_min
        self.longitude_max = longitude_max
        self.latitude_max = latitude_max

    def __str__(self) -> str:
        return f"{self.longitude_min},{self.latitude_min},{self.longitude_max},{self.latitude_max}"
