from army.interface import ArmyABC
from squad.interface import SquadABC
from typing import List


class Army(ArmyABC):

    def __init__(self, name_number: int, squads: List[SquadABC]):
        super().__init__(name_number, squads)
