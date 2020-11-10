class MinCountOfUnitsException(Exception):
    pass


class UnitValidator:

    def validate(self, number_of_units: int) -> int:
        """ Validate count of units per squad. """
        if not 5 <= number_of_units <= 10:
            raise MinCountOfUnitsException
        return number_of_units
