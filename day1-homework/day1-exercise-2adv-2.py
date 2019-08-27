#!/usr/bin/env python3
# using test file, want to isolate column 11 (10) and ,then convert the characters using ord into values. 

#Then with the entire file, I want to find the sums that are greater than 30 and then see how many of those are. I want to put each value in a list and then see how many in the lsit are greater than 30.


#OVERALL PROBLEMS:
#--wasn't able to complete because even though I could isolate values of fields10, could not convert to list for some reason. I tried it with a smaller test file and always the last entry would be the only value there.


#part 1
import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
for line in f:
    line = line.rstrip("\n")
    fields = line.split("\t")
    storage = []
    storage = (fields[10])
    
print(storage) # only printed one

for character in storage:
    value_ord = ord(character)
#print(value_ord) # got 67

final_list = ''
if value_ord > 30:
    final_list += str(value_ord)
print(final_list)
    




  
#final_list = []
#print(storage)
#for line in storage:
#    for character in line:
#        ord(character)
#        value_ord +=ord(character)
#        final_list += value_ord
#print(final_list)
    

    
    
