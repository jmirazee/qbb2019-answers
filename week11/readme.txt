scRNA seq exploration:

-dataset comes from 10x genomics

Makup of bead:
-has a unique barcode that is the same for all strands on the bead
-UMI, unique molecular identifier that is unique for each strand
-then poly dT to capture individual RNA strands.

Even though lose beads, you keep reads with the UMI and barcode

Since 3' end is sequenced, but very hard to capture all isoforms.

Steps:
- align the read 2 sequence 

- tabulate by cell barcode and by UMI
UMI can allow us to collapse pcr duplication (there should be one unique UMI)

4^10 possible combinations of barcodes

UMI 4^16, but have less than that becuase of increased hamming distance

SC suffers from 'dropout', low number of reads. 

Secondary analysis:
-QC, filtering
-normalization

dimension reduction
clustering (unsupervised)
cluster annotation 

trajectory inference (try to say which cell types derived from others (maybe see where exhaustion came from))

differential expression
velocity analysis ()


Recall: unsupervised learning:
****Tsne and clustering are not the same;; never do clustering in Tsne space!

When PCA fails: what the underlying dimensions of the data is non-linear. Need to do manifold learning:

The flaw in t-SNE is that it is very bad in global structure (does not preserve ). The size and global orientation means nothing.


t-SNE is a stochastic method: setting the perplexity parameter is an art.

UMAP: Uniform manifold approximation and projection:
major assumption: relies on original ability to approximate manifold. 

Distance between clusters in UMAP is more meaningful than t-SNE.



