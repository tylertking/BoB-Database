import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from cycler import cycler

df = pd.read_csv("Daily_Mission_BoBs.csv")

df 

df.Ship.value_counts()
for i in range(500, 2000, 100):
    start = df[df['Mission Number']==i].index.values
    end = df[df['Mission Number']==i+99].index.values
    print(start[0])
    print(end[0])
    print(df[df['Mission Number']==i])
    print(df[df['Mission Number']==i+99])
    newdf = df.iloc[start[0]:end[0]]
    bobCounter = (newdf.Ship.value_counts())
    print(bobCounter)