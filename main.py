import yaml
import pandas as pd

from src.extract.extract_excel import extract_excel
from src.transform.transform_sales import (
    transform_sales,
    sales_by_seller,
    sales_by_month
)
from src.load.export_excel import export_excel


def main():

    with open(
        "config/config.yaml",
        "r",
        encoding="utf-8"
    ) as file:
        config = yaml.safe_load(file)

    input_path = config["paths"]["input"]
    output_path = config["paths"]["output"]
    year = config["processing"]["year"]

    print("Iniciando proceso ETL...")

    # Extract
    df = extract_excel(input_path)

    # Transform
    df = transform_sales(df, year)

    seller_summary = sales_by_seller(df)
    monthly_summary = sales_by_month(df)

    # Load
    export_excel(
        seller_summary,
        monthly_summary,
        output_path
    )

    print("Proceso finalizado correctamente.")
    print(f"Archivo generado: {output_path}")


if __name__ == "__main__":
    main()