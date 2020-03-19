from utils import fullpath
import pandas as pd 
import japanese_numbers as jn
import jaconv 
import csv

excel = fullpath('.zip/Dシステム_テーブル定義/02 テーブル一覧表/０１　マスタ関係/01　マスタ関係.xls')

def parse_tablelist_excel(excel):
  cols = [
    [  1, 'No'          , '№',] , 
    [  2, 'title'       , 'テーブル名称',] , 
  # [  3, ''            , '',] , 
    [  4, 'name'        , 'テーブルＩＤ',] , 
    [  5, 'prefix'      , '識別名',] , 
    [  6, 'repli'       , 'ﾚﾌﾟﾘ',] , 
    [  7, 'busho_kensu' , '部署件数',] , 
    [  8, 'busho_kensu_tan' , '部署件数（単位）',] , 
    [  9, 'chiku_kensu' , '地区件数',] , 
    [ 10, 'chiku_kensu_tan' , '地区件数（単位）',] , 
    [ 11, 'zensha_kensu', '全社件数',] , 
    [ 12, 'zensha_kensu_tan', '全社件数(単位）',] ,  
    [ 13, 'biko'        , '備考',] , 
  ]
  name_dict = {v[0]: v[1] for v in cols}

  df = pd.read_excel(excel, 
    skiprows=[
      *range(5), 
      *range(40, 50), 
      *range(65, 90)
    ], 
    usecols=[
      *name_dict.keys(), 
    ], 
    header=None, 
    names=[
      *name_dict.values(), 
    ], 
    ).fillna('')
  

  # 全角数字を半角数字に変換する関数
  def kansuji(s):
    s = jaconv.z2h(str(s), digit=True)
    arabic = jn.to_arabic(s)
    return 0 if len(arabic) == 0 else arabic[0].number

  for name in ['repli']:
    df[name] = df[name].map(lambda x: x == '〇')
  
  # 部署件数、地区件数、全社件数について、
  # それぞれの単位項目が'件'の場合は全角数字の半角数字化を行う
  for name in [
    'busho', 
    'chiku', 
    'zensha',     
  ]:
    d = {}
    d['kensu'] = df[f'{name}_kensu'].to_dict()
    d['tan']   = df[f'{name}_kensu_tan'].to_dict()
    
    def apply(index):
      kensu = d['kensu'][index]
      tan   = d['tan'  ][index]
      if tan == '件':
        kensu = kansuji(kensu)
      return kensu
    
    df[f'{name}_kensu'] = df.index.map(apply) 
  
  # 部署件数（単位）が'件'ではなくて部署件数が空文字ではない場合、
  # 部署件数の値を備考にコピーする
  d = {}
  for name in [
    'busho_kensu', 
    'busho_kensu_tan', 
    'biko', 
  ]: 
    d[name] = df[name].to_dict()

  def apply(index):
    busho_kensu = d['busho_kensu'][index]
    busho_kensu_tan = d['busho_kensu_tan'][index]
    biko = d['biko'][index]
  
    if not busho_kensu == '' and not busho_kensu_tan == '件':
      return busho_kensu 
    else: 
      return biko 
  
  df['biko'] = df.index.map(apply)
  
  return df

def daiei_mas_tablelist_create_csv():
  df = parse_tablelist_excel(excel)

  df.to_csv(fullpath('csv/daiei_mas_tablelist.csv'), 
            index=False, 
            quoting=csv.QUOTE_ALL)