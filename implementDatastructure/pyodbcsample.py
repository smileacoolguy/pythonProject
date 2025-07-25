"""import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=SQLSRV01;DATABASE=DATABASE;UID=USER;PWD=PASSWORD')
cursor = cnxn.cursor()

cursor.execute("SELECT WORK_ORDER.TYPE,WORK_ORDER.STATUS, WORK_ORDER.BASE_ID, WORK_ORDER.LOT_ID FROM WORK_ORDER")
for row in cursor.fetchall():
    print(row)

pyodbc.connect("").cursor().execute("").fetchall()
"""
dict={"names":["abc","def","xyz"],"locations":["mumbai","pune","blore"]}
import pandas as pd

df = pd.DataFrame.from_dict(dict)
print(df)

json_string = '{"col1": {"0": "a", "1": "c"}, "col2": {"0": "b", "1": "d"}}'
df_from_string = pd.read_json(json_string)
print("DataFrame from JSON string:"+json_string)
print(df_from_string)

data_dict = {
    "Name": ["Alice", "Bob"],
    "Age": [30, 24]
}
df_from_dict = pd.DataFrame(data_dict)
print("\nDataFrame from Python dictionary:")
print(df_from_dict)