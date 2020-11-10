from army.validators import ArmyValidator
from game.factory import RandomArmyAttackStrategyGameFactory
from squad.validators import SquadValidator
from warring.validators import UnitValidator


def main_game():

    army_validator = ArmyValidator()
    squad_validator = SquadValidator()
    unit_validator = UnitValidator()

    number_of_armies = army_validator.validate(
        int(input('Number of armies in game: ')))
    number_of_squads = squad_validator.validate(
        int(input('Number of squads per army: ')))
    number_of_units = unit_validator.validate(
        int(input('Number of units per squad: ')))

    random_army_attack_strategy_game_factory = \
        RandomArmyAttackStrategyGameFactory()
    game = random_army_attack_strategy_game_factory.create(
        number_of_armies=number_of_armies,
        number_of_squads=number_of_squads,
        number_of_units=number_of_units,)

    print(game.play())


if __name__ == '__main__':
    main_game()
