'''
Created on Jan 7, 2013

@author: sscepano
'''
from os.path import isfile, join
from collections import defaultdict
import networkx as nx

# we take in user calls on weekdays between 7pm and 5am as being from HOME and count number of such calls
# for each user plus the number of calls on the weekends in general
def read_in_file(c, data):
    
    i = 0
    #data = defaultdict(int)
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                data[usr] += 1
    
    print i            
    return data


def read_in_subprefs():

    D4DPath = "/home/sscepano/DATA SET7S/D4D"
    file7s = "SUBPREF_POS_LONLAT.TSV"
    f = open(join(D4DPath,file7s), 'r')
    
    aG = nx.DiGraph()
    
    for line in f:
        sid, slon, slat = line.split('\t')
        aid = int(sid)
        alon = float(slon)
        alat = float(slat[:-1])
        aG.add_node(aid, lon = alon, lat = alat)
        
    return aG


def read_in_file_2graph(c, G, usr_chosen):
    
    
    old_subpref = 0
    i = 0
    #data = defaultdict(int)
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                if usr == usr_chosen:
                    i = i + 1
                    subpref = int(subpref)
                    if old_subpref <> 0:
                        if G.has_edge(old_subpref, subpref):
                            G[old_subpref][subpref]['weight'] += 1
                        else:
                            G.add_edge(old_subpref, subpref, weight = 1)
                        old_subpref = subpref
                    else:
                        old_subpref = subpref
    
    print i            
    return G