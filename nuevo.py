import pymysql

conn = pymysql.connect(
        host='junction.proxy.rlwy.net',
        user='Editor_Stephany',
        password='123456',
        database='ProyectoParcial',
        port=25596,
        connect_timeout=10
    )
print("Conexión establecida:", conn)

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta de prueba
cursor.execute("SHOW TABLES;")

# Obtener y mostrar los resultados
tables = cursor.fetchall()
print("Tablas en la base de datos 'votos':", tables)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()