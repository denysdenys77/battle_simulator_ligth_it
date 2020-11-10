from army.validators import ArmyValidator
from attack.validators import TypeOfStrategyValidator
from game.factory import GameFactory
from game.factory import RandomArmyAttackStrategyGameFactory
from squad.validators import SquadValidator
from warring.validators import UnitValidator

"""
Possible number of armies in game: 2 <= n.
Possible number of squads per army: 2 <= n.
Possible number of units per squad: 5 <= n <= 10.
Possible choice of attack strategy /per army/: random|weakest|strongest.
"""


def main_game():
    army_validator = ArmyValidator()
    squad_validator = SquadValidator()
    unit_validator = UnitValidator()
    type_of_strategy_validator = TypeOfStrategyValidator()


    number_of_armies = army_validator.validate(
        int(input('Number of armies in game: ')))
    number_of_squads = squad_validator.validate(
        int(input('Number of squads per army: ')))
    number_of_units = unit_validator.validate(
        int(input('Number of units per squad: ')))
    attack_strategy = type_of_strategy_validator.validate(
        input('Attack strategy (random|weakest|strongest): '))

    game_factory = GameFactory()
    game = game_factory.create(number_of_armies=number_of_armies,
                               number_of_squads=number_of_squads,
                               number_of_units=number_of_units,
                               attack_strategy=attack_strategy)
    print(game.play())


def main_per_army_attack_strategy_game():
    random_army_attack_strategy_game_factory = RandomArmyAttackStrategyGameFactory()
    game = random_army_attack_strategy_game_factory.create(number_of_armies=5,
                                                           number_of_squads=2,
                                                           number_of_units=5,
                                                           attack_strategy='strongest')
    print(game.play())


if __name__ == '__main__':
    main_game()
    # main_per_army_attack_strategy_game()
