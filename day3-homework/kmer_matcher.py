#!/usr/bin/env python3

"""
match all kmers in a FASTA file

#subset.fa is our target
# the dro is query


1. I ran fasta.py on the fasta sequence so that I could parse it
2. 
"""

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) # this is target (subset.fa)
#pep8

query = FASTAReader(open(sys.argv[2])) # this is query file

k = int(sys.argv[3])
kmers = {}

for ident, sequence in target:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            kmers[kmer]+=1
        else:
            kmers[kmer] = 1

for kmer,count in kmers.items():
    print(kmer, count, sep="\t")
    

# ./count_kmers.py 11  < subset.fa | less -S

