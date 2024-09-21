import pyodbc

connection_string = (
    r"DRIVER={Microsoft Access Driver( *.mdb, *.accdb)};"
    r"DBQ=Location of the file(File name = Products Database)"
)

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

cursor.execute('select * from products')
for row in cursor.fetchall():
    print(row)