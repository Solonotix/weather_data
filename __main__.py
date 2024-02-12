from pprint import PrettyPrinter

from Config import Config
from provider import TimeSeriesOptions, Synoptic


def main(config: Config, printer: PrettyPrinter):
    printer.pprint(f'Hi, {config.synoptic}')
    printer.pprint('Get Time Series from Synoptic')

    options = TimeSeriesOptions().add_state('CO').add_station('AD-123')

    printer.pprint(Synoptic(config.synoptic).get_time_series(options))


config = Config()
pprint = PrettyPrinter(indent=2, width=180, sort_dicts=True, underscore_numbers=True)
main(config, pprint)
