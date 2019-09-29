#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


"""
Usage: maing read_depth plot

the read depth distribution across each called variant
the genotype quality distribution
the allele frequency spectrum of your identified variants
a summary of the predicted effect of each variant as determined by snpEff (barplot?)

"""

#the read depth distribution across each called variant
DP_list = []
Gene_qualities = []
allele_freq = []
with open("parsed_vcf") as f:
    
    for line in f:
        if line.startswith("#"):
            continue
        if ";" in line:
            fields = line.split(";")
            info = str(fields[7])
            info2 = info.replace("DP=","")
            af = str(fields[3])
            af2 = af.replace("AF=","")
            for element0 in af2.split(","):
                allele_freq.append(float(element0))
            
            
            #DP_list.append(info2)
            for element in info2.split(","):
                DP_list.append(int(element))
            tab_part = fields[0]
            columns = tab_part.split("\t")
            gene_quals = (columns[1])
            Gene_qualities.append(int(gene_quals))
#print(Gene_qualities)
#print(DP_list) # works!, list of numbers


# Create a multi-panel figure
fig, axes = plt.subplots(nrows=2,ncols=2,figsize=(20, 10))
# flatten lets you call each plot in the figure by a number
axes = axes.flatten()

#'599,599' --> '599','599'


# Graph read depth values as a histogram
axes[0].hist([DP_list], color="red", bins=400)

start, end = axes[0].get_xlim()
#axes[0].xaxis.set_ticks(np.arange(start, end, 10))

axes[0].set_ylabel("Number of variants")
axes[0].set_xlabel("Read depth")
axes[0].set_yscale("log")
axes[0].set_title("Read depth distribution across each variant")
       


####################################################
 
#the genotype quality distribution

axes[1].hist(Gene_qualities, color="blue", bins=400)

start, end = axes[1].get_xlim()
axes[1].xaxis.set_ticks(np.arange(start, end, 1000))
axes[1].set(xlim=(0,10489))

axes[1].set_ylabel("Number of variants")
axes[1].set_yscale("log")
axes[1].set_xlabel("Genotype quality (Phred score)")
axes[1].set_title("Genotype quality distribution")

####################################################


# the allele frequency spectrum of your identified variants
axes[2].hist(allele_freq, color="green", bins=100)

axes[2].set_ylabel("Number of variants")
axes[2].set_xlabel("Allele frequency")
axes[2].set_title("Distribution of allele frequencies among identified variants")



downstream_gene_variant=[]
frameshift=[]
master_list = []
conservative_inframe_insertion=[]
downstream_gene_variant = []
conservative_inframe_deletion =[]
disruptive_inframe_deletion = []

initiator_codon_variant=[]
intron=[]
missense=[]
noncoding_transcript_exon=[]
splice_deceptor =[]
splice_donor =[]
splice_region=[]
start_lost=[]
stop_gained=[]
stop_lost=[]
stop_retained=[]
synonymous=[]
upstream_gene_variant=[]
disruptive_inframe_insertion=[]


with open(sys.argv[1]) as f:
    for i,line in enumerate(f):
        if line.startswith('#'):
            continue
        else:
            columns = line.rstrip('\r\n').split("\t")
            annot = columns[0].split(";")
            for part in annot:
                if part.startswith("ANN="):
                    subset = part.strip("\n").split("|")
                    #print(subset)
            for item in subset:
                master_list.append(item)
