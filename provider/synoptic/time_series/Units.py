from enum import Enum
from typing import Self

from .Altimeter import Altimeter
from .Height import Height
from .Precipitation import Precipitation
from .Pressure import Pressure
from .Speed import Speed
from .Temperature import Temperature


class Units(Enum):
    DEFAULT = "metric",
    METRIC = "metric",
    ENGLISH = "english"


class UnitsBuilder(object):
    def __init__(self):
        self.altimeter: Altimeter | None = None
        self.height: Height | None = None
        self.precipitation: Precipitation | None = None
        self.pressure: Pressure | None = None
        self.speed: Speed | None = None
        self.temperature: Temperature | None = None
        self.units: Units = Units.DEFAULT

    def __iter__(self):
        if self.altimeter is not None:
            yield 'altimeter', self.altimeter
        if self.height is not None:
            yield 'height', self.height
        if self.pressure is not None:
            yield 'pressure', self.pressure
        if self.speed is not None:
            yield self.speed
        if self.temperature is not None:
            yield self.temperature

    def build(self):
        units = [self.units] + ['{}|{}'.format(k, v) for k, v in self]
        return ','.join(units)

    @classmethod
    def from_string(cls, units: str) -> Self:
        builder = cls()
        for value in units.split(','):
            match value.split('|'):
                case ['alti', arg]:
                    builder.set_altimeter(arg)
                case ['height', arg]:
                    builder.set_height(arg)
                case ['precip', arg]:
                    builder.set_pressure(arg)
                case ['pres', arg]:
                    builder.set_pressure(arg)
                case ['speed', arg]:
                    builder.set_speed(arg)
                case ['temp', arg]:
                    builder.set_temperature(arg)
                case [arg]:
                    builder.set_units(arg)

        return builder

    def set_altimeter(self, altimeter: str) -> Self:
        match altimeter.lower():
            case Altimeter.MERCURY:
                self.altimeter = Altimeter.MERCURY
            case _:
                self.altimeter = Altimeter.PASCALS

        return self

    def set_height(self, height: str) -> Self:
        match height.lower():
            case Height.FEET:
                self.height = Height.FEET
            case _:
                self.height = Height.METERS

        return self

    def set_precipitation(self, precipitation: str) -> Self:
        match precipitation.lower():
            case Precipitation.INCHES:
                self.precipitation = Precipitation.INCHES
            case Precipitation.CENTIMETERS:
                self.precipitation = Precipitation.CENTIMETERS
            case _:
                self.precipitation = Precipitation.MILLIMETERS

        return self

    def set_pressure(self, pressure: str) -> Self:
        match pressure.lower():
            case Pressure.MERCURY:
                self.pressure = Pressure.MERCURY
            case Pressure.MILLIBARS:
                self.pressure = Pressure.MILLIBARS
            case _:
                self.pressure = Pressure.PASCALS

        return self

    def set_speed(self, speed: str) -> Self:
        match speed.lower():
            case Speed.KNOTS:
                self.speed = Speed.KNOTS
            case Speed.MILES:
                self.speed = Speed.MILES
            case Speed.KILOMETERS:
                self.speed = Speed.KILOMETERS
            case _:
                self.speed = Speed.METERS

        return self

    def set_temperature(self, temperature: str) -> Self:
        match temperature.lower():
            case Temperature.FAHRENHEIT:
                self.temperature = Temperature.FAHRENHEIT
            case Temperature.KELVIN:
                self.temperature = Temperature.KELVIN
            case _:
                self.temperature = Temperature.CELSIUS

        return self

    def set_units(self, units: str) -> Self:
        self.units = units if units.lower() == Units.ENGLISH else Units.DEFAULT
        return self
