from requests import get

from .synoptic import TimeSeriesOptions


class Synoptic(object):
    address = "https://api.synopticdata.com/v2"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_time_series(self, options: TimeSeriesOptions):
        params = options.build()
        params['token'] = self.api_key
        return get("{}/stations/timeseries".format(Synoptic.address), params=params).json()
