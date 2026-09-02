# Limpieza de datos con Strategy Pattern

Pequeña aplicación en Python que permite aplicar diferentes estrategias para manejar valores faltantes dentro de un conjunto de datos.

El proyecto fue realizado como parte de la materia **Fundamentos de Ingeniería de Software para Científicos de Datos**.

## ¿Qué hace la aplicación?

Partimos de una lista que contiene algunos valores faltantes:

```python
[10, 20, None, 40, None, 60]
```

Desde consola se puede elegir entre tres formas de procesarlos:

1. Eliminar los valores faltantes.
2. Reemplazarlos con la media.
3. Reemplazarlos con la mediana.

Para los cálculos de media y mediana utilizamos **NumPy**.

## ¿Por qué usamos Strategy?

Elegimos el patrón **Strategy** porque tenemos distintas formas de realizar una misma tarea: limpiar los datos.

Cada estrategia tiene su propia implementación y puede cambiarse sin modificar la lógica principal de la aplicación. También permite agregar nuevas formas de limpieza más adelante sin afectar las estrategias existentes.

## Estructura

```text
data_cleaner/
│
├── main.py
├── data-cleaner.py
├── requirements.txt
│
└── strategies/
    ├── __init__.py
    ├── cleaning_strategy.py
    ├── drop_missing_strategy.py
    ├── mean_strategy.py
    └── median_strategy.py
```

## Instalación

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

Al ejecutar el programa se mostrará un menú para seleccionar la estrategia de limpieza que se desea utilizar.

## Integrantes

Enrique Arce
EDGAR POLANCO OCHOA
CARLOS ALBERTO ARCE ORTUÑO
Silvia Huarachi Jaldin
TELASSIM GINNOLA TELASSIM GINNOLA