from game.interface import GameABC
from army.interface import ArmyABC
from attack.interface import AttackABC
from typing import Tuple, List, Dict, Any, Type

from loguru import logger


class Game(GameABC):

    def __init__(self, armies: List[Dict[str, Any]]) -> None:
        self.armies = armies

    def play(self) -> int:
        """
        Main play method.
        Returns winner army.
        """

        # set indexes for the loop
        # attacking_army_index, defending_army_index = 0, 1
        attacking_army_index = 0

        # iterating through list of armies
        # attacking and removing killed army
        while len(self.armies) != 1:

            # getting correct indexes
            attacking_army_index, defending_army_index = \
                self._get_armies_indexes_new(attacking_army_index)

            # getting armies by indexes
            attacking_army, defending_army = \
                self._get_fighting_armies(attacking_army_index,
                                          defending_army_index)

            # getting attack
            # attack_class: Type[AttackABC] = \
            #     self.armies[attacking_army_index]['attack']
            # attack = attack_class()

            # attacking and getting "army_was_killed" status
            # army_was_killed = attack.attack(attacking_army, defending_army)
            army_was_killed = attacking_army.attack(defending_army)
            if army_was_killed:
                self.armies.pop(defending_army_index)

            # upgrading indexes
            attacking_army_index += 1

        winner = self.armies[0]['army']
        return winner.name_number

    def _get_fighting_armies(self,
                             attacking_army_index: int,
                             defending_army_index: int) -> Tuple[ArmyABC,
                                                                 ArmyABC]:
        """Method to get attacking and defending armies for iteration."""

        attacking_army = self.armies[attacking_army_index]['army']
        defending_army = self.armies[defending_army_index]['army']

        return attacking_army, defending_army

    def _get_armies_indexes_new(self,
                                attacking_army_index: int) -> Tuple[int, int]:
        """
        Returning attacking and defending
        armies updated indexes.
        """

        if attacking_army_index > len(self.armies) - 1:
            attacking_army_index = 0
            defending_army_index = attacking_army_index + 1
        elif attacking_army_index == len(self.armies) - 1:
            defending_army_index = 0
        else:
            defending_army_index = attacking_army_index + 1

        # logging
        logger_info_data = (
            attacking_army_index,
            defending_army_index,
            len(self.armies) - 1
        )
        logger.info(f'{logger_info_data}'
                    f' // len={len(self.armies)}')
        logger.info(f'==================')

        return attacking_army_index, defending_army_index
