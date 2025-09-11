import os
import pandas as pd
import pyodbc

def guardar_csv(rows, filename="noticias_tacna_incidentes.csv"):
    df = pd.DataFrame(rows)
    if not df.empty:
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"✅ CSV guardado: {filename}")
    return df

def cargar_sql(df):
    if df.empty:
        print("⚠️ No hay datos para cargar en SQL")
        return

    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            f"SERVER={os.getenv('AZURE_SQL_SERVER')};"
            f"DATABASE={os.getenv('AZURE_SQL_DATABASE')};"
            f"UID={os.getenv('AZURE_SQL_USER')};"
            f"PWD={os.getenv('AZURE_SQL_PASSWORD')};"
            "Encrypt=yes;TrustServerCertificate=no;"
        )
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO IncidentesTacna (medio, url, ubicacion, lat, lon, snippet)
                VALUES (?, ?, ?, ?, ?, ?)
            """, row["medio"], row["url"], row["ubicacion"], row["lat"], row["lon"], row["snippet"])

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Datos cargados en Azure SQL")

    except Exception as e:
        print("❌ Error al cargar en Azure SQL:", e)
