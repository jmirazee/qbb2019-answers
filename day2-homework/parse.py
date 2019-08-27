#!/usr/bin/env python3

"""
parse and get two column file output
FBgn and DROME
"""
import sys

f = open(sys.argv[1])
for i,line in enumerate(f):
    columns = line.split()
    for field in columns:
        if field.endswith("DROME"):

            print(columns[-1], columns[-2])
            
            #then use stdout with command line to save to out file.


   
   
    #if str(line[3].contains("DROME")) and str(line[4].contains("FBgn")):
     #   columns.append(line)
#print(columns)
            
        