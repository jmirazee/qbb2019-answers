#!/usr/bin/env python3

"""
Count all kmers in a FASTA file
"""

from fasta import FASTAReader
import sys

reader = FASTAReader(sys.stdin)
#pep8

k = int(sys.argv[1])
kmers = {}

for ident, sequence in reader:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            kmers[kmer]+=1
        else:
            kmers[kmer] = 1

for kmer,count in kmers.items():
    print(kmer, count, sep="\t")
    

# ./count_kmers.py 4  < subset.fa | less -S