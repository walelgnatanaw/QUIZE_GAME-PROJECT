import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=LAPTOP-L4LBIQ7T;'
                      'Database=w;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
def DB1():
    PersonID = int(input("ID"))
    firstName=input('fname')
    LastName = input("Lname")
    Category=input('category')
    Question=input('question')
    Answer = input('answer')
    score=input('score')
    cursor.execute('select FirstName from A')
    cursor.execute("INSERT INTO [A] (PersonID, firstName,LastName,Category,Question,Answer,score) VALUES(?,?,?,?,?,?,?)",
                   (PersonID,firstName,LastName,Category,Question,Answer,score))
    conn.commit()
    cursor.close()
    conn.close()

DB1()
