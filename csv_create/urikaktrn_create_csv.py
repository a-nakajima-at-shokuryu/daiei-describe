import utils 
from config import daiei 
from datetime import date 
from dateutil.relativedelta import relativedelta 

from daiei_database import daiei_data 
import os, csv 

def urikaktrn_sql(buscd, first, last=None):
  if last is None: 
    last = first
  sql = '\n'.join([
    'select', 
    # 'top 10',
    ','.join([
      '*', 
    ]),  
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.URIKAKTRN, 
    ), 
    'where %s' % (
      '\nand '.join([
        "URI_SRYMD between '%s' and '%s'" % (first, last), 
        "URI_SISCD = '%s'" % (buscd[0:2]), 
        "URI_BUSCD = '%s'" % (buscd[2:4]), 
      ]), 
    ), 
  ])
  print(sql)
  return sql 

def urikaktrn_dataframe(buscd, first, last = None):
  if last is None: 
    last = first
  sql = urikaktrn_sql(buscd, first, last)
  print('部署コード:%s、処理日: %s～%s の売掛トランを取得しています...' % (
    buscd, first, last, 
  ))
  df = daiei_data(sql)
  print('部署コード:%s、処理日: %s～%s の売掛トランを取得しました (%d件)' % (
    buscd, first, last, len(df.index)
  ))
  return df

def urikaktrn_create_csv(bscd, first, last = None):
  if last is None: 
    last = first
  df = urikaktrn_dataframe(buscd, first, last)

  os.makedirs(utils.fullpath('csv'), exist_ok=True)
  filename = utils.fullpath('csv/urikaktrn_%s_%s_%s.csv' % (
    buscd, 
    first, 
    last, 
  ))
  print('%s を作成しましています...' % filename)
  df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)

if __name__ == '__main__':
  buscd = daiei.DAIKYO_BUSCD
  baseDay = date.today()
  count = 6

  for i in range(count):
    day = baseDay + relativedelta(months=-(i + 1))
    first = utils.firstDay(day)
    last = utils.lastDay(day)
    urikaktrn_create_csv(buscd, first, last)