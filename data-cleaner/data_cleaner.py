from strategies.cleaning_strategy import CleaningStrategy


class DataCleaner:
    """
    Clase encargada de ejecutar una estrategia de limpieza de datos.
    """

    def __init__(self, strategy: CleaningStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CleaningStrategy):
        """
        Cambia la estrategia de limpieza en tiempo de ejecución.
        """
        self.strategy = strategy

    def clean(self, data):
        """
        Ejecuta la estrategia de limpieza configurada.
        """
        return self.strategy.clean(data)