from utils import fullpath
import pandas as pd 
import csv

excel = fullpath('.zip/Dシステム_テーブル定義/02 テーブル一覧表/０２　トランザクション関係/トランザクション関係（整形）.xlsx')
sheets = [
  ['zan', '残高及び通常データ'], 
  ['tran', 'トランザクション'], 
]

def daiei_tran_tablelist_dataframe(excel, sheet):
  cols = [
    ['no'          , 'No', ], 
    ['title'       , 'テーブル名称', ], 
    ['removed'     , '消去', ], 
    ['name'        , 'テーブルＩＤ', ], 
    ['prefix'      , '識別名', ], 
    ['repli'       , 'レプリ', ], 
    ['busho_kensu' , '部署件数', ], 
    ['chiku_kensu' , '地区件数', ], 
    ['zensha_kensu', '全社件数',], 
    ['biko'        , '備考', ], 
  ]
  col2title = { v[0]: v[1] for v in cols }
  title2col = { v[1]: v[0] for v in cols }

  df = pd.read_excel(excel, sheet_name=sheet, 
        skiprows = [
          *range(0, 4), 
        ], 
        header=None, 
        names=[
          *col2title.keys(), 
        ], 
        ).fillna('')

  for name in ['removed', 'repli']:
    df[name] = df[name].map(lambda x: x == '〇')
  
  return df 

def daiei_tran_tablelist_create_csv(excel, sheets):
  for en, ja in sheets:
    filename = fullpath('csv/daiei_tran_tablelist_%s.csv' % en)
    daiei_tran_tablelist_dataframe(excel, ja)
    print('%sを作成しています...' % (filename))
    df = daiei_tran_tablelist_dataframe(excel, ja)
    df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)
    print('%sを作成しました' % (filename))

if __name__ == '__main__':
  daiei_tran_tablelist_create_csv(excel, sheets)
  

  
