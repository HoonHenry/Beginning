# coding: utf-8
from dateitme import datetime
from datetime import datetime
import pandas as pd
df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
df.columns
df.columns = ["month", "passengers"]
df['ones'] = 1
df.head()
datetime.strptime("1949-05", "%Y-%m")
df['dt'] = df.apply(lambda row: dateetime.strptime(row['month'], "%y-%m") axis=1)
df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%y-%m") axis=1)
df['dt'] = df.apply(lambda row: dateetime.strptime(row['month'], "%y-%m"), axis=1)
df['dt'] = df.apply(lambda row: dateetime.strptime(row['month'], "%Y-%m") axis=1)
df['dt'] = df.apply(lambda row: dateetime.strptime(row['month'], "Yy-%m"), axis=1)
df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
df.info()
get_ipython().run_line_magic('save', 'apply')
get_ipython().run_line_magic('save', 'applyPractice.py')
help(save)
help()
get_ipython().run_line_magic('save', 'applyFuncPractice 1-21')
