import psycopg2
from psycopg2 import Error
from os import getenv
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Función para conectar a la base de datos
def conectar():
    try:
        conexion = psycopg2.connect(
            user=getenv('PGUSER'),
            password=getenv('PGPASSWORD'),
            host=getenv('PGHOST'),
            port=getenv('PGPORT', 5432),
            database=getenv('PGDATABASE')
        )
        return conexion
    except (Exception, Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Función para insertar un nuevo registro en la tabla LiquidacionesNomina
def insertar_registro(datos):
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("""INSERT INTO LiquidacionesNomina (
                                    ID_Empleado, 
                                    Fecha_Liquidacion, 
                                    Salario_Base_Mensual, 
                                    Tiempo_Laborado_Horas, 
                                    Tiempo_Festivo_Laborado_Dias, 
                                    Horas_Extra_Diurnas, 
                                    Horas_Extra_Nocturnas, 
                                    Horas_Extra_Festivas, 
                                    Tiempo_Incapacidades_Dias, 
                                    Tiempo_Licencias_No_Remuneradas_Dias
                                ) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                           datos)
            conexion.commit()
            print("Registro insertado correctamente.")
    except (Exception, Error) as error:
        print("Error al insertar registro:", error)
    finally:
        if conexion is not None:
            conexion.close()

# Función para eliminar un registro de la tabla LiquidacionesNomina
def eliminar_registro(id_liquidacion):
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM LiquidacionesNomina WHERE ID_Liquidacion = %s", (id_liquidacion,))
            conexion.commit()
            print("Registro eliminado correctamente.")
    except (Exception, Error) as error:
        print("Error al eliminar registro:", error)
    finally:
        if conexion is not None:
            conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Insertar un nuevo registro
    datos_nuevo_registro = (
        1,  # ID_Empleado
        '2024-05-16',  # Fecha_Liquidacion
        1600000,  # Salario_Base_Mensual
        160,  # Tiempo_Laborado_Horas
        0,  # Tiempo_Festivo_Laborado_Dias
        0,  # Horas_Extra_Diurnas
        0,  # Horas_Extra_Nocturnas
        0,  # Horas_Extra_Festivas
        0,  # Tiempo_Incapacidades_Dias
        0  # Tiempo_Licencias_No_Remuneradas_Dias
    )
    insertar_registro(datos_nuevo_registro)

    # Eliminar un registro por su ID
    eliminar_registro(1)
