from attack.interface import AttackABC
from attack.attacks import (OnStrongestAttack,
                            OnWeakestAttack,
                            RandomAttack)
from typing import Type
from random import choice


class AttackFactory:

    def create(self, attack_strategy: str) -> Type[AttackABC]:
        """Returning a Attack class of specified type."""
        attack_strategies = {
            'strongest': OnStrongestAttack,
            'weakest': OnWeakestAttack,
            'random': RandomAttack,
        }

        if attack_strategy in attack_strategies.keys():
            attack = attack_strategies[attack_strategy]
            return attack
        raise Exception("Possible choice of attack strategy "
                        "/per army/: random|weakest|strongest.")


class RandomAttackFactory:

    def create(self) -> Type[AttackABC]:
        """Returning a Attack class of random type."""
        attack_strategies = [OnStrongestAttack, OnWeakestAttack, RandomAttack]
        return choice(attack_strategies)
