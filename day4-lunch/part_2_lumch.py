#!/usr/bin/env python3

"""
Usage:
1. Create a new script that uses scatter() to plot the FPKM values of two samples 
specified at the command line:
2. Provide plot title and label axes
3. Compensate for extreme values by log transforming your values (be sure not to l
lose any transcripts)
4. Compensate for overlapping points by adjusting transparency
5. Fit a curve using numpy polyfit
HINT: print the type() and value

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

ctab1 = []
ctab2 = []



for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    ctab1.append(float(fields[11])+1)
    
    
for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    ctab2.append(float(fields[11])+1)

log_ctab1 = np.log2(ctab1)
log_ctab2 = np.log2(ctab2)    
coef = np.polyfit(log_ctab1, log_ctab2, 1)
x_val = np.linspace(min(log_ctab1), max(log_ctab1), 100)   

def f(x, m, b):
    return x*m+b
y_val = f(x_val, coef[0], coef[1])
#print(exons[1])
#print(lengths[1])




fig, ax = plt.subplots() #can have more than two, for figure a,b,c,et cetera

ax.scatter(x=log_ctab1, y=log_ctab2, s=3, alpha = 0.2)
#ax.plot([0,13],[0,13], color = "red") #you are passing coordinates, not "x = "
ax.plot(x_val,y_val, color = "red")
plt.suptitle("ctab1 vs. ctab2")
plt.xlabel("ctab1")
plt.ylabel("ctab2")

fig.savefig("ctab1-v-ctab2.png")
plt.close(fig)






    
   #00  ../results/stringtie/