import pandas as pd
import teradatasql
#import win32com.client as win32
#import os
import warnings

# Ignorar advertencias específicas
warnings.filterwarnings("ignore", message="pandas only support SQLAlchemy")

def extraer_datos_teradata(query, archivo_excel):
    try:
        # Conexión a Teradata
        conn = teradatasql.connect('{"host":"teradata2.suranet.com","user":"johnhoas","password":"3113454135Jonda/"}')
        print("Conexión a Teradata exitosa.")
        
        # Ejecutar la consulta SQL
        df = pd.read_sql_query(query, conn)
        print("Consulta ejecutada correctamente.")
        
        # Exportar a Excel
        df.to_excel(archivo_excel, index=False, engine='openpyxl')
        print(f"Datos exportados a Excel: {archivo_excel}")
        return archivo_excel
    except Exception as e:
        print(f"Error en la extracción de datos: {e}")
        return None

query = "SELECT * FROM MDB_EPS_IPS_COLOMBIA.vips_sede"
archivo_excel = r"C:\Users\johnhoas\OneDrive - Seguros Suramericana, S.A\Documentos\JDANIEL\1- Gestion Informacion\7-epidemiologico\reporte_teradata.xlsx"
archivo_generado = extraer_datos_teradata(query, archivo_excel)