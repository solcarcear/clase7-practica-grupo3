from .cleaning_strategy import CleaningStrategy


class CustomValueStrategy(CleaningStrategy):
    """
    Estrategia que reemplaza los valores faltantes con un valor ingresado por el usuario
    """

    def __init__(self, replacement_value):
        """
        Inicializa la estrategia con el valor de reemplazo.
        """
        self.replacement_value = replacement_value

    def clean(self, data):
        """
        Reemplaza cada valor None con el valor personalizado ingresado.
        """
        return [
            self.replacement_value if value is None else value
            for value in data
        ]