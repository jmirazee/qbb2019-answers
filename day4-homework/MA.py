#!/usr/bin/env python3

"""
Usage: ./04-marge.py <ctab1> <ctab2>

SSR file is ctab1


"""
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import numpy as np

name1 = sys.argv[1].split(os.sep)[-2] #split cleans up the column headers to the SRR inside our file path name
name2 = sys.argv[2].split(os.sep)[-2]

ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name") #index col gives you unique transcript numbers instead of just row number
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm = {name1 : ctab1.loc[:,"FPKM"],
        name2 : ctab2.loc[:,"FPKM"]}
# fpkm = {"sample1": [1,2,3],
#         "sample2": [4,5,6]}

df = pd.DataFrame(fpkm)
df += 1

r = df.loc[:,name1]
g = df.loc[:,name2]

m = np.log2(r/g)
a = 0.5*np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter(a,m, alpha =0.3, s = 5)

plt.xlabel("Log2 Average Expression")
plt.ylabel("Log 2(SRR072893/SRR072894)")  
plt.suptitle("MA plot")

fig.savefig("MA_scatter.png")
plt.close(fig)



#print(df)
#print(type(df)) #<class 'pandas.core.frame.DataFrame'>