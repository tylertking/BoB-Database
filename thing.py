import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from cycler import cycler

pd.set_option("display.max_rows", None, "display.max_columns", None)

def graph_img(sizes, labels, str1, str2):
    fig1, ax1 = plt.subplots(figsize=(5, 5))
    fig1.subplots_adjust(0.3, 0, 1, 1)

    theme = plt.get_cmap('tab20b')
    themeTwo = plt.get_cmap('tab20c')
    arr = []
    for i in range(20):
        arr.append(theme(1. * i / 20))
    for i in range(21, 40):
        arr.append(themeTwo(1. * (i-20) / 20))
    ax1.set_prop_cycle("color", arr) 

    _, _ = ax1.pie(sizes, startangle=90, radius=1800)

    ax1.axis('equal')


    total = sum(sizes)
    plt.legend(
        loc='upper left',
        labels=['%s, %1.1f%%' % (
            l, (float(s) / total) * 100)
                for l, s in zip(labels, sizes)],
        prop={'size': 11},
        bbox_to_anchor=(0.0, 1),
        bbox_transform=fig1.transFigure
    )

    ax1.set_title(str1 + ': ' + str2, y=.98, pad=-14)
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

if (str2 == "Ship"):
    str = input("Enter Ship: ")
    test = df[df["Ship"] == str]
    print(test)
    bobCounter = (test.Player.value_counts())
    bobCounter = bobCounter.reset_index()
    bobCounter.columns = ["Player", "Count"] 
    print(bobCounter)
    graph_img(bobCounter["Count"], bobCounter["Player"], str3, str)  
else:
    str = input("Enter Player: ")
    test = df[df["Player"] == str]
    print(test)
    bobCounter = (test.Ship.value_counts())
    bobCounter = bobCounter.reset_index()
    bobCounter.columns = ["Ship", "Count"]
    print(bobCounter)
    graph_img(bobCounter["Count"], bobCounter["Ship"], str3, str)  
    
# bobCounter = bobCounter.reset_index()