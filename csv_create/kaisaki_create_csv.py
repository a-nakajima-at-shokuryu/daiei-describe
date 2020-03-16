import utils
import os, csv 
import pandas as pd 
from config import daiei 
from daiei_database import daiei_data 

def kaisaki_sql(buscd):
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join(['*']), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.AITSAKMST, 
    ), 
    'where %s' % (
      '\nand '.join([
        'AIT_AITCD between 3000 and 3999', 
        'AIT_BUSCD = %s' % buscd, 
      ]), 
    ), 
  ])
  return sql 

def kaisaki_dataframe(buscd):
  sql = kaisaki_sql(buscd)
  print('仕入先マスタを取得しています...')
  df = daiei_data(sql)
  print('仕入先マスタを取得しました (%d件)' % len(df.index))
  return df 

def kaisaki_create_csv(buscd):
  df = kaisaki_dataframe(buscd)

  os.makedirs(utils.fullpath('csv'), exist_ok=True)
  filename = utils.fullpath('csv/kaisaki_%s.csv' % buscd)
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  return filename 

if __name__ == '__main__':
  buscd = daiei.DAIKYO_BUSCD
  kaisaki_create_csv(buscd)