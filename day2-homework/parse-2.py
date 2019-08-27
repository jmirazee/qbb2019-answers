#!/usr/bin/env python3

"""
Write a python script for identifier mapping. Your script should take as input the mapping file 
(as above) and a c_tab file from StringTie and find the corresponding translation from the 
mapping file. If found, it should print the line from the c_tab file with the identifier. 
If not found, it should do one of two things depending on a command line argument:

Print nothing (ignore the line)
Print and fill the field with a default value
"""

#mapping_file = out.txt
#c_tab = /Users/cmdb/data/results/stringtie/SRR072893/t_data.ctab


#z =  out
#f = path one
#import sys

#z = open(sys.argv[1]) #mapping
#f = open(sys.argv[2]) #ctab
#for i,line in enumerate(z):
#    columnz = line.split()
    
#for i,line in enumerate(f):
#    columns = line.split()
#    for field in columns:
#        if columns[8] in f == columnz[0] in z:
 #           print(columns[8], columns[9])
            
            
import sys

final_dict = {}

for line in open(sys.argv[1]):
    columns = line.rstrip("\n").split()
    FBgn = columns[0]
    final_dict[FBgn] =  columns[1]
        
#print(final_dict)

for line in open(sys.argv[2]):
    columnz = line.rstrip("\n").split()
    gene_id = columnz[8]
    
    
    if gene_id not in final_dict and sys.argv[3] == "nothing":
        continue    
    elif gene_id not in final_dict and sys.argv[3] == "default":
        print("false")
    elif gene_id in final_dict:
        print(line + final_dict[gene_id])

     
     
 
 #for line in blank: 
 #   entry = columnz[9]
 #   if entry == " ":
 #       print(blank)
    
  #  
 #   if not in final
  #      for line in open(sys.argv[3]):
    
#arg 3 will be some word
        
  #/Users/cmdb/data/results/stringtie/SRR072893/t_data.ctab       
        
    
    



