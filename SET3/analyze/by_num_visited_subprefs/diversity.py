'''
Created on Feb 20, 2013

@author: sscepano
'''
import math
from collections import defaultdict
from read_in import fq_data as rd

# we have for each user ids of visited subprefs and number of visits in the data dictionary
def calculate_diversity(data):
 
################################################## 
###    this part calculates user diversity
##################################################
    div = defaultdict(int)
    
    # for each user calculate diversity using formula from Finger on the Pulse
    for usr in range(500001):
        # total places visits
        S = float(sum(data[usr].values()))
        
        if S > 0:
            for subpref in data[usr].iterkeys():
                if subpref <> -1:
                    # frequency of visits to this place
                    v = data[usr][subpref] / float(S)
                    div[usr] -= v * math.log(v)
            div[usr] = div[usr] / math.log(S)
            
        
#    file_name = "/home/sscepano/D4D res/allstuff/diversity of travel/usr_diversity_index.tsv"
#    f = open(file_name,"w")
#    
#    for usr in range(1,500001):
#        f.write(str(usr) + '\t' + str(div[usr]) + '\n')
#        
#    print file_name
#    f.close()

################################################################
### subpref diversity
################################################################
    num_subpref_usrs = rd.read_in_subpref_num_users()
    div_subpref = defaultdict(int)
    for subpref in range(1,256):
        # for places where we have users
        if num_subpref_usrs[subpref] > 0:
            # read ids of those users
            subpref_usrs = rd.read_in_subpref_users(subpref)
            # for each user check if he belongs here (not the fastest way but still fine)
            for usr in range(500001):
                # total places visits
                if subpref_usrs[usr] == 1:
                    # we sum all users diversity indexes and then avg
                    div_subpref[subpref] += div[usr]
            div_subpref[subpref] = div_subpref[subpref] / float(num_subpref_usrs[subpref])
                
    file_name2 = "/home/sscepano/D4D res/allstuff/diversity of travel/subpref_diversity_index.tsv"
    f2 = open(file_name2,"w")
        
    for subpref in range(1,256):
        if num_subpref_usrs[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(div_subpref[subpref]) + '\n')
            
    print file_name2
    f2.close()
            
    return div, div_subpref