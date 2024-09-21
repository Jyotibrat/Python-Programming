import pyodbc

connection_string = (
    r"DRIVER={Microsoft Access Driver( *.mdb, *.accdb)};"
    r"DBQ=Location of the file(file name = Data_Base_Employee);"
)

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

select_query = """
SELECT COUNT(*)
FROM Employees
WHERE designation = ?
"""

cursor.execute(select_query, ('Manager',))

count = cursor.fetchone()[0]

print(f"Number of managers: {count}")

cursor.close()
connection.close()