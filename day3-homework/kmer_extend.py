#!/usr/bin/env python3

"""
[usage statement]: enter this argument:
./.py file subset.fa droYak2_seq.fa 11
 script, target file, query file, and kmer number
"""

from fasta import FASTAReader
import sys
target = FASTAReader(open(sys.argv[1])) # classes are generally camel-case
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3]) # command line prompt will tell the number of units it's looking to match (e.g., 4, 11)

#basically do same thing as excercise 1 here
target_dictionary = {}

for name_t, sequence_t in target:
   for i in range(0, len(sequence_t) - k + 1):
       kmer_t = sequence_t[i:i+k].upper()
       target_tuple = (name_t, i)
       if kmer_t in target_dictionary:
           target_dictionary[kmer_t].append(target_tuple)
       else:
           target_dictionary[kmer_t] = [target_tuple]
        
#initialize new list that will contain the final info
extended_kmers = []


for name_q, sequence_q in query:
   for j in range(0, len(sequence_q) - k + 1):
       kmer_q = sequence_q[j:j+k].upper()
       if kmer_q not in target_dictionary:
           continue
       else:
           for target_tuple in target_dictionary[kmer_q]:

#now instead of print, move on by starting a while loop to extend kmers. 
#start "x" counter at 1.

#we only need to increase the size of the kmer from the righr!

#J = index of query
#I = index of target file

               x = 1 
               new_kmer_q = kmer_q
               while True:
                   if j-x == 0 or i-x == 0:
                       break
                       #why needed? Because this would mean we are at beginning and don't need to go further.
                       
                       #if letter in query = letter in target, add to new string.
                   if sequence_q[j-x] == sequence_t[i-x]:
                       new_kmer_q = sequence_q[j-x].join(new_kmer_q)
                       x += 1
                   else:
                       break
                       
            #don't actually need the commented out things below, for left       
               # x = 1
#                while True:
#                    if j+k+x >= (len(sequence_q) - 1) or i+k+x >= (len(sequence_t) - 1):
#                        break
#                    if sequence_q[j+k+x] == sequence_t[i+k+x]:
#                        new_kmer_q = "".join(new_kmer_q, sequence_q[j-x])
#                        x += 1
#                    else:
#                        break
               extended_kmers.append(new_kmer_q) #put new_kmer_q string in list?
extended_kmers.sort(reverse = True, key = len) #sort list
for new_kmer_q in extended_kmers:
   print(new_kmer_q) 
                    