#print(master_list)
for lolo in master_list:
    if lolo == "conservative_inframe_insertion":
       conservative_inframe_insertion.append(lolo)
    if lolo == "downstream_gene_variant":
       downstream_gene_variant.append(lolo)
    if lolo == "conservative_inframe_deletion":
       conservative_inframe_deletion.append(lolo)
    if lolo == "conservative_inframe_insertion":
       conservative_inframe_insertion.append(lolo)
    if lolo == "disruptive_inframe_deletion":
       disruptive_inframe_deletion.append(lolo)
    if lolo == "intron":
       intron.append(lolo)
    if lolo == "frameshift":
       frameshift.append(lolo)
    if lolo == "initiator_codon_variant":
       initiator_codon_variant.append(lolo)
    if lolo == "missense":
       missense.append(lolo)
    if lolo == "noncoding_transcript_exon":
       noncoding_transcript_exon.append(lolo)
    if lolo == "splice_deceptor":
       splice_deceptor.append(lolo)
    if lolo == "splice_donor":
       splice_donor.append(lolo)
    if lolo == "splice_region":
       splice_region.append(lolo)
    if lolo == "start_lost":
       start_lost.append(lolo)
    if lolo == "stop_gained":
       stop_gained.append(lolo)
    if lolo == "stop_lost":
       stop_lost.append(lolo)
    if lolo == "stop_retained":
       stop_retained.append(lolo)
    if lolo == "synonymous":
        synonymous.append(lolo)
    if lolo == "upstream_gene_variant":
       upstream_gene_variant.append(lolo)
    if lolo == "disruptive_inframe_insertion":
        disruptive_inframe_insertion.append(lolo)
    if lolo == "downstream_gene_variant":
        downstream_gene_variant.append(lolo)
       


labels = ["conservative_inframe_deletion", "conservative_inframe_insertion", "disruptive_inframe_deletion", "disruptive_inframe_insertion", "downtream_gene_variant", "frameshift", "initiator_codon_variant", "intron", "missense", "noncoding_transcript_exon", "splice_deceptor", "splice_donor", "splice_region", "start_lost", "stop_gained", "stop_lost", "stop_retained", "synonymous", "upstream_gene_variant"]
data = [len(conservative_inframe_deletion), len(conservative_inframe_insertion), len(disruptive_inframe_deletion), len(disruptive_inframe_insertion), len(downstream_gene_variant), len(frameshift), len(initiator_codon_variant), len(intron), len(missense), len(noncoding_transcript_exon), len(splice_deceptor), len(splice_donor), len(splice_region), len(start_lost), len(stop_gained), len(stop_lost), len(stop_retained), len(synonymous), len(upstream_gene_variant)]
#
#                         if lolo in annotation:
#                             annotation[lolo]+=1
#                         else:
#                             continue
#
#
#print(annotation)
axes[3].bar(labels, data)
axes[3].set_ylabel("Log Occurences")
axes[3].set_yscale('log')
axes[3].set_xlabel("Type of variant")
axes[3].set_title("Predicted effects")

# plt.bar(*zip(*annotation.items()))
plt.xticks(rotation=90, size=5)
plt.savefig("all_four.png")
#


#############
#with old file, here is old code:

#annotation = {
#     "downstream_gene_variant":0,
#     "conservative_inframe_deletion":0,
#     "conservative_inframe_insertion":0,
#     "disruptive_inframe_deletion":0,
#     "disruptive_inframe_insertion":0,
#     "downstream_gene_variant":0,
#     "frameshift":0,
#     "initiator_codon_variant":0,
#     "intron":0,
#     "missense":0,
#     "noncoding_transcript_exon":0,
#     "splice_deceptor":0,
#     "splice_donor":0,
#     "splice_region":0,
#     "start_lost":0,
#     "stop_gained":0,
#     "stop_lost":0,
#     "stop_retained":0,
#     "synonymous":0
# }
# annotation ={}
#
# master_list = []
# final_list=[]
# with open(sys.argv[1]) as f:
#     for i,line in enumerate(f):
#         if line.startswith('#'):
#             continue
#         else:
#             columns = line.rstrip('\r\n').split("\t")
#             annot = columns[7].split(";")
#             for part in annot:
#                 if part.startswith("ANN="):
#                     subset = part.strip("\n").split("|")
#                     #print(subset)
#                     for item in subset:
#                         master_list.append(item)
#                     print(master_list)
                    # for lolo in master_list:
#                         if lolo == "conservative_inframe_insertion":
#                             final_list.append(lolo)
#                         print(final_list)
