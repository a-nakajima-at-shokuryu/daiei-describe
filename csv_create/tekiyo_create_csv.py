import utils 
import os, csv  
import pandas as pd 
from config import daiei 
from daiei_database import daiei_data
def tekiyo_sql():
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join(['*']), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.TEKIYOMST, 
    ), 
  ])
  return sql

def tekiyo_dataframe():
  sql = tekiyo_sql()

  print('摘要マスタを取得しています...')
  df = daiei_data(sql)
  print('摘要マスタを取得しました (%d件)' % len(df.index))
  return df 

def tekiyo_create_csv():
  df = tekiyo_dataframe()

  os.makedirs(utils.fullpath('csv'), exist_ok=True)
  filename = utils.fullpath('csv/tekiyo.csv')
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  return filename 

if __name__ == '__main__':
  filename = utils.fullpath('csv/tekiyo.csv')
  df = pd.read_csv(filename, low_memory=False)
  pd.Series(df.columns, name='column'
    ).to_csv(utils.fullpath('csv/tekiyo_columns.csv'), 
      index=False, quoting=csv.QUOTE_ALL)