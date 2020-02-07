import pandas as pd
import csv
import random
from datetime import datetime, timedelta

df = pd.read_csv('hostcount.csv')
matrix = df.iloc[: , :].values

t = matrix[0][0]
dt = datetime.strptime(t, "%d/%m/%Y %H:%M:%S")
for i in range(0,matrix.shape[0]):
    x = random.randint(-5,5)
    #df.replace(df['host'][i], df['host'][i]+x)
    dt = dt + timedelta(minutes=33, seconds=x)  
    str = dt.strftime('%d/%m/%Y %H:%M:%S')
    #matrix[i][0] = datetime.strptime(dt, "%d/%m/%Y %H:%M:%S")
    matrix[i][0] = str
    t = matrix[i][0]
df = pd.DataFrame(matrix)
df.to_csv('temp.csv', index= False)