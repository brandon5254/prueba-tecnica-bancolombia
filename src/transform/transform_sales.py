import pandas as pd


def transform_sales(df, year):
    df = df.copy()

    df["Total_Venta"] = df["Total_Venta"].fillna(
        df["Cantidad"] * df["Precio_Unitario"]
    )

    df["Fecha"] = pd.to_datetime(
        df["Fecha"],
        errors="coerce"
    )

    df = df[df["Fecha"].dt.year == year].copy()

    df["Mes"] = df["Fecha"].dt.month

    return df


def sales_by_seller(df):
    return (
        df.groupby("Vendedor", as_index=False)["Total_Venta"]
        .sum()
        .sort_values("Total_Venta", ascending=False)
    )


def sales_by_month(df):
    return (
        df.groupby("Mes", as_index=False)["Total_Venta"]
        .sum()
        .sort_values("Mes")
    )