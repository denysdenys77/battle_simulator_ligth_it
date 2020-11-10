from random import randint

from warring.interface import WarringABC
from warring.soldier_realization import Soldier
from warring.vehicle_realization import Vehicle


class UnitFactory:

    def create(self, unit_type: str) -> WarringABC:
        """Returning unit instance of specified unit type"""

        units = {
            'soldier': Soldier(),
            'vehicle': Vehicle([Soldier() for _ in list(range(randint(1, 3)))])
        }

        if unit_type in units.keys():
            return units[unit_type]
        raise Exception("'unit_type' field value should "
                        "be 'soldier' or 'vehicle'.")
