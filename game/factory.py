from game.interface import GameABC
from game.game import Game
from army.factory import ArmyFactory
from attack.factory import AttackFactory, RandomAttackFactory
from loguru import logger
from typing import Union


class GameFactory:
    army_factory = ArmyFactory()
    attack_factory = AttackFactory()

    def create(self,
               number_of_armies: int,
               number_of_squads: int,
               number_of_units: int,
               **kwargs) -> GameABC:
        """Returning Game class instance."""

        attack_strategy: Union[str, None] = kwargs.get('attack_strategy')
        if not attack_strategy:
            raise Exception('Missing required "attack_strategy" parameter.')

        if 2 <= number_of_armies:
            armies_list = [{'army': self.army_factory.create(_,
                                                             number_of_squads,
                                                             number_of_units),
                            'attack': self.attack_factory.create(attack_strategy)}
                           for _ in range(number_of_armies)]

            logger.info(armies_list)

            return Game(armies=armies_list)
        raise Exception('Possible count of armies in game: 2 <= n.')


class RandomArmyAttackStrategyGameFactory:
    army_factory = ArmyFactory()
    random_attack_factory = RandomAttackFactory()

    def create(self,
               number_of_armies: int,
               number_of_squads: int,
               number_of_units: int,
               **kwargs) -> GameABC:
        """
        Returning Game class instance with
        per army random attack strategy.
        """

        if 2 <= number_of_armies:
            armies_list = [{'army': self.army_factory.create(_,
                                                             number_of_squads,
                                                             number_of_units),
                            'attack': self.random_attack_factory.create()}
                           for _ in range(number_of_armies)]

            logger.info(armies_list)

            return Game(armies=armies_list)
        raise Exception('Possible count of armies in game: 2 <= n.')
