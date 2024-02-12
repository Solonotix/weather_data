class Radius(object):
    def __init__(self, **kwargs):
        self.latitude = kwargs.get('latitude', None)
        self.longitude = kwargs.get('longitude', None)
        self.miles = kwargs.get('miles', 10)
        self.station = kwargs.get('station', None)

    def __str__(self) -> str:
        if self.station:
            return "{},{}".format(self.station, self.miles)
        else:
            return "{},{},{}".format(self.latitude, self.longitude, self.miles)
