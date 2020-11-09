from army.interface import ArmyABC
from army.army import Army
from squad.factory import SquadFactory


class ArmyFactory:
    squad_factory = SquadFactory()

    def create(self,
               army_name_number,
               number_of_squads: int,
               number_of_units: int) -> ArmyABC:
        """Creating an army class instance with specified count of squads."""

        if 2 <= number_of_squads:
            squads_list = [self.squad_factory.create(number_of_units)
                           for _ in range(number_of_squads)]
            return Army(name_number=army_name_number, squads=squads_list)
        raise Exception('Possible number of squads per army: 2 <= n.')
