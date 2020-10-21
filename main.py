from factories.game_factory import GameFactory
from factories.game_factory import RandomArmyAttackStrategyGameFactory

"""
Possible number of armies in game: 2 <= n.
Possible number of squads per army: 2 <= n.
Possible number of units per squad: 5 <= n <= 10.
Possible choice of attack strategy /per army/: random|weakest|strongest.
"""


def main_game():
    game = GameFactory.create(number_of_armies=5,
                              number_of_squads=2,
                              number_of_units=5,
                              attack_strategy='strongest')
    print(game.play())


def main_per_army_attack_strategy_game():
    game = RandomArmyAttackStrategyGameFactory.create(number_of_armies=5,
                                                      number_of_squads=2,
                                                      number_of_units=5,
                                                      attack_strategy='strongest')
    print(game.play())


if __name__ == '__main__':
    # main_game()
    main_per_army_attack_strategy_game()