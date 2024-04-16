import mysql.connector
try:
    conexion=mysql.connector.connect(host='localhost',
                                    user = 'root',
                                    passwd = 'Rooney21',
                                    database = 'escuela_rita')
    cur01=conexion.cursor()
    cur01.execute('show tables')
    for f in cur01:
        print(f)
except Exception as err :
    print('Error conectando a la base')
else :
    print('Conectado')
conexion.close()
