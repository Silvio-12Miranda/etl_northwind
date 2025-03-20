import polars as pl
import numpy as np

def transform_data(dataframes):
    """Transforma los datos para PostgreSQL evitando duplicados."""
    try:
        print("[Paso 3] Transformando datos...")
        dataframes["orders"] = dataframes["orders"].with_columns(
            pl.col("OrderDate").str.to_datetime("%Y-%m-%d %H:%M:%S", strict=False).dt.date()
        )
        dataframes["order_details"] = dataframes["order_details"].with_columns(
            (pl.col("UnitPrice") * pl.col("Quantity")).alias("Total_Venta")
        )
        dim_tiempo = (
            dataframes["orders"]
            .select(["OrderDate"])
            .unique()
            .with_columns([
                pl.col("OrderDate").alias("Fecha"),
                pl.col("OrderDate").dt.day().alias("Dia"),
                pl.col("OrderDate").dt.month().alias("Mes"),
                pl.col("OrderDate").dt.year().alias("Año")
            ])
        )
        dim_clientes = dataframes["customers"].rename({"CompanyName": "Nombre_Cliente"}).unique()
        dim_productos = dataframes["products"].unique()
        dim_categorias = dataframes["categories"].unique()
        dim_empleados = dataframes["employees"].unique()
        fact_ventas = (
            dataframes["order_details"]
            .join(dataframes["orders"], on="OrderID")
            .select(["OrderID", "CustomerID", "EmployeeID", "OrderDate", "ProductID", "Quantity", "UnitPrice", "Total_Venta"])
            .unique()
        )
        transformed_data = {
            "D_TIEMPO": dim_tiempo,
            "D_CLIENTES": dim_clientes,
            "D_PRODUCTOS": dim_productos,
            "D_CATEGORIAS": dim_categorias,
            "D_EMPLEADOS": dim_empleados,
            "VENTAS": fact_ventas
        }
        for name, df in transformed_data.items():
            print(f"[Paso 3] Muestra de datos transformados de {name}:\n{df.head(5)}")
        print("[Paso 3] Transformación de datos completada evitando duplicados.")
        return transformed_data
    except Exception as e:
        print(f"Error en [Paso 3] Transformación de datos: {e}")
        return {}