import os, sys 
from pathlib import Path 
from functools import reduce 
from datetime import date 
from dateutil.relativedelta import relativedelta 

def fullpath (path: str):
  return str(Path(path).resolve().absolute())

def pathJoin(*paths):
  return reduce(lambda a, b: Path(a) / Path(b), paths)

def firstDay(day = date.today(), months = 0):
  return (day + relativedelta(months=months)).replace(day=1)

def lastDay(day = date.today(), months = 0):
  return firstDay(day, months + 1) + relativedelta(days=-1)


root = fullpath(Path(__file__) / '../..')
if not root in sys.path: 
  sys.path.append(root)
