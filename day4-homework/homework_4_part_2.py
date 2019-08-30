#!/usr/bin/env python3

"""
Usage: ./01-boxplot.py <gene_name> <FPKMs.csv>
Boxplot all transcripts for a given gene

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gene_name = sys.argv[1]
fpkm_file = sys.argv[2] #modified csv


df = pd.read_csv(fpkm_file, index_col = "t_name") # index col is row name

#boolean filter

goi = df.loc[:,"gene_name"] == gene_name  # matches our input

#data.iloc[:, 0:2] # first two columns of data frame with all rows

fpkms = df.drop(columns = "gene_name") 

male = df.iloc[:, 1:9]

female = df.iloc[:, 9:18]



#fpkms_m = df.drop(columns = "gene_name") # to remove columsn
#fpkms_f = df.drop(columns = "gene_name")

#print(male)
#print(female)

fig,(ax1,ax2) = plt.subplots(2)


log_male = np.log2(male+1)
log_female = np.log2(female+1) 

ax1.boxplot(log_male.loc[goi,:].T) #.T is to traspose
ax1.set_title('Male boxplot')
#ax1.set_xlabel('Sample name')
ax1.set_ylabel('log FPKM')
ax1.set_xticklabels(["10","11","12","13","14A","14B","14C","14D"], rotation =45)


#ax1.set_xticks(1,2,3,4,5,6,7,8)
#ax1.set_xtickslabels(male_10,male_11,male_12,male_13,male_14A,male_14B,male_14C,male_14D)

#rotation=45

ax2.boxplot(log_female.loc[goi,:].T) #.T is to traspose
ax2.set_title('Female boxplot')

ax2.set_ylabel('log FPKM')
ax2.set_xticklabels(["10","11","12","13","14A","14B","14C","14D"], rotation =45)

#ax2.set_xticks(1,2,3,4,5,6,7,8)
#ax2.set_xtickslabels(female_10,female_11,female_12,female_13,female_14A,female_14B,female_14C,female_14D)

plt.subplots_adjust(hspace=.7)
fig.savefig("hw_q2-boxplot.png")
plt.close()


#_________________________

# df = pd.read_csv(fpkm_file, index_col = "t_name") # index col is row name
#
# #boolean filter
#
# goi = df.loc[:,"gene_name"] == gene_name  # matches our input
# fpkms = df.drop(columns = "gene_name") # to remove columsn
#
# #print(fpkms)
# #print(fpkms.loc[goi,:])
#
# fig, ax = plt.subplots()
# ax.boxplot(fpkms.loc[goi,:].T) #.T is to traspose
# fig.savefig("boxplot.png")
# plt.close()