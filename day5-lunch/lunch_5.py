#!/usr/bin/env python3

"""
Usage : ./lunch_4.py <c.tab file>

"""

#/Users/cmdb/qbb2019-answers/results/stringtie/SRR072893
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.decomposition import PCA
import scipy



#We need to import in the dataframe. You first have to set the delimeter to tab before setting the index col becuase you don't have columns until you have sep = \t
df = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")

#now want to make a dataframe just from the FPKM column
fpkms = pd.DataFrame(df["FPKM"])

#create a new column called log_FPKM - this is for the log questions, not for linear
#fpkms['log_FPKM'] = np.log2(fpkms.loc[:,'FPKM'] + 1)

#print(fpkms)

#for the tab files, we have six columns, but we need to add headers to each of them. The following: 
#'t_name','size','covered','sum','mean0','mean'. But we are actually only intersted in the mean and T-name column. So when I add it, I will only add those coluymnsx.


#deo code below three times, lol I know I hsould have dont for loop

H3K4me3 = pd.read_csv(open("H3K4me3_bed.tab"), sep = "\t", names=['t_name','size','covered','sum','mean0','H3K4me3_mean'])

#we just need the first and last column.

H3K4me3 = H3K4me3.loc[:,["t_name", "H3K4me3_mean"]]


#I couldn't figure out how to merge all DFs at once, so I'm doing it one at a time and overwriting df_fpkms_merge.

df_fpkms_merge = pd.merge(fpkms,H3K4me3, on="t_name")


#print(H3K4me3)

#print(fpkms)
#print(H3K4me3.to_string())

#H3K4me3.to_string() prints out entire df
#_____________________________

H3K4me1 = pd.read_csv(open("H3K4me1_bed.tab"), sep = "\t", names=['t_name','size','covered','sum','mean0','H3K4me1_mean'])

#we just need the first and last column.

H3K4me1 = H3K4me1.loc[:,["t_name", "H3K4me1_mean"]]
#print(H3K4me1)

df_fpkms_merge = pd.merge(df_fpkms_merge,H3K4me1, on="t_name")

#_____________________________

H3K9me3 = pd.read_csv(open("H3K9me3_bed.tab"), sep = "\t", names=['t_name','size','covered','sum','mean0','H3K9me3_mean'])

#we just need the first and last column.

H3K9me3 = H3K9me3.loc[:,["t_name", "H3K9me3_mean"]]
#print(H3K9me3)

df_fpkms_merge = pd.merge(df_fpkms_merge,H3K9me3, on="t_name")

#________________________________


#we only need fpkms and the means of each mark


model = sm.formula.ols(formula="FPKM ~ H3K4me3_mean + H3K4me1_mean + H3K9me3_mean", data=df_fpkms_merge)

ols_results = model.fit() # does least squares fitting

#print(ols_results.summary())


##############################################
#New Code For Number 5:

residuals = ols_results.resid

fig, ax = plt.subplots()



ax.hist(residuals,bins=1000, range=(-100,100))
ax.set_xlim((-100,100))
ax.set_xlabel('Residual values')
ax.set_ylabel('Counts')
ax.set_title('Residuals from FPKM-mark Model')
fig.savefig('lunch_pt_5_residuals_FPKM_mark_hist.png')
plt.close(fig)





#now specify model that we want to fit. put outcome on left, predicter on right. ~ means "depends on"

# R-squred how much variance in outcome is explained by predictor. If 0 nonrelated

#look at coef and see if it falls between 0 in the confidence interval




