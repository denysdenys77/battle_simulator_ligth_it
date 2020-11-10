from squad.interface import SquadABC
from warring.interface import WarringABC
from utils.geometric_average_helper import GeometricHelper
from typing import List


class Squad(SquadABC):
    geometric_helper = GeometricHelper()

    def __init__(self, units: List[WarringABC]) -> None:
        self._units = units

    def attack(self) -> float:
        """Returns attack success probability of a squad."""
        units_attack_success = [unit.attack() for unit in self._units]
        return self.geometric_helper.get_geometric_average(
            units_attack_success)

    def damage(self) -> float:
        """Returns amount of damage a squad can afflict."""
        return sum([unit.damage() for unit in self._units])

    def injure(self, total_damage: float) -> bool:
        """Reduces the number of units health points."""
        unit_damage = total_damage / len(self._units)
        for unit in self._units:
            self._injure_unit(unit, unit_damage)

        # check if squad was killed
        if not len(self._units):
            return True  # was killed
        return False

    def attack_status(self, success: bool) -> None:
        """Reduces the number of experience points for each unit."""
        for unit in self._units:
            unit.attack_status(success)

    def _injure_unit(self, unit: WarringABC, damage: float) -> None:
        """
        Dealing damage to a squad unit.
        Removing unit from units list if killed.
        """
        unit_was_killed = unit.injure(damage)
        if unit_was_killed:
            self._units.remove(unit)
