import pandas as pd

from src.extract.extract_excel import extract_excel


def test_extract_excel(tmp_path):
    file_path = tmp_path / "ventas.xlsx"

    data = pd.DataFrame({
        "ID_Venta": [1],
        "Fecha": ["2023-01-15"],
        "Producto": ["Producto A"],
        "Cantidad": [2],
        "Precio_Unitario": [100],
        "Total_Venta": [200],
        "Vendedor": ["Ana"]
    })

    data.to_excel(file_path, index=False)

    result = extract_excel(file_path)

    assert len(result) == 1
    assert "Total_Venta" in result.columns