#!/usr/bin/env python3

"""
Usage: ./make_pca.py <eigenvec file>
<eigenvec file> Eigenvector output file from PLINK
Makes a PCA plot from the PLINK analysis output.
"""

import sys
import matplotlib.pyplot as plt

allele_freq = []

for i,line in enumerate(open(sys.argv[1])):
        if i==0:
            continue
        
        fields = line.rstrip("\n").split()
        allele_freq.append(float(fields[5]))

print(allele_freq)
# Plot in a scatterplot
fig, ax = plt.subplots()
ax.hist(allele_freq, color ="orange", bins = 100, alpha =0.8)
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("Counts")
ax.set_title("Histogram of Allele Frequencies")
fig.savefig("allele_freq.jpeg")
plt.close(fig)