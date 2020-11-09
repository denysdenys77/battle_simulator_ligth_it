from typing import List


class GeometricHelper:

    def get_geometric_average(self, items: List[float]) -> float:
        """Returns geometric average of int items in list."""
        multiply: float = 1.0
        n = len(items)

        for i in items:
            multiply = multiply * i

        geometric_mean = multiply ** 1 / n
        return geometric_mean
