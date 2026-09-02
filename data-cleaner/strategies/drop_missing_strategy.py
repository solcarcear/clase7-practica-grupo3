from .cleaning_strategy import CleaningStrategy


class DropMissingStrategy(CleaningStrategy):
    """
    Estrategia que elimina los valores faltantes.
    """

    def clean(self, data):
        """
        Elimina todos los valores None de la lista.
        """
        return [
            value
            for value in data
            if value is not None
        ]