from abc import ABC, abstractmethod


class CleaningStrategy(ABC):
    """
    Clase base para las estrategias de limpieza de datos.
    """

    @abstractmethod
    def clean(self, data):
        """
        Limpia los datos usando una estrategia específica.
        """
        pass