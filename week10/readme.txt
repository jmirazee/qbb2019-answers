CLustering:

----Hierarchical Agglomerative clustering-----
Will build a tree, and then by genes, combine into list based on similarity of expression

How to quanitfy similarities:
You can do Euclinean distance sqrt(a^2 + b^2)
Squared euclidian = c^2
Manhattan is the vertical and horizontal distances a + b. 


When you compare the distances of two genes, in order to compare it to another gene:
- Complete(Max)
-Single (min)
-Average

Decisions to make:
-How is distance being calculated (start with Euclidean)
-Choose linkage type (average is pretty good)




-----K-means clustering-----

Two random points assigned, and then data is split in half by two points.  The group of points have an average taken and then the cluster is re-assigned (look at PPT)

___
Gene ontology
Fisher's exact test

Can use panther to do these calculations

Differential expression
Log fold change of 50 --> 


For the assignment:

Use HAC by:
1 - cell type
2 - by gene




