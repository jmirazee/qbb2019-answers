#!/usr/bin/env python3

"""
Usage: ./01-hist.py <ctab>

Plot FPKM

Modify the code we created to plot a histogram of FPKM values (01-hist.py).
Eyeball the best parameters and submit your plot. The changes you make should include:

1Specify scipy.stats parameters on the command line
2Add a skewnorm distribution
3Provide plot title and label axes
4Document parameters as text in the plot

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import skewnorm

fpkms = []
#lengths = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append(float(fields[-1]))

#print(len(fpkms))
#print(fpkms)

my_data = np.log2(fpkms)

a = float(sys.argv[2]) # this is skewness I put -10
mu_sq = float(sys.argv[3]) #last time I put 6
sigma_sq = float(sys.argv[4]) #last time I put 3.5
mu_norm = float(sys.argv[5]) # set as 4
sigma_norm = float(sys.argv[6]) # set as 2


x = np.linspace(-15, 15, 100)
y = stats.norm.pdf(x, mu_norm, sigma_norm)
z = skewnorm.pdf(x, a, mu_sq, sigma_sq)
#print(y)
#print(type(y)) 
#print(x) #numpy.ndarray (learn more about this)
#print(type(x)) # this prints the type that x is

fig,ax = plt.subplots()
ax.hist(my_data, bins = 100, density =  True) # bins gives more resolution
#ax.xscale('log FPKMS')
ax.plot(x,y) # this gives you a normal distribution
ax.plot(x,z)
plt.suptitle("FPKMs")
plt.xlabel("Log transformed FPKMs")
plt.ylabel("Percentage of Log2 transformed relative to total FPKMs")
plt.figtext(x =.05, y = .92, s = "a = -10, mu_sq = 6, sigma_sq = 3.5, mu_norm = 4, sigma_norm = 2")
fig.savefig("fpkms_eyeball.png")
plt.close(fig)



    #exons.append(int(fields[6]))
    #lengths.append(int(fields[7]))
#print(exons[1])
#print(lengths[1])

# fig, ax = plt.subplots() #can have more than two, for figure a,b,c,et cetera
#
# ax.scatter(x=exons, y=lengths)
# ax.plot([0,40],[0,20000], color = "red") #you are passing coordinates, not "x = "
# fig.savefig("exon-v-length.png")
# plt.close(fig)