import cx_Oracle
import csv

username = 'Marina'
password = 'xu40e5'
database = 'localhost/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

filename = "Cocktails.csv"

with open(filename, newline='') as file:
    reader = csv.DictReader(file)
    tables = ['HumanCocktail', 'HumanBar', 'Bar', 'Human', 'Cocktail', 'City']
    for i in tables:
        cursor.execute("DELETE FROM " + i)
    cocktail_list = []
    human_list = []
    city_list = []


    for row in reader:
        try:
            cocktail_name = row['Cocktail Name']
            human_name = row['Bartender']
            bar_name = row['Bar/Company']
            city_name = row['City']

            try:
                if cocktail_name not in cocktail_list:
                    cocktail_list.append(cocktail_name)
                    query = """INSERT INTO Cocktail(cocktail_name) VALUES (:cocktail_name)"""
                    cursor.execute(query, cocktail_name=cocktail_name)
            except:
                pass
            try:
                if human_name not in human_list:
                    human_list.append(human_name)
                    query = """INSERT INTO Human(human_name)  VALUES (:human_name)"""
                    cursor.execute(query, human_name=human_name)
            except:
                pass

            try:
                if city_name not in city_list:
                    city_list.append(city_name)
                    query = """INSERT INTO City(city_name) VALUES (:city_name)"""
                    cursor.execute(query, city_name=city_name)
            except:
                pass

            try:
                query = """INSERT INTO Bar(bar_name, city_name) VALUES (:bar_name, :city_name)"""
                cursor.execute(query, bar_name=bar_name, city_name=city_name)
            except:
                pass

            try:
                query = """INSERT INTO HumanBar(human_name, bar_name) VALUES (:human_name, :bar_name)"""
                cursor.execute(query, human_name=human_name, bar_name=bar_name)
            except:
                pass

            try:
                query = """INSERT INTO HumanCocktail(human_name, cocktail_name) VALUES (:human_name, :cocktail_name)"""
                cursor.execute(query, human_name=human_name, cocktail_name=cocktail_name)
            except:
                pass
        except:
            pass

    connection.commit()
    cursor.close()
    connection.close()
