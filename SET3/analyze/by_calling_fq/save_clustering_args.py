'''
Created on Jan 16, 2013

@author: sscepano
'''
def save_data_to_matrix(home_calls, last_usr_loc_n_dist, radius_gyr):
    
    file_o = "/home/sscepano/D4D res/allstuff/CLUSTERING/ALL_files_clustering_args.tsv"
    f_o = open(file_o, "w")
    
    for usr in range(500001):
        f_o.write(str(usr) + '\t' + str(home_calls[usr][0]) + '\t' + str(home_calls[usr][1]) + '\t' + str(last_usr_loc_n_dist[usr][1]) + '\t' +  str(radius_gyr[usr]) + '\n')
      
    return