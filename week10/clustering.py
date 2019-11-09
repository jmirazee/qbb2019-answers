#!/usr/bin/env python3
import numpy as np
import sys
#
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
#
# gene_array = np.random.rand(10, 12)
# ax = sns.heatmap(gene_array, linewidth=0.5)
# plt.show()
# #
# listo = []
# f = open(sys.argv[1])
# locations = []
# for line in f:
#    if line.startswith("gene"):
#        continue
#    col = line.rstrip("\n").split()
#    listo.append(col[0])
#
# #print(listo)
# # #

#
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage,leaves_list

#
#
#
# #%matplotlib inline
#
data = pd.read_csv(sys.argv[1], sep = "\t", header = 0, index_col = "gene")




#Methods ‘centroid’, ‘median’ and ‘ward’ 
linkage_1 = linkage(data, method = 'average')

#transposed_linkage_1_4_dendro = linkage_1.transpose()

leaves_list_1 = leaves_list(linkage_1)
#pass Z to leaves list

#iloc
new_data = data.iloc[leaves_list_1]

transposed_new_data = new_data.transpose()

linkage_2 = linkage(transposed_new_data, method = 'average')
leaves_list_2 = leaves_list(linkage_2)
finish_last_data = transposed_new_data.iloc[leaves_list_2]

final_transposed = finish_last_data.transpose()
#print(finish_last_data)

sns.heatmap(final_transposed)
plt.show()


#Z = linkage(data, 'single')
fig = plt.figure(figsize=(5, 3))

plt.xlabel('Cell Types')

plt.title('Dendrogram')
plt.grid(True)

#plt.xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue', 'test'))
#
# label_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
# ax1 = dendrogram(linkage_2, labels = label_list)
#CFU      poly       unk       int       mys       mid

#Adcy6          0.139492  1.436242  1.530206  3.014137  2.957060  4.271844

label_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
labels = np.array(label_list)
sort_label = labels[leaves_list_2]
ax1 = dendrogram(linkage_2, labels = sort_label)
plt.show()


#`````````````````````` Now k means clustering

cfu = data["CFU"].values
poly = data["poly"].values




#X, y = cfu,poly

#
# #Reshape your data either using array.reshape(-1, 1) if your data has a single feature or
# #array.reshape(1, -1) if it contains a single sample.
# plt.scatter(X[:,0], X[:,1])
# kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
# pred_y = kmeans.fit_predict(X)
# plt.scatter(X[:,0], X[:,1])
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
# plt.show()
#
#
#
#
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(X)
# y_kmeans = kmeans.predict(X)
# plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
# plt.show()

#
#
#
#
# from scipy.cluster.vq import vq, kmeans, whiten
# test = kmeans(cfu,poly)
from sklearn.cluster import KMeans
from pandas import DataFrame

Data = {'x':cfu,
        'y': poly
       }
  
df = DataFrame(Data,columns=['x','y'])
#print (df)

kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_
#print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("CFU")
plt.ylabel("poly")
plt.title('K-means')
plt.show()


#kmeans = KMeans(n_clusters=5).fit(data)
cluster_map = pd.DataFrame()
cluster_map['data_index'] = df.index.values
cluster_map['cluster'] = kmeans.labels_
cluster_map[cluster_map.cluster == 5]

print(cluster_map)

# gene_list = data['gene']
# #
# # final_list = []
# # for item in gene_list:
# #     final_list.append(gene_list)
#
#
# #print(final_list)
# #
# # for item in data[0]:
# #     gene_list.append(item)
# # print(gene_list)
#

#Index= ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
#Cols = ['CFU','poly','unk','int','mys','mid']
#df = DataFrame(data, index=listo, columns=Cols)


# unk = data["unk"].values
# poly = data["poly"].values
#
# into = data["int"].values
# mid = data["mid"].values


from scipy import stats

diff_exp_high = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) >= 2
diff_exp_low = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) <= 0.5

diff_exp_genes = data[diff_exp_high | diff_exp_low]
#print(diff_exp_genes)
for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    # print(gene_name, stats.ttest_rel(sample1, sample2).pvalue)
    pval = stats.ttest_rel(sample1, sample2).pvalue
    if pval <= 0.05:
        print(gene_name, pval)



labels = list(kmeans.labels_)
genes = list(data.index.values)

goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]

related_genes = []
for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)

print(related_genes)

with open('list_of_genes.txt', 'w') as f:
    for item in related_genes:
        f.write("%s," % item)
        
            
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #print(diff_exp_genes)        


# from scipy import stats
# for gene_name, row in diff_exp_genes.iterrows():
#     sample1 = [row['CFU'], row['unk']]
#     sample2 = [row['poly'], row['int']]
#     print(gene_name, stats.ttest_ind(sample1, sample2).pvalue)


  
#test = data['']


# stats.ttest_rel(rvs1,rvs3)


# from scipy import stats
# num_1 = ((data['poly'] + data['unk'])/2).to_list()
# num_2 = ((data['mid'] + data['int']/2)).to_list()
# zipped = zip(num_1,num_2)
#
#
# full_list = []
# for item in zipped:
#     print(item)
#     full_list.appendstats.ttest_rel(item)
#
# print(full_list)




