import cx_Oracle
import csv

username = 'Marina'
password = 'xu40e5'
database = 'localhost/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

tables = ['Bar', 'Human', 'Cocktail', 'HumanCocktail', 'HumanBar', 'City']


for i in tables:
    try:
        with open(i + '.csv', 'w', newline='') as file:
            cursor.execute("SELECT * FROM " + i)
            database = cursor.fetchall()
            csv_writer=csv.writer(file, delimiter=',')
        for row in database:
            csv_writer.writerow(row)
    except:
        pass
cursor.close()
connection.close()
