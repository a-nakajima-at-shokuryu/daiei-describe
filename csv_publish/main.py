from utils import fullpath
from datetime import date 
from dateutil.parser import parse 
from dateutil.relativedelta import relativedelta
import pandas as pd 

buscd = '0281'
ymd = parse('2020-02-22')

ymd1 = ymd + relativedelta(day=1)
ymd2 = ymd + relativedelta(day=31)

filename = fullpath('csv/urikaktrn_{}_{}_{}.csv'.format(
  buscd, 
  ymd1.strftime('%Y-%m-%d'), 
  ymd2.strftime('%Y-%m-%d'), 
))

if filename.exists() == False:
  raise Exception('%s が見つかりません' % filename)

df = pd.read_csv(filename)