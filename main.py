import sqlite3

database='database.sqlite'

conn = sqlite3.connect(database)
print("opened data successfully!!")

import pandas as pd
cursor=conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(tables)