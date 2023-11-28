import mysql.connector

# Conecta a la base de datos
connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1105768400Juan_",
        database="classicmodels",
    )

# Crea un cursor para la conexión
cursor = connection.cursor()

# Ejecuta la instrucción SQL para listar las tablas
cursor.execute("SHOW TABLES")

# Recupera los resultados de la consulta
tables = cursor.fetchall()

# Itera sobre los resultados para obtener el nombre de cada tabla
for table in tables:

    # Crea un nuevo cursor para la tabla actual
    new_cursor = connection.cursor()

    # Ejecuta la instrucción SQL para obtener los datos de la tabla
    new_cursor.execute("SELECT * FROM " + table[0])

    # Recupera los resultados de la consulta
    results = new_cursor.fetchall()

    # Imprime los resultados de la consulta
    print("Tabla: " + table[0])
    for row in results:
        print(row)

# Cierra el cursor y la conexión
cursor.close()
connection.close()