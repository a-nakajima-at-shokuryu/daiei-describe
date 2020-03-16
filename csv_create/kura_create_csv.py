import utils 
import os, csv 
import pandas as pd 
from config import daiei 
from daiei_database import daiei_data 

def kura_sql():
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join(['*']), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.KURADRMST, 
    ), 
  ])
  return sql 

def kura_dataframe():
  sql = kura_sql()

  print('冷蔵庫マスタを取得しています...')
  df = daiei_data(sql)
  print('冷蔵庫マスタを取得しました (%d件)', len(df.index))
  return df 

def kura_create_csv():
  df = kura_dataframe()

  filename = utils.fullpath('csv/kura.csv')
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  return filename

if __name__ == '__main__': 
  pass
