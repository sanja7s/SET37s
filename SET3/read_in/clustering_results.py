'''
Created on Jan 18, 2013

@author: sscepano
'''
from collections import defaultdict

def read_in_subpref_assigned_3clusters():
    
    subpref_cluster = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/1/5args_kmeans_3clusters.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster3 = line.split('\t')
        subpref =  int(subpref)
        cluster3 = int(cluster3)
        subpref_cluster[subpref] = cluster3
             
    return subpref_cluster   

def read_in_subpref_assigned_2clusters():
    
    subpref_cluster = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/1/5args_kmeans_2clusters.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster2 = line.split('\t')
        subpref =  int(subpref)
        cluster2 = int(cluster2)

        subpref_cluster[subpref] = cluster2
             
    return subpref_cluster   

def read_in_subpref_assigned_4clusters():
    
    subpref_cluster = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/1/5args_kmeans_4clusters.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster2 = line.split('\t')
        subpref =  int(subpref)
        cluster2 = int(cluster2)

        subpref_cluster[subpref] = cluster2
             
    return subpref_cluster   


def read_in_subpref_assigned_5clusters():
    
    subpref_cluster = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/1/5args_kmeans_5clusters.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster2 = line.split('\t')
        subpref =  int(subpref)
        cluster2 = int(cluster2)

        subpref_cluster[subpref] = cluster2
             
    return subpref_cluster   

def read_in_subpref_assigned_6clusters():
    
    subpref_cluster = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/1/5args_kmeans_6clusters.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster2 = line.split('\t')
        subpref =  int(subpref)
        cluster2 = int(cluster2)

        subpref_cluster[subpref] = cluster2
             
    return subpref_cluster   


def read_in_subpref_assigned_7clusters():
    
    subpref_cluster = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/1/5args_kmeans_7clusters.csv"
    f = open(file_name,'r')
    
    for line in f:
        subpref, cluster2 = line.split('\t')
        subpref =  int(subpref)
        cluster2 = int(cluster2)

        subpref_cluster[subpref] = cluster2
             
    return subpref_cluster   