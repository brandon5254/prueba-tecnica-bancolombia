import pandas as pd

from src.load.export_excel import export_excel


def test_export_excel(tmp_path):
    output_file = tmp_path / "resumen_ventas.xlsx"

    sellers = pd.DataFrame({
        "Vendedor": ["Ana"],
        "Total_Venta": [1000]
    })

    months = pd.DataFrame({
        "Mes": [1],
        "Total_Venta": [1000]
    })

    export_excel(
        sellers,
        months,
        output_file
    )

    excel_file = pd.ExcelFile(output_file)

    assert output_file.exists()
    assert "Resumen_Ventas" in excel_file.sheet_names
    assert "Ventas_Mensuales" in excel_file.sheet_names