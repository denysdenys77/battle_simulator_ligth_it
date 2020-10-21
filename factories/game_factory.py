from interfaces.game_interface import GameABC
from realisations.game import Game
from .army_factory import ArmyFactory
from .attack_factory import AttackFactory, RandomAttackFactory
from loguru import logger
from typing import Union


class GameFactory:

    @staticmethod
    def create(number_of_armies: int,
               number_of_squads: int,
               number_of_units: int,
               **kwargs) -> GameABC:
        """Returning Game class instance."""

        attack_strategy: Union[str, None] = kwargs.get('attack_strategy')
        if not attack_strategy:
            raise Exception('Missing required "attack_strategy" parameter.')

        if 2 <= number_of_armies:
            armies_list = [{'army': ArmyFactory.create(_,
                                                       number_of_squads,
                                                       number_of_units),
                            'attack': AttackFactory.create(attack_strategy)}
                           for _ in range(number_of_armies)]

            logger.info(armies_list)

            return Game(armies=armies_list)
        raise Exception('Possible count of armies in game: 2 <= n.')


class RandomArmyAttackStrategyGameFactory:

    @staticmethod
    def create(number_of_armies: int,
               number_of_squads: int,
               number_of_units: int,
               **kwargs) -> GameABC:
        """
        Returning Game class instance with
        per army random attack strategy.
        """

        if 2 <= number_of_armies:
            armies_list = [{'army': ArmyFactory.create(_,
                                                       number_of_squads,
                                                       number_of_units),
                            'attack': RandomAttackFactory.create()}
                           for _ in range(number_of_armies)]

            logger.info(armies_list)

            return Game(armies=armies_list)
        raise Exception('Possible count of armies in game: 2 <= n.')
