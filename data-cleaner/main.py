from data_cleaner import DataCleaner
from strategies.drop_missing_strategy import DropMissingStrategy
from strategies.mean_strategy import MeanStrategy
from strategies.median_strategy import MedianStrategy


def show_menu():
    """
    Muestra las estrategias de limpieza disponibles.
    """
    print("\n=== LIMPIEZA DE DATOS ===")
    print("1. Eliminar valores faltantes")
    print("2. Reemplazar con la media")
    print("3. Reemplazar con la mediana")


def main():
    """
    Ejecuta el flujo principal de la aplicación.
    """
    data = [10, 20, None, 40, None, 60]

    print("Datos originales:")
    print(data)

    show_menu()

    option = input(
        "\nSeleccione una estrategia: "
    ).strip()

    if option == "1":
        strategy = DropMissingStrategy()

    elif option == "2":
        strategy = MeanStrategy()

    elif option == "3":
        strategy = MedianStrategy()

    else:
        print("Opción no válida.")
        return

    cleaner = DataCleaner(strategy)

    result = cleaner.clean(data)

    print("\nDatos procesados:")
    print(result)


if __name__ == "__main__":
    main()