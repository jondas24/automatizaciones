from flask import Flask, jsonify
import pandas as pd
import teradatasql
import warnings

app = Flask(__name__)

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

@app.route('/extraer_datos', methods=['GET'])
def api_extraer_datos():
    query = "SELECT * FROM MDB_EPS_IPS_COLOMBIA.vips_sede"
    archivo_excel = '/tmp/reporte_teradata.xlsx'  # Cambiar la ruta a algo más apropiado para el servidor
    archivo_generado = extraer_datos_teradata(query, archivo_excel)
    if archivo_generado:
        return jsonify({"message": "Datos exportados correctamente", "archivo": archivo_generado}), 200
    else:
        return jsonify({"message": "Error al extraer los datos"}), 500

if __name__ == '__main__':
    app.run(debug=True)
