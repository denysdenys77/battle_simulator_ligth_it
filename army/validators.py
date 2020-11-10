class MinCountOfArmiesException(Exception):
    pass


class ArmyValidator:

    def validate(self, number_of_armies: int) -> int:
        """ Validate count of armies per game. """
        if 2 >= number_of_armies:
            raise MinCountOfArmiesException
        return number_of_armies
