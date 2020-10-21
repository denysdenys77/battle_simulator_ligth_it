from interfaces.army_interface import ArmyABC
from realisations.army import Army
from .squad_factory import SquadFactory


class ArmyFactory:

    @staticmethod
    def create(army_name_number,
               number_of_squads: int,
               number_of_units: int) -> ArmyABC:
        """Creating an army class instance with specified count of squads."""

        if 2 <= number_of_squads:
            squads_list = [SquadFactory.create(number_of_units)
                           for _ in range(number_of_squads)]
            return Army(name_number=army_name_number, squads=squads_list)
        raise Exception('Possible number of squads per army: 2 <= n.')
