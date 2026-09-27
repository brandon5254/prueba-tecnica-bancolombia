import pandas as pd


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