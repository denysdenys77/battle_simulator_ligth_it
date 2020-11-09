from warring.interface import WarringABC
from warring.soldier import Soldier
from warring.vehicle import Vehicle


class UnitFactory:

    def create(self, unit_type: str) -> WarringABC:
        """Returning unit instance of specified unit type"""

        units = {
            'soldier': Soldier(),
            'vehicle': Vehicle(Soldier)
        }

        if unit_type in units.keys():
            return units[unit_type]
        raise Exception("'unit_type' field value should "
                        "be 'soldier' or 'vehicle'.")
