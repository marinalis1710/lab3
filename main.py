import chart_studio
chart_studio.tools.set_credentials_file(username = 'mLisichenko', api_key='OALHe7ZRtB5XG1u7UQUK')
import plotly.graph_objects as go
import chart_studio.plotly as py
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

bar_name = []
quantity_bartenders = []
for data in cursor.fetchall():
    bar_name.append(data[0])
    quantity_bartenders.append(data[1])

bar = go.Bar(x=bar_name, y=quantity_bartenders)
py.plot([bar], auto_open=True, filename='oracle-data')

query2 = """
select bar_name,
count(human_name)*100/(
select count(*) from humanbar) as procent_of_total_bartenders from party
group by bar_name
"""
cursor.execute(query2)


bar_name2 = []
quantity_bartenders2 = []

for row in cursor.fetchall():
    bar_name2.append(row[0])
    quantity_bartenders2.append(row[1])
pie = go.Pie(labels=bar_name2, values=quantity_bartenders2)
py.plot([pie], auto_open=True)


query3 = """
select count(cocktail_name) as quantity_of_cocktails,
city_name
from party                     
group by city_name
order by quantity_of_cocktails desc
"""
cursor.execute(query3)

quantity = []
location = []

for data in cursor.fetchall():
    quantity.append(data[0])
    location.append(data[1])

scatter = go.Scatter(
    x=location,
    y=quantity
)

py.plot([scatter], auto_open=True)
