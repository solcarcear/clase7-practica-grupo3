import numpy as np

from .cleaning_strategy import CleaningStrategy
from .cleaning_strategy import MissingValueStrategy
from typing import List, Optional

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
class DropNullsStrategy(MissingValueStrategy):
    """Estrategia 1: Elimina filas que contienen valores nulos (Listwise Deletion)."""
    def clean(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        df_copy = df.copy()
        if columns:
            return df_copy.dropna(subset=columns)
        return df_copy.dropna()

class ModeImputationStrategy(MissingValueStrategy):
    """Estrategia 4: Imputa nulos usando la moda (Ideal para atributos categóricos o cualitativos)."""
    def clean(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        df_copy = df.copy()
        target_cols = columns if columns else df_copy.columns
        
        for col in target_cols:
            if not df_copy[col].mode().empty:
                mode_val = df_copy[col].mode()[0]
                df_copy[col] = df_copy[col].fillna(mode_val)
        return df_copy