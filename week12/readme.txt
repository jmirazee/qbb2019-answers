Bisulfite seq:

Limitations: moved from 4 letter to 3 letter alphabet, therefroe less info content and harder to align.

- 

We will be using bizmark that aligns to reference genome as well as additional genomes that have already converted all Cs to Ts.

https://trace.ddbj.nig.ac.jp/DRASearch/submission?acc=SRA111995

fastq-dump -X 1000000 --split-files SRR1035454

fastq-dump -X 1000000 --split-files SRR1035452







/bismark/bismark_genome_preparation --path_to_aligner /Users/cmdb/miniconda3/pkgs/bowtie2-2.3.5-py36h5c9b4e4_0 --verbose chr19.fa


bismark --sam --genome chr19 -1 SRR1035452_1.fastq -2 SRR1035452_2.fastq

bismark --sam --genome chr19 -1 SRR1035454_1.fastq -2 SRR1035454_2.fastq



samtools sort SRR1035452_1_bismark_bt2_pe.bam -o sorted_SRR1035452_1_bismark_bt2_pe.bam

samtools sort SRR1035454_1_bismark_bt2_pe.bam -o sorted_SRR1035454_1_bismark_bt2_pe.bam



bismark_methylation_extractor --bedgraph --comprehensive SRR1035452_1_bismark_bt2_pe.bam
bismark_methylation_extractor --bedgraph --comprehensive SRR1035454_1_bismark_bt2_pe.bam