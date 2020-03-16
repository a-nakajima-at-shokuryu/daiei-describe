import utils
import os, csv 
from config import daiei 
from daiei_database import daiei_data

def kaikaktrn_sql(buscd, first, last):
  sql = '\n'.join([
    'select', 
    # 'top 10', 
    ','.join(['*']), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.KAIKAKTRN, 
    ), 
    'where %s' % (
      '\nand '.join([
        "KAI_SRYMD between '%s' and '%s'" % (
          first, 
          last, 
        ), 
        'KAI_SISCD = %s' % buscd[:2], 
        'KAI_BUSCD = %s' % buscd[2:4], 
      ]), 
    ), 
  ])
  return sql 

def kaikaktrn_dataframe(buscd, first, last): 
  sql = kaikaktrn_sql(buscd, first, last)
  
  print('部署コード: %s、処理日付: %s～%s の買い掛けトラン一覧を取得しています...' % (
    buscd, first, last, 
  ))
  df = daiei_data(sql)
  print('部署コード: %s、処理日付: %s～%s の買い掛けトラン一覧を取得しました (%d件)' % (
    buscd, first, last, len(df.index)
  ))
  return df 

def kaikaktrn_create_csv(buscd, first, last):
  df = kaikaktrn_dataframe(buscd, first, last)

  os.makedirs(utils.fullpath('csv'), exist_ok=True)
  filename = utils.fullpath('csv/kaikaktrn_%s_%s_%s.csv' % (
    buscd, first, last, 
  ))
  print('%s を作成しています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  return filename 

if __name__ == '__main__':
  buscd = daiei.DAIKYO_BUSCD
  count = 6

  for i in range(count): 
    first = utils.firstDay(months=-(i + 1))
    last = utils.lastDay(months=-(i + 1))
    
    kaikaktrn_create_csv(buscd, first, last)
    
    

