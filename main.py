import pymysql
from config import *
from pymysql.cursors import DictCursor

db = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=DictCursor
)

cursor = db.cursor()
a = cursor.execute('SELECT name FROM A')
rows = cursor.fetchall()
for b in rows:
    print(b)
print('cool')
print('success')
