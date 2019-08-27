#Construct commands to analyze SRR072893 using fastqc, hisat2, samtools, and stringtie


#1 40,000 reads equals 10,000 lines
head -40000 SRR072893.fastq > SRR072893.10k.fastq

#B Generate a quality control report for the reads using FastQC
file:///Users/cmdb/qbb2019-answers/day2-lunch/SRR072893_fastqc.html

#C Map reads to BDGP6 using HISAT2
hisat2 -x BDGP6 -U SRR072893.10k.fastq -S SRR072893.sam

#D Convert .sam to a sorted .bam and index using SAMtools
samtools sort SRR072893.sam > SRR072893.bam
/Users/cmdb/qbb2019-answers/day2-lunch $ samtools index SRR072893.bam

#E Quantitate sorted .bam file using StringTie
StringTie SRR072893.bam -e -B -p 4 -G BDGP6.Ensembl.81.gtf -o SRR072893.stringtie



#3 Calculate how many alignments are on each chromosome for SRR072893
#this is output from stringTie

sort SRR072893.stringtie | cut -f 1 | uniq -c > SRR072893.number3

The slow way would be to do a for loop with python. 

This was a pretty fast way and I could not think of faster ways. Will do unconsciously though and will write it down if I think of faster way


#4 a. Summarize how many alignments fall into each category of "numbers of columns", save the results as SRR072893.columns, and submit to your repository

samtools view SRR072893.sam | awk '{print NF}' | sort | uniq -c > SRR072893.columns


#4 b. 
Column #12: YT:Z:UU
Column #13: YF:Z:NS
22 coluns: AS:i:-2	ZS:i:-6	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:5A34	YT:Z:UU	XS:A:+	NH:i:1

Each of these columns are different in that all the ones that only have YT:Z:UU and YF:Z:NS (containing only column #12, #13) do not have an alignment score (AS) that lines with 20,21,and 22 columns have. 

Column 21 adds ZS:i:-7 and column 22 adds XS:A:+