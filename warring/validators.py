class MinCountOfUnitsException(Exception):
    pass


class UnitValidator:

    def validate(self, number_of_units: int) -> int:
        """ Validate count of units per squad. """
        if 2 >= number_of_units:
            raise MinCountOfUnitsException
        return number_of_units
