#!/usr/bin/env python3
#advanced #1


#Flages
# 0 on forward strand
#16 on reverse strand (bit mask 10000) four zeros becuase 2^4 which is 16

bit_mask = 0b10000

import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
count = 0

for i, line in enumerate(f):
    #if line.startswith("@"):
       # continue
    fields = line.split("\t")
    #if fields[5] =="*":
        #continue

if int(fields[1]) & bit_mask:
    count +=1
    
print(count)
    
