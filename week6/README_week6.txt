Chip-seq
- look for regions of the genome that are associated with proteins.
Best controls:
Input DNA (after fragmentation but before IP, you basically do not pulldown)
Need to have very specific antibody

Generally do not do paired ends.

MACS2 (model based analysis of chip seq data)

Computes distances between modes and determines the location (center) of the DNABP.

P-Value: The probability of observing that test statistic or greater that value if the null hypothesis is true.

Controlling for multiple testing:
Family wise error rate is too stringent

with FDR,
you accept higher false positives, but at least you get more true positives.
q-value is the minimum FDR at which the test is significant. You can rank based on confidence.

q-value package in R will assign q-values given a list of pv-alues

**Use a control sample to compute the FDR!**

Mouse chromosome 19, map reads onto it. Make conda env for macs 2; 


 bowtie2-build -f chr19.fa index
 
 bowtie2 -f -x dbname -U <reads> -S <outputfile.sam>
 bowtie2 -x index -U CTCF_ER4.fastq -S CTCF_ER4.sam
 
 bowtie2 -x index -U CTCF_G1E.fastq -S CTCF_G1E.sam
 bowtie2 -x index -U input_ER4.fastq -S input_ER4.sam
 bowtie2 -x index -U input_G1E.fastq -S input_G1E.sam
 
 
 samtools view -Sb input.sam > output.bam
 
 samtools view -Sb CTCF_ER4.sam > CTCF_ER4.bam
 samtools view -Sb CTCF_G1E.sam > CTCF_G1E.bam
 samtools view -Sb input_ER4.sam > input_ER4.bam
 samtools view -Sb input_G1E.sam > input_G1E.bam

 samtools sort input.bam > output_sorted.bam
 
 samtools sort CTCF_ER4.bam > CTCF_ER4_sorted.bam
 samtools sort CTCF_G1E.bam > CTCF_G1E_sorted.bam
 samtools sort input_ER4.bam > input_ER4_sorted.bam
 samtools sort input_G1E.bam > input_G1E_sorted.bam
 
 macs2 callpeak -f BAM -t CTCF_G1E.bam -c input_G1E.bam -g 62309240 --outdir callpeaks_output_GIE
 
 
 macs2 callpeak -f BAM -t CTCF_G1E_sorted.bam -c input_G1E_sorted.bam -g 62309240 --outdir callpeaks_output_G1E
 macs2 callpeak -f BAM -t CTCF_ER4_sorted.bam -c input_ER4_sorted.bam -g 62309240 --outdir callpeaks_output_ER4
 
 
 #awk '{print $1,$2,$3,$4}' NA_peaks.narrowPeak > /Users/cmdb/qbb2019-answers/week6/simplifed_ER4
 a#wk '{print $1,$2,$3,$4}' NA_peaks.narrowPeak > /Users/cmdb/qbb2019-answers/week6/simplifed_G1E
 
 cut -f 1,2,3,4,5,6 NA_peaks.narrowPeak > /Users/cmdb/qbb2019-answers/week6/mini_ER4
 
 cut -f 1,2,3,4,5,6 NA_peaks.narrowPeak > /Users/cmdb/qbb2019-answers/week6/mini_G1E
 
 bedtools intersect -v -a mini_ER4 -b mini_G1E > differential_binding_CTCF (sites in ER4 and not found in G1E)
 
 bedtools intersect -v -a mini_G1E -b mini_ER4 > differential_binding_CTCF_2 (sites in G1E and not found in ER4)
 
 
 Feature overlap:
 
 bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b mini_ER4 > overlap_ER4
 
 bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b mini_G1E > overlap_G1E
 
 
 
 
 