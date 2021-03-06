SERVER = '172.16.70.201'
DATABASE = 'DAIEI_DB'
USERNAME = 'sa'
PASSWORD = ''

# 2. 在庫一覧情報のネタとなるようなデータ 
GZAIKOZAN = 'GZAIKOZAN' 

# 3. 商品の過去の取引一覧のネタとなるようなデータ 
URIKAKTRN = 'URIKAKTRN' 
KAIKAKTRN = 'KAIKAKTRN' 

# その他マスタ関連テーブル 
HINZNSMST = 'HINZNSMST' #（商品マスタ） 
TEKIYOMST = 'TEKIYOMST' #（摘要マスタ） 
KURADRMST = 'KURADRMST' #（冷蔵庫マスタ） 
AITSAKMST = 'AITSAKMST' #（相手先マスタ売上・仕入） 

KAISAKI_CONDITION = 'AIT_AITCD between 3000 and 3999'
URISAKI_CONDITION = 'AIT_AITCD >= 4000'
DAIKYO_BUSCD = '0281'
DAIKYO_CONDITION = 'AIT_BUSCD = %s' % (DAIKYO_BUSCD)

# SELECT top 10 * FROM AITSAKMST where AIT_BUSCD='0281' and AIT_AITCD between 4000 and 4999 order by AIT_AITCD
