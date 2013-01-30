'''
Created on Jan 29, 2013

@author: sscepano
'''
from os.path import isfile, join
from collections import defaultdict
import networkx as nx
from datetime import datetime, date

def read_in_subpref_users(subpref):

    D4DPath = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes"
    file7s = "Subprefs_and_their_users.tsv"
    f = open(join(D4DPath,file7s), 'r')
    
    usrs_list = defaultdict(int)
    
    for line in f:
        line_elems = line.split('\t')
        subpref_id = line_elems[0]
        subpref_id = int(subpref_id[:-1])
        if subpref_id == subpref:
            for i in range(1, len(line_elems)):
                usr = int(line_elems[i])
                usrs_list[usr] = 1
            break
        
    return usrs_list

usrs_subpref = read_in_subpref_users(237)

print usrs_subpref

def read_in_user_home_subprefs():

    D4DPath = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes"
    file7s = "Users_and_their_homes.tsv"
    f = open(join(D4DPath,file7s), 'r')
    
    usrs_subprefs = defaultdict(int)
    
    for line in f:
        usr, subpref = line.split('\t')
        usr = int(usr)
        subpref = int(subpref)
        usrs_subprefs[usr] = subpref
      
    return usrs_subprefs