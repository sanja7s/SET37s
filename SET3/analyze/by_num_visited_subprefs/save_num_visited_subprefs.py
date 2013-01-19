'''
Created on Jan 17, 2013

@author: sscepano
'''
from collections import defaultdict
from read_in import fq_data as rd
import numpy as n

def data_to_files(data):
    
    num_visited_subprefs_per_subpref = defaultdict(int)
    num_visited_subprefs_per_subpref_scaled = defaultdict(int)
    usr_home = rd.read_in_user_home_subprefs()
    num_usrs = rd.read_in_subpref_num_users()
    
    for usr in range(500001):
        num_visited_subprefs_per_subpref[usr_home[usr]] += data[usr].sum()
        
    for subpref in range(256):
        if num_usrs[subpref] <> 0:
            num_visited_subprefs_per_subpref_scaled[subpref] = num_visited_subprefs_per_subpref[subpref] / num_usrs[subpref]
        
        
        
    file1 = "/home/sscepano/D4D res/allstuff/distr of num of visited subprefs/1/usr_num_visited_subprefs.tsv"
    file2 = "/home/sscepano/D4D res/allstuff/distr of num of visited subprefs/1/subpref_summed_num_visited_subprefs.tsv"
    file3 = "/home/sscepano/D4D res/allstuff/distr of num of visited subprefs/1/subpref_scaled_num_visited_subprefs.tsv"
    
    f1 = open(file1, "w")
    f2 = open(file2, "w")
    f3 = open(file3, "w")
    
    for usr in range(500001):
        f1.write(str(usr) + '\t' + str(n.sum(data[usr])) + '\n')
        
    for subpref in range(256):
        if num_visited_subprefs_per_subpref[subpref] <> 0:
            f2.write(str(subpref) + '\t' + str(num_visited_subprefs_per_subpref[subpref]) + '\n')
        
    for subpref in range(256):
        if num_visited_subprefs_per_subpref_scaled[subpref] <> 0:
            f3.write(str(subpref) + '\t' + str(num_visited_subprefs_per_subpref_scaled[subpref]) + '\n')
        
        
    print file1
    print file2
    print file3
    
    return