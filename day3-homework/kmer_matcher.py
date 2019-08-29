#!/usr/bin/env python3

"""
Commands: enter this argument:
./.py file subset.fa droYak2_seq.fa 11
 script, target file, query file, and kmer number
"""

#use previously developed FASTAReader to make the work below easier.
from fasta import FASTAReader
import sys

#add our files
target = FASTAReader(open(sys.argv[1])) # this is target (subset.fa)
query = FASTAReader(open(sys.argv[2])) # this is query file
k = int(sys.argv[3]) # this is the length of kmer

#initialize dictionary that holds the kmer (sequence) as the key and a tuple that contains the name 
target_dictionary = {}


#for loop to go through target file
for name_t, sequence_t in target:
    for i in range(0, len(sequence_t) - k + 1):
        #set kmer_t length and make letters IN CAPS
        kmer_t = sequence_t[i:i+k].upper()
        #since we are using a dictionary, add name_t and i into the values section and assign it to specific kmer_t
        target_tuple = (name_t, i)
        if kmer_t in target_dictionary:
            target_dictionary[kmer_t].append(target_tuple)
        else:
            target_dictionary[kmer_t] = [target_tuple]

#this for loop is to search for the kmer defined above.  If it is in the above dictionary, print out the name_t (gene name?), the index at which it was found (i), and the actual kmer in that case.
for name_q, sequence_q in query:
    for i in range(0, len(sequence_q) - k + 1):
        kmer_q = sequence_q[i:i+k].upper()
        if kmer_q in target_dictionary:
            for target_tuple in target_dictionary[kmer_q]:
                print(target_tuple, i, kmer_q)
                #the purpose of this for loop is to avoid printing one gene in one line and instead having multiple lines for where a gene has multiple alignments across the genome.