'''
Created on Jan 30, 2013

@author: sscepano
'''
from os.path import isfile, join
from datetime import date,timedelta
from collections import defaultdict

def read_in_file(c, data):
    
    i = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                subpref = subpref[:-1]
                data[subpref] += 1 
    
    print i            
    return data