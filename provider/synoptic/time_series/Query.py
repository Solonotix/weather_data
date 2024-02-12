from typing import Self

from .Altimeter import Altimeter
from .BoundingBox import BoundingBox
from .Complete import Complete
from .Height import Height
from .Precipitation import Precipitation
from .Pressure import Pressure
from .Radius import Radius
from .Speed import Speed
from .Status import Status
from .Temperature import Temperature
from .TimezonePreference import TimezonePreference
from .Units import Units


class Query(object):
    def __init__(self):
        # Alias: stid
        self.station_ids: list[str] = list()
        # Alias: state
        self.states: list[str] = list()
        # Alias: country
        self.countries: list[str] = list()
        # Alias: nwszone
        self.nws_zones: list[str] = list()
        # Alias: nwsfirezone
        self.nws_fire_zones: list[str] = list()
        # Alias: cwa
        self.country_warning_areas: list[str] = list()
        # Alias: gacc
        self.geo_area_coord_centers: list[str] = list()
        # Alias subgacc
        self.sub_geo_area_coord_center: list[str] = list()
        # Alias: county
        self.counties: list[str] = list()
        # Alias: vars (required)
        self.sensor_variables: list[str] = list()
        # Alias: varsoperator
        self.vars_operator = 'or'
        # Alias: network
        self.network_ids: list[str] = list()
        # Alias: radius, format: [latitude, longitude, miles] or [station_id, miles]
        self.radius: Radius | None = None
        self.limit: int | None = None
        # Alias: bbox
        self.bounding_box: BoundingBox | None = None
        # Alias: status
        self.status: Status = Status.ALL
        # Alias: complete
        self.complete: Complete = Complete.DEFAULT
        # Alias: fields
        self.fields: list[str] = list()
        # Alias: obtimezone
        self.observed_timezone: TimezonePreference = TimezonePreference.DEFAULT
        # Alias: showemptystations
        self.show_empty_stations: bool = False
        # Alias: units
        self.units: str = str(Units.METRIC)
        # Alias: precip
        self.precipitation: bool = False

    @property
    def __dict__(self) -> dict:
        result = dict()
        if self.station_ids:
            result['stid'] = ','.join(self.station_ids)
        if self.states:
            result['state'] = ','.join(self.states)
        if self.countries:
            result['country'] = ','.join(self.countries)
        if self.nws_zones:
            result['nwszone'] = ','.join(self.nws_zones)
        if self.nws_fire_zones:
            result['nwsfirezone'] = ','.join(self.nws_fire_zones)
        if self.country_warning_areas:
            result['cwa'] = ','.join(self.country_warning_areas)
        if self.geo_area_coord_centers:
            result['gacc'] = ','.join(self.geo_area_coord_centers)
        if self.geo_area_coord_centers:
            result['sgacc'] = ','.join(self.sub_geo_area_coord_center)
        if self.counties:
            result['county'] = ','.join(self.counties)
        if self.sensor_variables:
            result['vars'] = ','.join(self.sensor_variables)
        if self.vars_operator:
            result['varsoperator'] = self.vars_operator
        if self.network_ids:
            result['network'] = ','.join(self.network_ids)
        if self.radius:
            result['radius'] = self.radius
            if self.limit:  # Only respected if a radius has been defined
                result['limit'] = self.limit
        if self.bounding_box:
            result['bbox'] = str(self.bounding_box)
        if self.status:
            result['status'] = self.status
        if self.complete:
            result['complete'] = 1 if self.complete else 0
        if self.fields:
            result['fields'] = ','.join(self.fields)
        if self.observed_timezone:
            result['obtimezone'] = self.observed_timezone
        if self.show_empty_stations:
            result['showemptystations'] = 'on' if self.show_empty_stations else 'off'
        if self.units:
            result['units'] = self.units
        if self.precipitation:
            result['precip'] = 1 if self.precipitation else 0

        return result

    def set_units(self, units: Units = Units.DEFAULT, /, temp: Temperature = None, speed: Speed = None, pressure: Pressure = None, height: Height = None, precipitation: Precipitation = None, altimeter: Altimeter = None) -> Self:
        self.units = units
        if temp is not None:
            self.units = "{},temp|{}".format(self.units, temp)
        if speed is not None:
            self.units = "{},speed|{}".format(self.units, speed)
        if pressure is not None:
            self.units = "{},pressure|{}".format(self.units, pressure)
        if height is not None:
            self.units = "{},height|{}".format(self.units, height)
        if precipitation is not None:
            self.units = "{},precipitation|{}".format(self.units, precipitation)
        if altimeter is not None:
            self.units = "{},altimeter|{}".format(self.units, altimeter)

        return self
