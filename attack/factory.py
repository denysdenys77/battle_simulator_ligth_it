from attack.interface import AttackABC
from attack.attacks_realizations import (OnStrongestAttack,
                                         OnWeakestAttack,
                                         RandomAttack)
from typing import Type
from random import choice


class AttackFactory:
    attack_strategies = {
        'strongest': OnStrongestAttack,
        'weakest': OnWeakestAttack,
        'random': RandomAttack,
    }

    def create(self, attack_strategy: str) -> Type[AttackABC]:
        """Returning a Attack class of specified type."""

        if attack_strategy in self.attack_strategies.keys():
            attack = self.attack_strategies[attack_strategy]
            return attack
        raise Exception("Possible choice of attack strategy "
                        "/per army/: random|weakest|strongest.")


class RandomAttackFactory:

    def create(self) -> Type[AttackABC]:
        """Returning a Attack class of random type."""
        attack_strategies = [OnStrongestAttack, OnWeakestAttack, RandomAttack]
        return choice(attack_strategies)
