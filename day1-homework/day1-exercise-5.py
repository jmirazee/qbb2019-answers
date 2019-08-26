#!/usr/bin/env python3

#count number of alignments

import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
listo = []
for i, line in enumerate(f): 
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[5] =="*":
        continue  
    listo.append(int(fields[4]))

avg = sum(listo)/len(listo)

print(avg)

