import pyodbc 
import pandas as pd 

from config import daiei

dsn = ';'.join([
  'driver={SQL Server}', 
  'server=%s' % daiei.SERVER, 
  'uid=%s' % daiei.USERNAME, 
  'pwd=%s' % daiei.PASSWORD, 
])
def daiei_data(sql): 
  with pyodbc.connect(dsn) as conn:
    return pd.read_sql(sql, conn)

