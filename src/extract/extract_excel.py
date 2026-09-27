import pandas as pd


COLUMNS = [
    "ID_Venta",
    "Fecha",
    "Producto",
    "Cantidad",
    "Precio_Unitario",
    "Total_Venta",
    "Vendedor"
]


def extract_excel(path):
    df = pd.read_excel(path)

    missing_columns = [
        column for column in COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Faltan columnas requeridas: {missing_columns}"
        )

    return df[COLUMNS]