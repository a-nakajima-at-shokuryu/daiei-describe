from config import daiei
from datetime import date 
import numpy as np

def urisaki_0281_sql():
  sql = '\n'.join([
    'select', 
    # 'TOP 10', 
    ','.join([
      '*', 
      ]), 
    'from %s.dbo.%s' % (
      daiei.DATABASE, 
      daiei.AITSAKMST, 
      ), 
    'where %s and %s' % (
      daiei.DAIKYO_CONDITION, 
      daiei.URISAKI_CONDITION, 
      ), 
  ])
  return sql

def urikaktrn_sql(srymd):

  srymd = list(np.array(srymd).flatten())
  srymd = (srymd + [srymd[0]] * 2)[:2]
  
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
    'where %s' % ' and '.join([
      'URI_SISCD=%s' % (daiei.DAIKYO_BUSCD[0:2]), 
      'URI_BUSCD=%s' % (daiei.DAIKYO_BUSCD[2:4]), 
      "URI_SRYMD between '%s' and '%s'" % (
        srymd[0], 
        srymd[1], 
      ), 
    ])
  ])

  return sql

