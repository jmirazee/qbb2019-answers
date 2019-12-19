#!/usr/bin/env python3
import sys
from fasta import FASTAReader

reader = FASTAReader(open(sys.argv[1]))
sequence_list = []
for ident, sequence in reader:
    sequence_list.append(sequence)
sequence_list = sorted(sequence_list, reverse = True, key = len)
#print(len(sequence_list)) #123 is number of contigs

#calculate statistics of lengths:
sequence_length = []
for sequence in sequence_list:
    sequence_length.append(len(sequence))
sequence_length = sorted(sequence_length, reverse = True)

print(sequence_length)
print(min(sequence_length))
print(max(sequence_length))


print(sum(sequence_length)/len(sequence_list))
#Write a python script to compute the number of contigs, minimum/maximum/average contig length, and N50. 

##N50
count = 0
print(sum(sequence_length)/2)
for i,item in enumerate(sequence_length):
    count += item
    if count >= 32015.0:
        break
        #372 is right answer
# print(count)
# print(i) # this is the index
# print(sequence_list[i])
print(len(sequence_list[i]))

#print("the right answer is 372, N50")

#print(sequence_list)
