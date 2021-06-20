import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from cycler import cycler

def graph_img(count, label):
    plt.pie(count, labels = label, startangle=90)
    plt.show() 

str3 = input("Daily or Specialist?: ")
if (str3 == "Daily"):
    df = pd.read_csv("Daily_Mission_BoBs.csv")
else: 
    df = pd.read_csv("Specialist_Mission_BoBs.csv")

df 
print(df.shape)
arr = []
totalArr = []
for index, columnData in df.iterrows():
    totalArr.append(columnData[2])
    if columnData[2] not in arr:
        arr.append(columnData[2])
print(arr)
print(len(arr))
arr2 = np.empty((len(arr), 2), dtype=object)
i=0
for item in arr:
    arr2[i, 0] = item
    arr2[i, 1] = totalArr.count(item)
    i+=1
sorted_array = arr2[np.argsort(arr2[:, 1])][::-1]
print(sorted_array)

str2 = input("Ship or Player?: ")

'''ts = df.groupby(['Player']).sum() #.plot(kind='pie', y=1)
tss = ts.iloc[:,1]
print(tss)
plt.pie(tss)
plt.show()'''


if (str2 == "Ship"):
    str = input("Enter Ship: ")
    test = df[df["Ship"] == str]
    print(test)
    bobCounter = (test.Player.value_counts())
    bobCounter = bobCounter.reset_index()
    bobCounter.columns = ["Player", "Count"] 
    print(bobCounter)
    graph_img(bobCounter["Count"], bobCounter["Player"])  
else:
    str = input("Enter Player: ")
    test = df[df["Player"] == str]
    print(test)
    bobCounter = (test.Ship.value_counts())
    bobCounter = bobCounter.reset_index()
    bobCounter.columns = ["Ship", "Count"]
    print(bobCounter)
    graph_img(bobCounter["Count"], bobCounter["Ship"])  
    
# bobCounter = bobCounter.reset_index()