'''
Created on Jan 18, 2013

@author: sscepano
'''
from collections import defaultdict

def read_in_subpref_assigned_clusters():
    
    subpref_cluster = defaultdict(int)
    for i in range (256):
        subpref_cluster[i] = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/MATLAB_results_1_fq_dist_pcthome.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster3, cluster2 = line.split('\t')
        subpref =  int(subpref)
        cluster3 = int(cluster3)
        cluster2 = int(cluster2)
        subpref_cluster[subpref][1] = cluster3
        subpref_cluster[subpref][0] = cluster2
             
    return subpref_cluster   