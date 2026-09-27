import pandas as pd
from openpyxl.styles import Font


def format_sheet(sheet):
    # Encabezados en negrita
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    # Ajustar ancho de columnas
    sheet.column_dimensions["A"].width = 20
    sheet.column_dimensions["B"].width = 18

    # Formato moneda para Total_Venta
    for cell in sheet["B"][1:]:
        cell.number_format = '$#,##0.00'

    # Mantener encabezados visibles
    sheet.freeze_panes = "A2"


def export_excel(seller_summary, monthly_summary, path):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:

        seller_summary.to_excel(
            writer,
            sheet_name="Resumen_Ventas",
            index=False
        )

        monthly_summary.to_excel(
            writer,
            sheet_name="Ventas_Mensuales",
            index=False
        )

        format_sheet(writer.sheets["Resumen_Ventas"])
        format_sheet(writer.sheets["Ventas_Mensuales"])