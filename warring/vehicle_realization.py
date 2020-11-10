from warring.interface import WarringABC
from utils.geometric_average_helper import GeometricHelper
from random import choice
from typing import List


class Vehicle(WarringABC):
    geometric_helper = GeometricHelper()

    def __init__(self, soldiers: List[WarringABC]) -> None:
        self._operators: list = soldiers
        self._health: float = 100.0 + 100.0 * len(self._operators)

    def attack(self) -> float:
        """Returns attack success probability of a vehicle."""
        operators_attack_success = [float(operator.attack())
                                    for operator in self._operators]
        return (0.5 * (1 + self._health / 100) *
                self.geometric_helper.get_geometric_average(
                    operators_attack_success))

    def damage(self) -> float:
        """Returns amount of damage a vehicle can afflict."""
        operators_experience = sum([operator.experience
                                    for operator in self._operators])
        return 0.1 + operators_experience / 100

    def injure(self, total_damage: float) -> bool:
        """Reduces the number of health points."""

        # calculating damage for each unit
        vehicle_damage = total_damage / 100 * 60
        sed_operator_damage = total_damage / 100 * 20
        rest_operators_damage = total_damage / 100 * 10

        # attacking operators and vehicle
        self._attack_operators(sed_operator_damage, rest_operators_damage)
        self._health -= vehicle_damage

        # check if vehicle was killed
        if self._health <= 0:
            return True  # is destroyed
        return False

    def attack_status(self, success: bool) -> None:
        """Reduces the number of experience points for each operator."""
        for operator in self._operators:
            operator.attack_status(success)

    def _attack_operators(self, sed_operator_damage: float,
                          rest_operators_damage: float) -> None:
        """Dealing damage to a vehicle operators."""
        # damaging random operator
        sed_operator = choice(self._operators)
        self._injure_operator(sed_operator, sed_operator_damage)

        # damaging rest operators
        for operator in self._operators:
            if operator != sed_operator:
                self._injure_operator(operator, rest_operators_damage)

    def _injure_operator(self, operator: WarringABC, damage: float) -> None:
        """
        Dealing damage to a concrete vehicle operator.
        Removing operator from operators list if killed.
        """
        operator_was_killed = operator.injure(damage)
        if operator_was_killed:
            self._operators.remove(operator)
