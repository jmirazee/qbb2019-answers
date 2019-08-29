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
target = FASTAReader(open(sys.argv[1])) # classes are generally camel-case
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3]) # command line prompt will tell the number of units it's looking to match (e.g., 4, 11)
target_dictionary = {}
name_dictionary = {}
for name_t, sequence_t in target:
   name_dictionary[name_t] = sequence_t
   for i in range(0, len(sequence_t) - k + 1):
       kmer_t = sequence_t[i:i+k].upper()
       target_tuple = (name_t, i)
       if kmer_t in target_dictionary:
           target_dictionary[kmer_t].append(target_tuple)
       else:
           target_dictionary[kmer_t] = [target_tuple]
extended_kmers = []
for name_q, sequence_q in query:
   for j in range(0, len(sequence_q) - k + 1):
       kmer_q = sequence_q[j:j+k].upper()
       if kmer_q not in target_dictionary:
           continue
       else:
           for target_tuple in target_dictionary[kmer_q]:
               #print(target_tuple, j, kmer_q)
               x = 1
               new_kmer_q = kmer_q
               while True:
                   if j-x == 0 or i-x == 0:
                       break
                   if sequence_q[j-x] == sequence_t[i-x]:
                       new_kmer_q = sequence_q[j-x].join(new_kmer_q)
                       x += 1
                   else:
                       break
               x = 1
               while True:
                   if j+k+x >= (len(sequence_q) - 1) or i+k+x >= (len(sequence_t) - 1):
                       break
                   if sequence_q[j+k+x] == sequence_t[i+k+x]:
                       new_kmer_q = "".join(new_kmer_q, sequence_q[j-x])
                       x += 1
                   else:
                       break
               extended_kmers.append(new_kmer_q)
extended_kmers.sort(reverse = True, key = len)
for new_kmer_q in extended_kmers:
   print(new_kmer_q)
                    
            
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
