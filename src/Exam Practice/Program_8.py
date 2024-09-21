import pyodbc

def connect_to_db():
    connStr = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=E:/Downloads/Student_Database.accdb;"
    )
    return pyodbc.connect(connStr)

connection = connect_to_db()
cursor = connection.cursor()

insert_query = """
INSERT INTO Student (student_register_number, student_name, student_school) 
VALUES (?, ?, ?)
"""
values_to_insert = ('23BAI10963', 'Bindupautra Jyotibrat', 'Carmel School')
cursor.execute(insert_query, values_to_insert)

connection.commit()

update_query = """
UPDATE Student 
SET student_name = ? 
WHERE student_register_number = ?
"""
values_to_update = ('Akshit Joshi', '23BAI10963')
cursor.execute(update_query, values_to_update)

connection.commit()

delete_row = input("Enter the student register number whose row you want to delete: ")
delete_query = """
DELETE FROM Student 
WHERE student_register_number = ?
"""
cursor.execute(delete_query, (delete_row,))

connection.commit()

cursor.close()
connection.close()

print("Operations completed successfully.")