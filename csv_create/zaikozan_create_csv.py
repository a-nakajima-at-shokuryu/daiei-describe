import utils 
import os, csv 
import pandas as pd 
from config import daiei 
from daiei_database import daiei_data 

def zaikozan_sql(buscd):
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join(['*']), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.GZAIKOZAN, 
    ), 
    'where %s' % (
      '\nand '.join([
        'GZA_SISCD = %s' % buscd[:2], 
        'GZA_BUSCD = %s' % buscd[2:4], 
      ]), 
    ), 
  ])
  return sql 

def zaikozan_dataframe(buscd):
  sql = zaikozan_sql(buscd)

  print('部署コード: %s の在庫一覧を取得しています...' % buscd)
  df = daiei_data(sql)
  print('部署コード: %s の在庫一覧を取得しました (%d件)' % (buscd, len(df.index)))
  return df 

def zaikozan_create_csv(buscd):
  buscd = daiei.DAIKYO_BUSCD
  df = zaikozan_dataframe(buscd)

  os.makedirs(utils.fullpath('csv'), exist_ok=True)
  filename = utils.fullpath('csv/zaikozan_%s.csv' % buscd)
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  return filename

if __name__ == '__main__':
  pass