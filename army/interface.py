from squad.interface import SquadABC
from abc import ABC
from typing import List


class ArmyABC(ABC):
    """Army interface."""

    def __init__(self,
                 name_number: int,
                 squads: List[SquadABC]) -> None:
        self.squads = squads
        self.name_number = name_number

    def attack(self, defending_army) -> bool:
        pass
