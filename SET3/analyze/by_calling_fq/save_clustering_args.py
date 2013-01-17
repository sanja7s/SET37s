'''
Created on Jan 16, 2013

@author: sscepano
'''
from read_in import fq_data as rd
from collections import defaultdict

#def save_data_to_matrix(home_calls, last_usr_loc_n_dist, radius_gyr):
#    
#    file_o = "/home/sscepano/D4D res/allstuff/CLUSTERING/ALL_files_clustering_args.tsv"
#    f_o = open(file_o, "w")
#    
#    for usr in range(500001):
#        f_o.write(str(usr) + '\t' + str(home_calls[usr][0]) + '\t' + str(home_calls[usr][1]) + '\t' + str(last_usr_loc_n_dist[usr][1]) + '\t' +  str(radius_gyr[usr]) + '\n')
#      
#    return

#def save_data_to_matrix(home_calls, last_usr_loc_n_dist):
#    
#    file_o = "/home/sscepano/D4D res/allstuff/CLUSTERING/ALL_files_clustering_args.tsv"
#    f_o = open(file_o, "w")
#    
#    for usr in range(500001):
#        f_o.write(str(usr) + '\t' + str(home_calls[usr][0]) + '\t' + str(home_calls[usr][1]) + '\t' + str(last_usr_loc_n_dist[usr][1]) + '\n')
#      
#    return

def save_data_to_matrix(home_calls, last_usr_loc_n_dist):
    
    usr_home = rd.read_in_user_home_subprefs()
    subpref_avg_fq = rd.read_in_subpref_avg_fq()
    
    subpref_calls = defaultdict(int)
    subpref_outside_calls = defaultdict(int)
    subpref_pct_inside_calls = defaultdict(int)
    subpref_total_traj = defaultdict(int)
    
    file_o = "/home/sscepano/D4D res/allstuff/CLUSTERING/ALL_SUBPREF_clustering_args_v2same.tsv"
    f_o = open(file_o, "w")
    
    for usr in range(500001):
        subpref_calls[usr_home[usr]] += home_calls[usr][0]
        subpref_outside_calls[usr_home[usr]] += home_calls[usr][1]
        subpref_total_traj[usr_home[usr]] += last_usr_loc_n_dist[usr][1]
        
    print len(subpref_outside_calls)    
    print len(subpref_calls)
    print len(subpref_total_traj)
    print len(subpref_avg_fq)
    
#    for usr_id in usr_home:
#        if usr_home[usr_id] == 0:
#            print usr_id
        
    for subpref_id in range(256):
        suma = float(subpref_calls[subpref_id] + subpref_outside_calls[subpref_id])
        if suma <> 0:
            subpref_pct_inside_calls[subpref_id] = subpref_calls[subpref_id] / suma   
        f_o.write(str(subpref_id) + '\t' + str(subpref_calls[subpref_id]) + '\t' + str(subpref_outside_calls[subpref_id]) + '\t' + \
                  str(subpref_pct_inside_calls[subpref_id]) + '\t' + str(subpref_total_traj[subpref_id]) + '\t' + str(subpref_avg_fq[subpref_id]) + '\n')
      
    return