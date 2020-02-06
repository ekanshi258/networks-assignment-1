import pandas as pd
import csv
import random

df = pd.read_csv('temp.csv')
matrix = df.iloc[: , :].values

for i in range(0,matrix.shape[0]):
    x = random.randint(-5,5)
    #df.replace(df['host'][i], df['host'][i]+x)
    matrix[i][1] = matrix[i][1] + x

df = pd.DataFrame(matrix)
df.to_csv('tempppppp.csv', index= False)