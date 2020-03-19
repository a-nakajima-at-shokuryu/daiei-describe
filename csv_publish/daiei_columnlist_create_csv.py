from utils import fullpath, alpha_to_num, a1_to_r1c1
import pandas as pd
import csv, re 
import xlrd 

filename = fullpath('.zip/Dシステム_テーブル定義/03 テーブル項目定義書/01 マスタ関係/M01 AITSAKMST 取引相手先ﾏｽﾀ.xls')

cols = [
  ['b' , 'no'    , 'No ', ], 
  ['e' , 'title' , '項目名称', ], 
  ['y' , 'prefix', 'プレフィックス', ], 
  ['ad', 'name'  , '項目識別子', ], 
  ['ak', 'type'  , '項目タイプ', ], 
  ['as', 'size'  , '桁数', ], 
  ['ax', 'iskey' , 'キー項目', ], 
  ['bh', 'biko'  , '備考', ], 
]


name_cell = 'ah2'
page_cell = 'ck2'

nrows = 50
page_size = 58

def a1_to_rowcol(s):
  r1c1 = a1_to_r1c1(s)
  row, col = [x - 1 for x in r1c1]
  return row, col 

def read_cell_value(sheet, a1):
  row, col = a1_to_rowcol(a1)
  return sheet.cell_value(row, col)

def daiei_columnlist_read_name_and_pagesize(filename, 
  name_cell=name_cell, 
  page_cell=page_cell):
  wb = xlrd.open_workbook(filename)
  sheets = wb.sheets()
  sheet = sheets[0]

  tablename = read_cell_value(sheet, name_cell)

  s = read_cell_value(sheet, page_cell)
  match = re.findall(r'1/([0-9]+)', s)
  if len(match) == 0:
    raise Exception('ページ番号記述が不正です（"%s"）' % s)
  
  return tablename, int(match[0])
  

def daiei_columnlist_dataframe(excel, page, 
  cols=cols, 
  nrows=nrows):

  usecols = [alpha_to_num(v[0]) - 1 for v in cols]
  names = [v[1] for v in cols]
  

  offset = page_size * page

  skiprows = [
    *range(0, offset + 3), 
  ]

  df = pd.read_excel(excel, 
        skiprows=skiprows, 
        usecols=usecols, 
        names=names, 
        nrows=nrows, 
        ).fillna('')
  
  def isnum(x):
    return re.search(r'^[0-9]+(?:\.0)?$', str(x)) is not None

  def isempty(s):
    return not len(str.strip(s)) == 0
  
  df = df[df['no'].apply(isnum)]
  
  df = df[df['name'].apply(isempty)]

  return df 

def daiei_columnlist_create_csv(filename, 
    name_cell=name_cell, 
    page_cell=page_cell, 
    cols=cols, 
    nrows=nrows):
  
  match = re.findall(r'([A-Z][0-9|x]+)[ ]+(?:([^ ]+)[ ]+)?([^ ]+).(?:XLS|xls)[xX]?$', 
    str(filename))
  if len(match) == 0: 
    raise Exception('ファイル名が不正です "%s"' % filename.name)
  
  match = match[0]
  
  tablename, pagesize = daiei_columnlist_read_name_and_pagesize(filename, 
    name_cell, 
    page_cell)
  all = pd.DataFrame() 

  tablename = tablename.lower()

  for i in range(pagesize):
    print('%s の %dページ目を読み込んでいます...' % (filename.name, i + 1))
    df = daiei_columnlist_dataframe(filename, i, 
      cols, 
      nrows)

    all = pd.concat([all, df], ignore_index=True)
    print('%s の %dページ目を読み込みました' % (filename.name, i + 1))
  
  mxx, tn, ja = match 
  if tn == '':
    tn = tablename.upper()
  prefix = '%s_%s_%s' % (mxx, tn, ja)
  
  filename = fullpath('csv/_describe_[%s]_(%s).csv' % (prefix, tablename))

  print('%s を作成しています...' % filename)
  all.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
  print('%s を作成しました' % filename)
  print(all)
