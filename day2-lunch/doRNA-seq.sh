#!/bin/bash

GENOME=/Users/cmdb/data/genomes/BDGP6.fa
ANNOTATION=/Users/cmdb/data/genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp /Users/cmdb/data/rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p $THREADS -x BDGP6 -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -@ $THREADS $SAMPLE.sam > $SAMPLE.bam
  samtools index $SAMPLE.bam
  stringtie $SAMPLE.bam -e -B -p $THREADS -G $ANNOTATION -o $SAMPLE.stringtie
done	