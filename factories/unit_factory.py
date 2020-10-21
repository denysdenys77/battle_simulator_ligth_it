from interfaces.warring_interface import WarringABC
from realisations.soldier import Soldier
from realisations.vehicle import Vehicle


class UnitFactory:

    @staticmethod
    def create(unit_type: str) -> WarringABC:
        """Returning unit instance of specified unit type"""

        units = {
            'soldier': Soldier(),
            'vehicle': Vehicle(Soldier)
        }

        if unit_type in units.keys():
            return units[unit_type]
        raise Exception("'unit_type' field value should "
                        "be 'soldier' or 'vehicle'.")
