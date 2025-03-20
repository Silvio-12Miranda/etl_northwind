import psycopg2
from sqlalchemy import create_engine
import polars as pl
from etl_northwind.config import DATABASE_CONFIG

def get_postgres_engine():
    """Crea un motor de conexión a PostgreSQL."""
    return create_engine(
        f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['dbname']}"
    )

def load_data(transformed_data):
    """Carga los datos en PostgreSQL evitando duplicados."""
    try:
        print("[Paso 4] Cargando datos en PostgreSQL evitando duplicados...")
        engine = get_postgres_engine()
        conn = engine.raw_connection()
        cursor = conn.cursor()

        for table, df in transformed_data.items():
            print(f"Procesando {df.shape[0]} registros para {table}...")

            if df.shape[0] > 0:
                # Obtener registros ya existentes en la base
                existing_df = pl.read_database(f"SELECT * FROM {table}", engine)

                if not existing_df.is_empty():
                    # Filtrar registros nuevos con `anti_join`
                    common_cols = [col for col in df.columns if col in existing_df.columns]
                    df = df.join(existing_df, on=common_cols, how="anti")

                if df.shape[0] > 0:
                    df.to_pandas().to_sql(table, engine, if_exists="append", index=False)
                    print(f"{table} cargado correctamente con {df.shape[0]} nuevos registros.")
                else:
                    print(f"{table} ya tenía todos los registros, no se insertó nada nuevo.")
        
        conn.commit()
        cursor.close()
        conn.close()
        print("[Paso 4] Datos cargados exitosamente en PostgreSQL evitando duplicados.")

    except Exception as e:
        print(f"Error en [Paso 4] Carga de datos en PostgreSQL: {e}")