"""
parse and find all genes that are protein coding
"""
import sys

f = open(sys.argv[1])
for line in f:
    column = line.split()
    if "protein_coding" in column[0]:
        print(line)