#!/usr/bin/env python3

"""
parse and find all genes in chromosome 3R
Gene biotype is in column 16 == column[15]
"""


import sys

gene_list = []
snp_pos = "21378950"
start = 0
number_iterations = 0

with open(sys.argv[1]) as file:
   for line in file:
       line = line.strip("\n").split("\t")
       if "3R" in line[0] and "protein_coding" in line[8]:
           col = line[8].split(" ")
           x = col.index("gene_biotype")
           if "protein_coding" in col[x+1]:
               
               if "+" in line[6]:
                   start = line[3]
                   #print(start)
               elif "-" in line[6]:
                   start = line[4]
                   #print(start)
               line.append(start)
               
               gene_list.append(line)
                              
low = 0
high = float(len(gene_list)-1)
mid = float((high+low)/2)

while(low<=high):
    mid = (high+low)/2
    #mid = x
    number_iterations = number_iterations +1
    #for gene_list(mid):
    if int(gene_list[-1]) < snp_pos:
        break
    if gene_list[x][-1] > snp_pos:
        high = mid
    elif gene_list[x][-1] < snp_pos:
        low = mid
    elif gene_list[x][-1] == snp_pos:
        
    
print(number_iterations)
    
    



#what other didf:


    
 






