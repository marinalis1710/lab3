import cx_Oracle
import csv

username = 'Marina'
password = 'xu40e5'
database = 'localhost/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

tables = ['Bar', 'Human', 'Cocktail', 'HumanCocktail', 'HumanBar', 'City']

try:
    for i in tables:
        with open(i + '.csv', 'w', newline='') as file:
            cursor.execute("SELECT * FROM " + i)
            database = cursor.fetchall()
            csv_writer=csv.writer(file, delimiter=',')
        for row in database:
            csv_writer.writerow(row)
cursor.close()
connection.close()
