from utils import fullpath 
from zipfile import ZipFile
import pandas as pd 
import io 

def namelistFromArchive(archive):
  with ZipFile(archive) as z: 
    # Pythonでzipファイル解凍後の文字化け解消（Qiita）
    # https://qiita.com/gsk3beta/items/aa0f4149334848285b69
    # for info in z.infolist():
    #   print(info.filename.encode('cp437').decode('cp932'))
    return [info.filename.encode('cp437').decode('cp932') for info in z.infolist()]

def stringIOFromArchive(archive, filename, encoding='utf-8'):
  namelist = namelistFromArchive(archive)
  if filename not in namelist: 
    raise Exception('%s is not exists in %s' % (filename, archive))

  with ZipFile(archive) as z:
    b = z.read(filename)
    s = b.decode(encoding) 
    return io.StringIO(s)

def readFileFromArchive(archive, filename): 
  with ZipFile(archive) as z: 
    return z.read(filename)
    
def readCsvFromArchive(archive, filename, encoding='utf-8', **kargs):
  stringIO = stringIOFromArchive(archive, filename, encoding)

  df = pd.read_csv(stringIO, low_memory=False, encoding=encoding, **kargs)

  return df 


if __name__ == '__main__':
  archive = fullpath('.zip/mas.zip')
  filename = 'hinsyu.csv'
  df = readCsvFromArchive(archive, filename)
  print(df.head())