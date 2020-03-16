import utils 
from config import daiei 
from daiei_database import daiei_data 
import os, csv
import pandas as pd 

def hinsyu_sql(): 
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join(['*']), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.HINZNSMST, 
    ), 
    
  ])
  return sql 

def hinsyu_dataframe(): 
  sql = hinsyu_sql()
  
  print('品種マスタを取得しています...')
  df = daiei_data(sql)
  print('品種マスタを取得しました (%d件)' % len(df.index))
  return df 

def hinsyu_create_csv():
  df = hinsyu_dataframe()

  os.makedirs(utils.fullpath('csv'), exist_ok=True)
  filename = utils.fullpath('csv/hinsyu.csv')
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  return filename 

if __name__ == '__main__':
  hinsyu_create_csv()