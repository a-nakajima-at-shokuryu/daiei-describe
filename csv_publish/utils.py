from pathlib import Path 
from functools import reduce 
import sys, re

def fullpath(*paths):
  join = reduce(lambda a, b: Path(a) / Path(b), paths)
  absolute = Path(join).resolve().absolute()
  return absolute

root = str(fullpath(__file__, '../..'))

if not root in sys.path: 
  sys.path.append(root)

# アルファベット->数値 
def alpha_to_num(s): 
  a = ord('a')
  z = ord('z')
  base = z - a + 1
  num = 0
  for i, c in enumerate(reversed(s)):
    o = ord(c) - a + 1
    num += o * pow(base, i)

  return num 

def a1_to_r1c1(s): 
  match = re.findall(r'^([a-z]+)([0-9]+)$', s)

  if (len(match) == 0):
    raise Exception('"%s" はA1形式ではありません' % s)

  col, row = match[0]  

  row = int(row)
  col = alpha_to_num(col)

  return (row, col)
