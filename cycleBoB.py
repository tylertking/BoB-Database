import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from cycler import cycler

df = pd.read_csv("Daily_Mission_BoBs.csv")

df 

i = 1326-436
print(df.iloc[i:i+21])
while i < (df.iloc[-1]['Mission Number']-436):
    newdf = df.iloc[i:i+21]
    bobCounter = (newdf.Ship.value_counts())
    print(df.iloc[i:i+21])
    print(bobCounter)
    i = i + 21