import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='sati5108',
    host='localhost',
    port='13306'
)
cursor = cnx.cursor()
cursor.execute('select * from ksjpt_db.users')

for id, name in cursor:
    print(f'{id}: {name}')
