#!/usr/bin/env python2

import sys
import numpy as np
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

#RNA is first argument
#Activity is the second argument

input1 = []

fieldstuple = ()

v1 = [0] * 7000
v2 = [0] *7000


#we are just doing the RNA one. Just because the assignment said to only submit that one.

rna_index = []
rna_expression = {}

for i, line in enumerate(f1):
    if i == 0: 
        continue 
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index1 = (int(fields[1]) - 5000000) / 5000
        rna_index.append(index1)
        rna_expression[index1] = float(fields[-2])
       # v1[index1] = f
 
activity_index = []
activity_value= {}
     
for i, line in enumerate(f2):
    if i == 0: 
        continue 
    fields = line.rstrip('\n').split('\t')
    if int(fields[1]) >= 5000000 and int(fields[1]) <= 40000000:
        index2 = (int(fields[1]) - 5000000) / 5000
        activity_index.append(index2)
        activity_value[index2] = float(fields[-2])
        #v2[index2] = 

        
        
        
import hifive
import numpy
hic = hifive.HiC('PROJECT_FNAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)        
        
print data
    
interaction_activity = {}

for index1 in rna_index:
    int_act = 0
    for index2 in activity_index:
        int_act += float(activity_value[index2])* data[index1][index2]
    interaction_activity[index1] = int_act

# data_subset = data[np.where(v2 > 0), :]
# sum_data_subset = np.sum(data_subset, axis=1)
# R = np.corrcoef(sum_data_subset, v2)[0, 1]
# # data_subset = data[rows, :][:, colums]

#
# print(R)

rna_expression_list = []
interaction_activity_list = []
for index in rna_index:
    rna_expression_list.append(float(rna_expression[index]))
    interaction_activity_list.append(interaction_activity[index])
rna_array = numpy.array(rna_expression_list)
interaction_activity_array = numpy.array(interaction_activity_list)
R_value = numpy.corrcoef(rna_array, interaction_activity_array)[0, 1]
#print "R coefficient =" , R_value


#print(v2)


#filter out every thing greater than 5 Mil and 40 Mil

