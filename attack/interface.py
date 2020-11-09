from abc import ABC, abstractmethod
from army.interface import ArmyABC


class AttackABC(ABC):
    """Attack interface."""

    @abstractmethod
    def attack(self, attacking_army: ArmyABC, defending_army: ArmyABC) -> bool:
        pass
