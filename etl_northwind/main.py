from etl_northwind.execute_sql import execute_sql_file
from etl_northwind.extract import extract_data
from etl_northwind.transform import transform_data
from etl_northwind.load_data import load_data

def run_etl():
    """Ejecuta el proceso ETL completo evitando duplicados."""
    try:
        print("📜 Iniciando proceso ETL...")
        execute_sql_file()
        data = extract_data()
        transformed_data = transform_data(data)
        load_data(transformed_data)
        print("ETL finalizado con éxito evitando duplicados.")
    except Exception as e:
        print(f"Error crítico en el proceso ETL: {e}")

if __name__ == "__main__":
    run_etl()