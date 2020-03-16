import utils 
from config import daiei 
from daiei_database import daiei_data 
import os, csv

def urisaki_sql(buscd):
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join([
      '*', 
    ]), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.AITSAKMST, 
    ), 
    'where %s' % (
      ' and '.join([
          'AIT_AITCD >= 4000', 
          '1=1' if buscd is None else 'AIT_BUSCD = %s' % buscd, 
      ]), 
    ), 
  ])
  return sql 
def urisaki_dataframe(buscd):
  sql = urisaki_sql(buscd)
  print(sql)

  print('部署コード:%s の売り先一覧を取得しています...' % buscd)
  df = daiei_data(sql)
  print('部署コード:%s の売り先一覧を取得しました (%d件)' % (
    buscd, 
    len(df.index), 
  ))

  return df 
  
def urisaki_create_csv(buscd = None):
  
  df = urisaki_dataframe(buscd)

  dirname = 'csv'
  os.makedirs(dirname, exist_ok=True)
  filename = utils.fullpath(
    'csv/urisaki.csv' if buscd is None else 
    'csv/urisaki_%s.csv' % buscd)
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)

if __name__ == '__main__':
  urisaki_create_csv()
  # urisaki_create_csv(daiei.DAIKYO_BUSCD)