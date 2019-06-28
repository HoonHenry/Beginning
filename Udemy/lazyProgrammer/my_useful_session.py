# coding: utf-8

import pandas as pd
df = pd.read_csv("international-airline-passengers.csv, engine="python", skipfooter=3)
df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
df.columns
df.columns = ["month", "passengers"]
df.columns
df['passengers']
df.passengers
df['ones'] = 1
df.head()
