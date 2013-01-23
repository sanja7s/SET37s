'''
Created on Jan 23, 2013

@author: sscepano
'''
from os.path import isfile, join
from datetime import date,timedelta
from collections import defaultdict

import fq_data as rd

# we do simple counting here for how many users who live in one subpref
# travel to each other subpref -- thus we just collect their overall dynamics
# averaged and for all subprefs and users
def read_in_file_2graph(c, G):
    
    i = 0
    usr_home = rd.read_in_user_home_subprefs()
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                i = i + 1
                subpref = int(subpref)
                if G.has_edge(usr_home[usr], subpref):
                    G[usr_home[usr]][subpref]['weight'] += 1
                else:
                    G.add_edge(usr_home[usr], subpref, weight = 1)
    
    print i            
    return G