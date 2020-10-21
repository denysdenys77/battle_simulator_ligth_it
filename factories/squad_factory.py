from interfaces.squard_interface import SquadABC
from realisations.squad import Squad
from .unit_factory import UnitFactory
from random import choice


class SquadFactory:

    @staticmethod
    def create(number_of_units: int) -> SquadABC:
        """
        Creating an army class instance
        with specified count of units.
        """

        unit_types = ['soldier', 'vehicle']
        units_list = []
        if 5 <= number_of_units <= 10:
            for _ in range(number_of_units):
                unit_type = choice(unit_types)
                unit = UnitFactory.create(unit_type=unit_type)
                units_list.append(unit)
            return Squad(units=units_list)
        raise Exception('Possible number of '
                        'units per squad: 5 <= n <= 10.')
