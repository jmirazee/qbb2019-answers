#!/usr/bin/env python3


"""
Usage: ./metadata.py <metadata.csv> <ctab_dir>
metadata.csv = samples.csv

<ctab.dir> e.g. ~/qbb2019-answers/results/stringtie/

Create all.csv with FPKMs

t_name, gene_name, sample1, ..., samplen


./00-metadata.py ~/qbb2019/data/samples.csv ~/qbb2019-answers/results/stringtie/


"""

import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

#us apndas
fpkms = {}

for i, line in enumerate(open(metadata)):
    if i == 0:
        continue
    fields = line.strip("\n").split(",")
    srr_id = fields[0]
    ssr_sex = fields[1]
    srr_time = fields[2]
    srr_join = ssr_sex + "_" + srr_time
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    
    
    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[srr_join] = df.loc[:,"FPKM"] #this stores only FPKMs as a value in dictionary
df_fpkms = pd.DataFrame(fpkms)
#print(df_fpkms.describe())

pd.DataFrame.to_csv(df_fpkms, "hw1-all.csv")  

#to add additional column:

#t_name,gene_name,male_11,male_12,male_13,
#_______________________________
