import cx_Oracle

username = 'Marina'
password = 'xu40e5'

database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

query1 = """
select bar_name,
count(human_name) as total_humans from party
group by bar_name
order by total_humans desc
"""
cursor.execute(query1)
print("Bar_name - Quantity_of_bartenders")
for row in cursor:

    print(row)

query2 = """
select bar_name,
concat(round(count(human_name)*100/(
select count(*) from humanbar)),'%') as procent_of_total_bartenders from party
group by bar_name
"""
cursor.execute(query2)
print("\n Bar_name - %_quantity_of_bartenders")
for row in cursor:

    print(row)

query3 = """
select count(cocktail_name) as quantity_of_cocktails,
city_name
from party                     
group by city_name
order by quantity_of_cocktails desc
"""
cursor.execute(query3)
print("\nQuantity_of_cocktails - Bar_location")
for row in cursor:

    print(row)
