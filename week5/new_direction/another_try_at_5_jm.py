#!/usr/bin/env python3


import statistics
import matplotlib.pyplot as plt

"""
Usage: ./.py new_blast_output.fa aa_alignment.out week5_query.fa

./101019_code.py new_direction/100919_blast_output.fa new_direction/100919_mafft_output 

week5_query.fa
"""
import sys
from fasta import FASTAReader
import numpy as np


dna_seqs={}
protein_seqs={}

dna_reader = FASTAReader(open(sys.argv[1]))
for ident, sequence in dna_reader:
    ident = ident + "_1"
    dna_seqs[ident] = sequence
#print(dna_seqs)


protein_reader = FASTAReader(open(sys.argv[2]))
for ident, sequence in protein_reader:
    protein_seqs[ident] = sequence   
#print(protein_seqs)


nuc_aligned = {}
#print(range(len(dna_seqs))) #= 1001 for both prot and dna

for seq_id in protein_seqs:
    counter = 0
    gap_dna = ""
    for num,a in enumerate(protein_seqs[ident]):
        if a == "-":
            gap_dna+="---"
        else:
            gap_dna += dna_seqs[seq_id][(counter*3):(counter*3)+3]
            #print(dna_seqs[seq_id][(counter*3):(counter*3)+3])
            counter+=1
    nuc_aligned[seq_id] = gap_dna
        
#print(nuc_aligned)

codon_dict = {
      "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
      "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
      "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
      "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
      "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
      "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
      "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
      "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
      "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
      "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
      "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
      "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
      "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
      "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
      "TAC":"Y", "TAT":"Y", "TAA":"", "TAG":"",
      "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W",
  }


for i in range(0,len(nuc_aligned["query_1"]),3):
    z_score = []
    list_seq = []
    q_codon = nuc_aligned["query_1"][i:i+3]
     
     
    for seq_id in nuc_aligned:
        codon = nuc_aligned[seq_id][i:i+3]
        if codon == q_codon not in codon_dict or codon not in codon_dict:
            continue
        elif codon_dict[codon] == codon_dict[q_codon]:
            list_seq.append(-1)
        elif codon_dict[codon]!=codon_dict[q_codon]:
            list_seq.append(1) 
    #print(list_seq)
    from scipy import stats
    z = stats.zscore(list_seq)
    print(z)

#     mean = sum(list_seq)/len(list_seq)
#     std = statistics.stdev(list_seq)
#     z =
#
# print(mean)
# print(std)
#
    


# for i in range(0,len(aligned_dna["query"]), 3):
#    q_codon = aligned_dna["query"][i:i+3]
#    for j in range(1, total_number):
#        seq_id = blast_dnaid[j]
#        dna_seq = aligned_dna[seq_id]
#        seq_codon = dna_seq[i:i+3]
#        if q_codon != seq_codon:
#            q_aa = protein_id["query"][int(i/3)]
#            seq_aa = protein_id[seq_id][int(i/3)]
#            if q_aa == seq_aa:
#                if q_codon not in dS:
#                    dS[q_codon] = 1
#                else:
#                    dS[q_codon] += 1
#            if q_aa != seq_aa:
#                if q_codon not in dS:
#                    dN[q_codon] = 1
#                else:
#                    dN[q_codon] += 1
#