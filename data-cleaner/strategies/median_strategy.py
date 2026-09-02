import numpy as np

from .cleaning_strategy import CleaningStrategy


class MedianStrategy(CleaningStrategy):
    """
    Estrategia que reemplaza los valores faltantes con la mediana.
    """

    def clean(self, data):
        """
        Reemplaza cada valor None con la mediana de los valores válidos.
        """
        values = [
            value
            for value in data
            if value is not None
        ]

        if not values:
            return data

        median = float(np.median(values))

        return [
            median if value is None else value
            for value in data
        ]