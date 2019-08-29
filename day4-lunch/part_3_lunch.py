#!/usr/bin/env python3

"""
Usage:
1. In a third script combine FPKM values from an arbitrary number of ctab files 
specified at the command line. Only report transcripts that exceed a threshold 
FPKM. Allow the user to specify whether:

2. Threshold should be applied to the total rowsum
3. Only one sample needs to exceed threshold
4. Usage: ./merge_fpkms.py <threshold> <criteria> <ctab_file1> <ctab_file2> ... <ctab_filen>

"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd
import sys
import os

threshold = float(sys.argv[1])
criteria = float(sys.argv[2])

for i in range(3:len(sys.argv[])):


    for j, line in enumerate(open(i)):
        if j == 0:
            continue
            fields = line.rstrip("\n").split("\t")
            ctab1.append(float(fields[11]))
            





