#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import numpy as np
list_y = []
list_x = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    y = int(fields[5]) - int(fields[4])
    x = int(fields[8])
    list_y.append(y)
    list_x.append(x)
#print(list_y)   

fig, ax = plt.subplots() #can have more than two, for figure a,b,c,et cetera
fig.suptitle("Dotplot_Spades_improve_2")

ax.scatter(x=list_x, y=list_y, alpha = 0.2)
ax.set_xlabel("total len of contigs")
ax.set_ylabel("len of reference")


fig.savefig("Dotplot_Spades_improve_2.png")
plt.close(fig)