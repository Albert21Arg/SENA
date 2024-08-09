import mysql.connector

try:
    conexion = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='Rooney21',
                                       database='escuela_rita')
except Exception as err:
    print('Error conectando a la base de datos')
else:
    print('Conectado correctamente')

try:
    cur01 = conexion.cursor()
    insertar = "INSERT INTO estudiantes VALUES ('',1036667172, 'Albert', 'Nafer', 'Taborda', 'Gomez', '1996-06-15', 3004407014, 'O+', '2020-08-15')"
    cur01.execute(insertar)
    conexion.commit()
except Exception as err:
    print(f'Error al insertar datos en la tabla: {err}')
else:
    print('Datos insertados correctamente')

conexion.close()

