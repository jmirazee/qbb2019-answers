#!/usr/bin/env python3

"""
parse and find all genes in chromosome 3R
Gene biotype is in column 16 == column[15]
"""
import sys

gene_list=[]
start = 0

f = open(sys.argv[1])
for line in f:
    line = line.rstrip("\n").split("\t")
    if "3R" in line[0] and "protein_coding" in line[8]:
        col = line[8].split(" ")
        x = col.index("gene_biotype")
        if "protein_coding" in col[x+1]:
            gene_list.append(line)
            if "+" in line[6]:
                start = line[3]
                #print(start)
            elif "-" in line[6]:
                start = line[4]
                line.append(start)
            
print(gene_list[1])
                
                         
            
            
            
            
            # gene_list.append((col[3], col[4]))
            #
            # print(gene_list)
            #
        #
#
# search_pos = 10
# lo = 0
# hi = len(gene_list)-1
# mid = 0
# number_iterations = 0
#
# while (lo <= hi):
#     mid = (float(hi)+float(lo)) / 2
#     number_iterations = number_iterations + 1
#     if (search_pos < gene_list[mid][0]):
#         pick lo
#     elif (search_pos > gene_list[mid][1]):
#         pick hi
#     else:
#         gene_list[mid] spans the search_pos
#
#
#
#
#
#
#             #print(column[0], col[x+1])
#             print(line)
#
#
#
#             #then use stdout with command line to save to out file.
#
#
#
#
#     #if str(line[3].contains("DROME")) and str(line[4].contains("FBgn")):
#      #   columns.append(line)
# #print(columns)
#
#