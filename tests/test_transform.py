import pandas as pd

from src.transform.transform_sales import (
    transform_sales,
    sales_by_seller,
    sales_by_month
)


def test_transform_sales():
    data = pd.DataFrame({
        "ID_Venta": [1, 2],
        "Fecha": ["2023-01-15", "2022-05-10"],
        "Producto": ["Producto A", "Producto B"],
        "Cantidad": [2, 3],
        "Precio_Unitario": [100, 50],
        "Total_Venta": [None, 150],
        "Vendedor": ["Ana", "Carlos"]
    })

    result = transform_sales(data, 2023)

    assert len(result) == 1
    assert result.iloc[0]["Total_Venta"] == 200
    assert result.iloc[0]["Mes"] == 1


def test_sales_summaries():
    data = pd.DataFrame({
        "Vendedor": ["Ana", "Ana", "Carlos"],
        "Mes": [1, 2, 1],
        "Total_Venta": [100, 200, 300]
    })

    sellers = sales_by_seller(data)
    months = sales_by_month(data)

    assert sellers["Total_Venta"].sum() == 600
    assert months["Total_Venta"].sum() == 600