class MinCountOfSquadsException(Exception):
    pass


class SquadValidator:

    def validate(self, number_of_squads: int) -> int:
        """ Validate count of squads per game. """
        if 2 > number_of_squads:
            raise MinCountOfSquadsException
        return number_of_squads
