import numpy as np

from .cleaning_strategy import CleaningStrategy


class MeanStrategy(CleaningStrategy):
    """
    Estrategia que reemplaza los valores faltantes con la media.
    """

    def clean(self, data):
        """
        Reemplaza cada valor None con la media de los valores válidos.
        """
        values = [
            value
            for value in data
            if value is not None
        ]

        if not values:
            return data

        mean = float(np.mean(values))

        return [
            mean if value is None else value
            for value in data
        ]