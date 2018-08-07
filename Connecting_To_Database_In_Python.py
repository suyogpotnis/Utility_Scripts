import pyodbc
import numpy as np
import pandas as pd

con = pyodbc.connect('Trusted_Connection=yes',
                            driver = '{SQL Server}',
                            server = '(local)\SQLEXPRESS',
                            database = 'Test')
A =[]
cur = con.cursor()

# 1.] Read data into a Data Frame
df = pd.read_sql_query("select ID,IP,COUNTRY_CODE from Responses",con)
df

# 2.] Fetch Results using a cursor
querystring = "select ID,IP,COUNTRY_CODE from Responses"
cur.execute(querystring)
results = cur.fetchone()
while results:
    print (results)
    results = cur.fetchone()

con.close()
