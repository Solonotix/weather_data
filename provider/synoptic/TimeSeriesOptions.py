from typing import Self

from .time_series import *


class TimeSeriesOptions(object):
    def __init__(self):
        self.query = TimeSeriesQuery()

    def add_country(self, country: str) -> Self:
        self.query.countries.append(country)
        return self

    def add_country_warning_area(self, country_warning_area: str) -> Self:
        self.query.country_warning_areas.append(country_warning_area)
        return self

    def add_county(self, county: str) -> Self:
        self.query.counties.append(county)
        return self

    def add_field(self, field: str) -> Self:
        self.query.fields.append(field)
        return self

    def add_geo_area_coord_center(self, geo_area_coord_center: str) -> Self:
        self.query.geo_area_coord_centers.append(geo_area_coord_center)
        return self

    def add_network_id(self, network_id: str) -> Self:
        self.query.network_ids.append(network_id)
        return self

    def add_nws_fire_zone(self, fire_zone: str) -> Self:
        self.query.nws_fire_zones.append(fire_zone)
        return self

    def add_nws_zone(self, zone: str) -> Self:
        self.query.nws_zones.append(zone)
        return self

    def add_sensor_variable(self, sensor_variable: str) -> Self:
        self.query.sensor_variables.append(sensor_variable)
        return self

    def add_state(self, state: str) -> Self:
        self.query.states.append(state)
        return self

    def add_station(self, station: str) -> Self:
        self.query.station_ids.append(station)
        return self

    def add_sub_geo_area_coord_center(self, sub_geo_area_coord_center: str) -> Self:
        self.query.sub_geo_area_coord_center.append(sub_geo_area_coord_center)
        return self

    def build(self) -> dict:
        return self.query.__dict__

    def set_bounding_box(self, latitude_min: float, latitude_max: float, longitude_min: float, longitude_max: float) -> Self:
        self.query.bounding_box = TimeSeriesBoundingBox(longitude_min, latitude_min, longitude_max, latitude_max)
        return self

    def set_derived_precipitation(self, enable: bool) -> Self:
        self.query.precipitation = enable
        return self

    def set_extended_attributes(self, enable: bool) -> Self:
        self.query.complete = TimeSeriesComplete.EXTENDED if enable else TimeSeriesComplete.DEFAULT
        return self

    def set_observed_timezone(self, preference: str) -> Self:
        if preference != "local":
            self.query.observed_timezone = TimeSeriesTimezonePreference.DEFAULT  # UTC
        else:
            self.query.observed_timezone = TimeSeriesTimezonePreference.LOCAL

        return self

    def set_radius_by_coordinates(self, latitude: float, longitude: float, miles: int, limit: int = None) -> Self:
        self.query.radius = TimeSeriesRadius(latitude=latitude, longitude=longitude, miles=miles)
        self.query.limit = limit
        return self

    def set_radius_by_station(self, station_id: str, miles: int, limit: int = None) -> Self:
        self.query.radius = TimeSeriesRadius(station=station_id, miles=miles)
        self.query.limit = limit
        return self

    def set_show_empty_stations(self, enable: bool) -> Self:
        self.query.show_empty_stations = enable
        return self

    def set_status(self, status: str) -> Self:
        match status:
            case TimeSeriesStatus.ALL:
                self.query.status = status
            case TimeSeriesStatus.INACTIVE:
                self.query.status = status
            case _:
                self.query.status = TimeSeriesStatus.ACTIVE

        return self

    def set_units(self, units: str) -> Self:
        self.query.units = TimeSeriesUnitsBuilder.from_string(units).build()
        return self

    def set_vars_operator(self, operator: str) -> Self:
        self.query.vars_operator = operator if operator == 'and' else 'or'
        return self
