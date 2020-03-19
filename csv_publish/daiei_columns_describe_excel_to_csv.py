from utils import fullpath, a1_to_r1c1 
import re 
from daiei_columnlist_create_csv import daiei_columnlist_create_csv

dirname = fullpath('.zip/Dシステム_テーブル定義/03 テーブル項目定義書/01 マスタ関係')

basenames = [
  'M01 AITSAKMST 取引相手先ﾏｽﾀ.xls', 
  'M02 HINSHUMST 独自品名ﾏｽﾀ.xls', 
  'M03 HFUZUIMST 品種付随情報ﾏｽﾀ.xls', 
  'M04 TEKIYOMST 摘要マスタ.xls', 
  'M05 KURADRMST 冷蔵庫住所マスタ.xls', 
  'M06 AGROUPMST 取引先ｸﾞﾙｰﾌﾟﾏｽﾀ.XLS', 
  'M07 FRKOZAMST 支払振込口座ﾏｽﾀ.XLS', 
  'M08 HGROUPMST 品種ｸﾞﾙｰﾌﾟﾏｽﾀ.XLS', 
  'M09 SKANRIMST ｼｽﾃﾑ管理ﾏｽﾀ.xls', 
  'M10 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
  'M11 SAIBANMST 採番マスタ.xls', 
  'M12 KIGYO1MST 企業情報ﾏｽﾀ(名称編).XLS', 
  'M13 KIGYO2MST 企業情報ﾏｽﾀ(数値編).XLS', 
  'M14 KADOBIMST 稼動日数マスタ.XLS', 
  'M15 MSAIBNMST 携帯端末採番マスタ.XLS', 
  'M16 ZENGINMST 全銀マスタ.XLS', 
  'M17 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
  'M18 HASSOUMST その他発送先ﾏｽﾀ.xls', 
  'M19 SIWAKETBL 売買自動仕訳ﾃｰﾌﾞﾙ.xls', 
  'M20 SIWINFTBL 仕訳情報ﾃｰﾌﾞﾙ.xls', 
  'M21 SIWAKEPTN 仕訳ﾊﾟﾀｰﾝﾌｧｲﾙ.XLS', 
  'M22 NYUSIHPTN 仕訳ﾊﾟﾀｰﾝF.XLS', 
  'M23 LOCATEMST ﾛｹｰｼｮﾝﾏｽﾀ.XLS', 
  'M24 HACCHUMST 発注先ﾏｽﾀ.XLS', 
  'M25 HAISOLMST ルートﾏｽﾀ.XLS', 
  'M26 BATKNRMST バッチ管理マスタ.XLS', 
  'M27 SVRCNTMST 地区別ｻｰﾊﾞｰ接続管理ﾏｽﾀ.XLS', 
  'M28 HINZNSMST 全社品種ﾏｽﾀ.xls', 
  'M29 YUUBINMST 郵便番号マスタ.XLS', 
  'M30 BAIKAYMST  売価マスター.XLS', 
  'M31 KINESYMST 杵屋商品マスタ.XLS', 
  'M32 UMEKNRMST 梅の花管理マスタ.XLS', 
  'M33 HINCHGMST 店舗品種変換マスタ.xls', 
  'M34 COMENTMST 物流ｺﾒﾝﾄﾏｽﾀ.xls', 
  'M35 ONLINEMST ｵﾝﾗｲﾝ設定ﾏｽﾀ.xls', 
  'M36 Cタッチﾞ商品マスタ.xls', 
  'M37 Cタッチ相手先マスタ.xls', 
  'M38 Cタッチ価格マスタ.xls', 
  'M39 多目的変換管理マスタ.xls', 
  'M40 パソコン管理マスタ.xls', 
  'M41 荷割倉指定ﾏｽﾀ.xls', 
  'M42 ハガキ住所録マスタ.xls', 
  'M43 FB提出先ﾏｽﾀ.xls', 
  'M44 運送先ﾏｽﾀ.xls', 
  'M45 ﾘｽﾄﾜｰｸｽ連携ｵﾌﾟｼｮﾝﾏｽﾀ.xls', 
  'M46 ﾘｽﾄﾜｰｸｽ連携ｸﾞﾙｰﾌﾟﾏｽﾀ.xls', 
  'M47 EDI相手先マスタ.XLS', 
  'M48 EDI品種マスタ.XLS', 
  'M49 プログラム管理ﾏｽﾀ.xls', 
  'M50 備品管理マスタ.xls', 
  'M51 データ削除管理ﾏｽﾀ.xls', 
  'M52 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
  'M53 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
  'M54 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
  'M55 CODNAMMST 業務コードマスタ.xls', 
  'M56 HINBNRMST 商品分類マスタ.xls', 
  'M57 品種別分類マスタ.xls', 
  'Mxx HOLIDAYMST 休日マスタ.xlsx', 
]

