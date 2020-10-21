from interfaces.army_interface import ArmyABC
from interfaces.squard_interface import SquadABC
from typing import List


class Army(ArmyABC):

    def __init__(self, name_number: int, squads: List[SquadABC]):
        super().__init__(name_number, squads)
