from interfaces.squard_interface import SquadABC
from abc import ABC
from typing import List


class ArmyABC(ABC):
    """Army interface."""

    def __init__(self, name_number: int, squads: List[SquadABC]):
        self.squads = squads
        self.name_number = name_number
