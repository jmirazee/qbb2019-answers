#!/usr/bin/env python3

"""
Usage: ./make_pca.py <eigenvec file>
<eigenvec file> Eigenvector output file from PLINK
Makes a PCA plot from the PLINK analysis output.
"""

import sys
import matplotlib.pyplot as plt
#plt.style.use('ggplot')

zPCA_1 = []
zPCA_2 = []

for i, line in enumerate(open(sys.argv[1])):
    fields = line.rstrip("\n").split("\t")
    zPCA_1.append(float(fields[2]))
    zPCA_2.append(float(fields[3]))
 
 
    
# Plot in a scatterplot
fig, ax = plt.subplots()
ax.scatter(zPCA_1,zPCA_2, alpha=0.3, s=5, color="blue")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("PCA")
plt.tight_layout()
fig.savefig("pca.jpeg")
plt.close(fig)
