from interfaces.attack_interface import AttackABC
from realisations.attacks import (OnStrongestAttack,
                                  OnWeakestAttack,
                                  RandomAttack)
from typing import Type
from random import choice


class AttackFactory:

    @staticmethod
    def create(attack_strategy: str) -> Type[AttackABC]:
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

    @staticmethod
    def create() -> Type[AttackABC]:
        """Returning a Attack class of random type."""
        attack_strategies = [OnStrongestAttack, OnWeakestAttack, RandomAttack]
        return choice(attack_strategies)
