import pandas as pd
import numpy as np

file = "D:\\HoonsCode\\Beginning\\crawling\\table_goobne.csv"

df = pd.read_csv(file, sep=",")
df.head()