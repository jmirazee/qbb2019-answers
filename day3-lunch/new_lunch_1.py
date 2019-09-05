#!/usr/bin/env python3

"""
Fresh look at the code, redid it.

/Users/cmdb/data/genomes/BDGP6.Ensembl.81.gtf

Goal: start at a specified point on genome, and keep searching 
along until a protein coding gene is found

/Users/cmdb/data/genomes/BDGP6.Ensembl.81.gtf
"""


import sys

gene_list = []



for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    fields = line.strip("\n").split()
    if ('gene_biotype "protein_coding"' not in line) or ("3R" not in line) or (fields[2] != "gene"):
        continue
    start = fields[3]
    end = fields[4]
    gene_id = fields[13]
    gene_list.append((int(start), int(end), gene_id))
gene_list.sort()


snp_pos = 21378950
lo = 0
mid = 0
hi = len(gene_list)-1
number_iterations = 0

#print(gene_list) This works!

#use mid, lo and high as a way to index the list and move up the list

while (lo < hi):
    mid = int((hi+lo)/2)
    number_iterations +=1
    if snp_pos < gene_list[mid][0]:
        hi = mid
    elif snp_pos > gene_list[mid][1]:
        lo = mid +1
    else:
        break
print(gene_list[lo], number_iterations)
    
       #
       #
       # if "3R" in line[0] and "protein_coding" in line[8]:
       #     col = line[8].split(" ")
       #     x = col.index("gene_biotype")
       #     if "protein_coding" in col[x+1]:
       #
       #         if "+" in line[6]:
       #             start = line[3]
       #             #print(start)
       #         elif "-" in line[6]:
       #             start = line[4]
       #             #print(start)
       #         line.append(start)
       #
       #         gene_list.append(line)