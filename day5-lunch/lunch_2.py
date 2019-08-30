#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.decomposition import PCA

ctab_file = sys.argv[1]


df = pd.read_csv(ctab_file, sep = "\t")

goi_p = df.loc[:,"strand"] == "+"
goi_n = df.loc[:,"strand"] == "-"



p_start = df.loc[goi_p,["chr","start","end", "strand","t_name"]]
n_end = df.loc[goi_n,["chr","start","end", "strand","t_name"]]


p_start.loc[:, "start"] -= 500
p_start.loc[:,"end"] = p_start.loc[:,"start"] + 1000
n_end.loc[:,"end"] += 500
n_end.loc[:,"start"] = n_end.loc[:,"end"] - 1000

roi = p_start.loc[:,"start"]<= 0
p_start.loc[roi, "start"] = 1

roi2 = n_end.loc[:,"start"]<= 0
n_end.loc[roi2, "start"] = 1



new_df = p_start.append(n_end)

#new_df = df.drop(columns = " ")

new_df = new_df.drop(columns = "strand")

new_df.to_csv("promoter.bed", sep = "\t", header=None, index=False) 




#p_start_correct = p_start.loc[int():,"strand"] < 0
#p_start.loc[:, "start"] == 1
#p_start_final = df.loc[p_start_correct,["chr","start","end", "strand","t_name"]]







#print(p_start)

#print(p_start, n_end)


# from pandas import DataFrame
#
# Numbers = {'set_of_numbers': [1,2,3,4,5,6,7,8,9,10]}
# df = DataFrame(Numbers,columns=['set_of_numbers'])
#
# df.loc[df.set_of_numbers <= 4, 'equal_or_lower_than_4?'] = 'True'
# df.loc[df.set_of_numbers > 4, 'equal_or_lower_than_4?'] = 'False'
#
# print (df)


#goi = pd.DataFrame(df.iloc[:,]


#col_names = df.columns.values.tolist()

#print()





#df = df.drop(columns = "gene_name")


#if - strand use +
#if + strand use -