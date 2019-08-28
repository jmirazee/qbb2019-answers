#!/usr/bin/env python3

"""
match all kmers in a FASTA file

#subset.fa is our target
# the dro is query


1. I ran fasta.py on the fasta sequence so that I could parse it
2. 


[usage statement]: enter this argument:
./.py file subset.fa droYak2_seq.fa 11
 script, target file, query file, and kmer number
"""

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) # this is target (subset.fa)
#pep8

query = FASTAReader(open(sys.argv[2])) # this is query file

k = int(sys.argv[3])

target_dictionary = {}

#replace query with target 
for name_t, sequence_t in target:
    for i in range(0, len(sequence_t) - k + 1):
        kmer_t = sequence_t[i:i+k].upper()
        target_tuple = (name_t, i)
        if kmer_t in target_dictionary:
            target_dictionary[kmer_t].append(target_tuple)
        else:
            target_dictionary[kmer_t] = [target_tuple]

for name_q, sequence_q in query:
    for i in range(0, len(sequence_q) - k + 1):
        kmer_q = sequence_q[i:i+k].upper()
        if kmer_q in target_dictionary:
            print(target_dictionary[kmer_q], i, kmer_q)
            
            # for each kmer, we want to show name_T, i, i, kmer_q 
            # kmer1
        
        
        
        
# for value_q, sequence_q in query:
#     for i in range(0, len(sequence_q) - k + 1):
#
#         kmer_q = sequence_q[i:i+k]
#
#
#
# if kmer_q == kmer_t:
#     empty_list.append(kmer_t, kmer_q)
#
#
#
#
#
#         if kmer in kmers:
#             kmers[kmer]+=1
#         else:
#             kmers[kmer] = 1
#
# for kmer,count in kmers.items():
#     print(kmer, count, sep="\t")
#
#
# # ./count_kmers.py 11  < subset.fa | less -S
#