def daiei_columns_describe_excel_to_csv():
  
  dirname = fullpath('.zip/Dシステム_テーブル定義/03 テーブル項目定義書')

  # dirname = fullpath(dirname, '01 マスタ関係')
  # dirname = fullpath(dirname, '02 ﾄﾗﾝｻﾞｸｼｮﾝ関係')
  dirname = fullpath(dirname, '03 残高・通常ﾃﾞｰﾀ関係')
  # dirname = fullpath(dirname, '04 一時ﾃｰﾌﾞﾙ関係')
  # dirname = fullpath(dirname, '05 TXT関係')
  # dirname = fullpath(dirname, '06 NAVI')

  filename = fullpath(dirname, 'T01 KAIKAKTRN 仕入買掛発生ﾃﾞｰﾀ.xls')
  filename = fullpath(dirname, 'T04 SRENRATRN 内部売買連絡ﾃﾞｰﾀ.xls')
  filename = fullpath(dirname, 'T05 URIKAKTRN 売上売掛発生ﾃﾞｰﾀ.xls')
  filename = fullpath(dirname, 'Z01 GZAIKOZAN 在庫残高ﾏｽﾀ.xls')

  # exit()#####################################
  
  name_cell='ah2'
  page_cell='ck2'
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
  nrows = 50
  
  # ============================================
 
  daiei_columnlist_create_csv(filename, 
    name_cell=name_cell, 
    page_cell=page_cell, 
    cols=cols,
    nrows=nrows, 
    )

# #######################################
  # # 'M02 HINSHUMST 独自品名ﾏｽﾀ.xls', 
  # filename = dirname / basenames[1]
  # name_cell='af2'
  # page_cell='ci2'
  # cols = [
  #   ['b' , 'no'    , 'No ', ], 
  #   ['c' , 'title' , '項目名称', ], 
  #   ['w' , 'prefix', 'プレフィックス', ], 
  #   ['ab', 'name'  , '項目識別子', ], 
  #   ['ai', 'type'  , '項目タイプ', ], 
  #   ['aq', 'size'  , '桁数', ], 
  #   ['ax', 'iskey' , 'キー項目', ], 
  #   ['bf', 'biko'  , '備考', ], 
  # ]
  # ============================================
  # 'M05 KURADRMST 冷蔵庫住所マスタ.xls', 
  # cols = [
  #   ['b' , 'no'    , 'No ', ], 
  #   ['e' , 'title' , '項目名称', ], 
  #   ['y' , 'prefix', 'プレフィックス', ], 
  #   ['ad', 'name'  , '項目識別子', ], 
  #   ['ak', 'type'  , '項目タイプ', ], 
  #   ['as', 'size'  , '桁数', ], 
  #   ['ax', 'iskey' , 'キー項目', ], 
  #   ['bi', 'biko'  , '備考', ], # <<<
  # ]
  # ============================================
  # 'M21 SIWAKEPTN 仕訳ﾊﾟﾀｰﾝﾌｧｲﾙ.XLS', 
  # nrows=100
  # ============================================
  # M33 HINCHGMST 店舗品種変換マスタ.xls
  # name_cell='e2'
  # page_cell='q2'
  # cols = [
  #   ['b' , 'no'    , 'No ', ], 
  #   ['c' , 'title' , '項目名称', ], 
  #   ['d' , 'prefix', 'プレフィックス', ], 
  #   ['e', 'name'  , '項目識別子', ], 
  #   ['f', 'type'  , '項目タイプ', ], 
  #   ['g', 'size'  , '桁数', ], 
  #   ['h', 'iskey' , 'キー項目', ], 
  #   ['m', 'biko'  , '備考', ], 
  # ]
  # ============================================
  # M36 Cタッチﾞ商品マスタ
  # ...
  # M46 ﾘｽﾄﾜｰｸｽ連携ｸﾞﾙｰﾌﾟﾏｽﾀ
  # M49 プログラム管理ﾏｽﾀ
  # name_cell='af2'
  # page_cell='ci2'
  # cols = [
  #   ['b' , 'no'    , 'No ', ], 
  #   ['c' , 'title' , '項目名称', ], 
  #   ['w' , 'prefix', 'プレフィックス', ], 
  #   ['ab', 'name'  , '項目識別子', ], 
  #   ['ai', 'type'  , '項目タイプ', ], 
  #   ['aq', 'size'  , '桁数', ], 
  #   ['av', 'iskey' , 'キー項目', ], 
  #   ['bf', 'biko'  , '備考', ], 
  # ]