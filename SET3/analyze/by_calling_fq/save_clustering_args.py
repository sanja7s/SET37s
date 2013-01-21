'''
Created on Jan 16, 2013

@author: sscepano
'''
from read_in import fq_data as rd
from read_in import clustering_arguments as rd0
from collections import defaultdict
import math

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
    subpref_num_usr = rd.read_in_subpref_num_users()
    
    subpref_calls = defaultdict(int)
    subpref_outside_calls = defaultdict(int)
    subpref_pct_inside_calls = defaultdict(int)
    subpref_total_traj = defaultdict(int)
    
    file_o = "/home/sscepano/D4D res/allstuff/CLUSTERING/ALL_SUBPREF_clustering_args.tsv"
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
        subpref_total_traj[subpref_id] = subpref_total_traj[subpref_id] / subpref_num_usr[subpref_id]
        f_o.write(str(subpref_id) + '\t' + str(subpref_calls[subpref_id]) + '\t' + str(subpref_outside_calls[subpref_id]) + '\t' + \
                  str(subpref_pct_inside_calls[subpref_id]) + '\t' + str(subpref_total_traj[subpref_id]) + '\t' + str(subpref_avg_fq[subpref_id]) + '\n')
      
    return

def data_to_file0(data):
    
    file = "/home/sscepano/D4D res/allstuff/CLUSTERING/usr_radius_gyration3.tsv"
    f = open(file, 'w')
    
    for usr in data.iterkeys():
        f.write(str(usr) + '\t' + str(data[usr]) + '\n')   
    
    return

def data_to_file2(data):
    
    file = "/home/sscepano/D4D res/allstuff/CLUSTERING/usr_traj_lengthALL2.tsv"
    f = open(file, 'w')
    
    for usr in range(500001):
        f.write(str(usr) + '\t' + str(data[usr][1]) + '\n')   
    
    return


# it is much more convenient to read in all user trajectories at once
# and then to calculate the gyration radius here
def calculate_radius_gyration_from_data(usr_traj):
    
    subpref_pos_data = rd0.read_in_subpref_pos_file()
    # we save result for each user here
    rg = defaultdict(int)
    
    # this is added after eureka hehe :)
    num_places = 0
    file_name = "/home/sscepano/D4D res/allstuff/distr of num of visited subprefs/1/2 check/save_num_places_visited.tsv"
    f = open(file_name, "w")
    
    # loop the users                
    for usr in usr_traj.iterkeys():
            # calculate total number of places visited per user (hehe, I can use this to verify what I calculated before for the number of visited places)
            num_places = 0
            L = 0
            for subpref in usr_traj[usr]:
                if usr_traj[usr][subpref] > 0:
                    L += usr_traj[usr][subpref]
                    num_places += 1
            #print L
            
            f.write(str(usr) + '\t' + str(num_places) + '\n')  
            
            # here we save lon/lat/weight data
            lon = []
            lat = []
            w = []
            # populate the arrays
            for subpref in range(256):
                if usr_traj[usr][subpref] > 0:
                    lon.append(subpref_pos_data[subpref][0])
                    lat.append(subpref_pos_data[subpref][1])
                    w.append(usr_traj[usr][subpref])
            
            # if we found any visited places, then we calculate midpoint for all of them
            # this is what Barabasi calls center of mass of trajectory      
            if len(lon) > 0:        
                center_mass_lon, center_mass_lat = rd0.find_mid_point(lon, lat, w)
                
            # we start with zero radius of gyration
            radius_gyr = 0.0
            
            # here we calculate the distances from the midpoint for all the traveled places for the user
            for subpref in range(256):
                if usr_traj[usr][subpref] > 0: 
                    # subtracting tow vectors and then squaring the difference should result in squared distance between them
                    d = rd0.find_distance(subpref_pos_data[subpref][0], subpref_pos_data[subpref][1], center_mass_lon, center_mass_lat)
                    ds = d*d
                    # this line I had inversed with the line above and it was not correct calculation
                    # we just here multiply by the number of times we found the user in this place
                    radius_gyr += ds * usr_traj[usr][subpref]
            
            # for users who were not traveling at all (?)        
            if L > 0:    
                radius_gyr = math.sqrt(radius_gyr / L)
                
            # assign this user's radius to output array    
            rg[usr] = radius_gyr  
    
    return rg

def recalculate_subpref_traj():
    
    total_traj = rd.read_in_BACK_traj_only()
    scaled_traj = defaultdict(float)
    num_usrs = rd.read_in_subpref_num_users()
    
    file_out = "/home/sscepano/D4D res/allstuff/CLUSTERING/traj_scaled.tsv"
    f = open(file_out, "w")
    
    for subpref in range(256):
        if num_usrs[subpref] <> 0:
            scaled_traj[subpref] = total_traj[subpref] / num_usrs[subpref]
            
            print scaled_traj[subpref]
            f.write(str(subpref) + '\t' + str(scaled_traj[subpref]) + '\n')
    
    return

def recalculate_num_visits_outside():
    
    total_visits = rd.read_in_BACK_num_of_visits_outisde_only()
    scaled_visits = defaultdict(float)
    num_usrs = rd.read_in_subpref_num_users()
    
    file_out = "/home/sscepano/D4D res/allstuff/CLUSTERING/num_outside_visits_scaled.tsv"
    f = open(file_out, "w")
    
    for subpref in range(256):
        if num_usrs[subpref] <> 0:
            scaled_visits[subpref] = total_visits[subpref] / num_usrs[subpref]
            
            print scaled_visits[subpref]
            f.write(str(subpref) + '\t' + str(scaled_visits[subpref]) + '\n')
    
    return

def calculate_rg_subpref_from_usr_file():
    
    usr_home = rd.read_in_user_home_subprefs()
    subpref_num_users = rd.read_in_subpref_num_users()
    
    subpref_rg = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Clustering/usr res/usr_radius_gyration.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        usr, rg = line.split('\t')
        usr =  int(usr)
        rg = float(rg)
        subpref_rg[usr_home[usr]] += rg
        
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            subpref_rg[subpref] = subpref_rg[subpref] / float(subpref_num_users[subpref])
        
    file_name2 = "/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/subpref_avg_rg.tsv"
    f2 = open(file_name2, 'w')
    
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(subpref_rg[subpref]) + '\n')
             
    return subpref_rg  

#recalculate_num_visits_outside()
#calculate_rg_subpref_from_usr_file()


def calculate_hc_subpref_from_usr_file():
    
    usr_home = rd.read_in_user_home_subprefs()
    subpref_num_users = rd.read_in_subpref_num_users()
    
    subpref_rg = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Clustering/usr res/usr_home_calls.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        usr, rg = line.split('\t')
        usr =  int(usr)
        rg = float(rg)
        subpref_rg[usr_home[usr]] += rg
        
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            subpref_rg[subpref] = subpref_rg[subpref] / float(subpref_num_users[subpref])
        
    file_name2 = "/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/subpref_avg_hc.tsv"
    f2 = open(file_name2, 'w')
    
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(subpref_rg[subpref]) + '\n')
             
    return subpref_rg  

#recalculate_num_visits_outside()
#calculate_hc_subpref_from_usr_file()


def calculate_oc_subpref_from_usr_file():
    
    usr_home = rd.read_in_user_home_subprefs()
    subpref_num_users = rd.read_in_subpref_num_users()
    
    subpref_rg = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Clustering/usr res/usr_outside_calls.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        usr, rg = line.split('\t')
        usr =  int(usr)
        rg = float(rg)
        subpref_rg[usr_home[usr]] += rg
        
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            subpref_rg[subpref] = subpref_rg[subpref] / float(subpref_num_users[subpref])
        
    file_name2 = "/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/subpref_avg_oc.tsv"
    f2 = open(file_name2, 'w')
    
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(subpref_rg[subpref]) + '\n')
             
    return subpref_rg  

#recalculate_num_visits_outside()
#calculate_oc_subpref_from_usr_file()


def calculate_traj_subpref_from_usr_file():
    
    usr_home = rd.read_in_user_home_subprefs()
    subpref_num_users = rd.read_in_subpref_num_users()
    
    subpref_rg = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Clustering/usr res/usr_traj_length.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        usr, rg = line.split('\t')
        usr =  int(usr)
        rg = float(rg)
        subpref_rg[usr_home[usr]] += rg
        
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            subpref_rg[subpref] = subpref_rg[subpref] / float(subpref_num_users[subpref])
        
    file_name2 = "/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/subpref_avg_traj.tsv"
    f2 = open(file_name2, 'w')
    
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(subpref_rg[subpref]) + '\n')
             
    return subpref_rg  

#recalculate_num_visits_outside()
#calculate_traj_subpref_from_usr_file()

def save_subpref_calling_fq():
    
    subpref_num_users = rd.read_in_subpref_num_users()
    subpref_fq = rd.read_in_subpref_avg_fq()
    
    file_name2 = "/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/subpref_avg_fq.tsv"
    f2 = open(file_name2, 'w')
    
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(subpref_fq[subpref]) + '\n')
             
    return subpref_fq   
    
#save_subpref_calling_fq()    


def calculate_fq_subpref_from_usr_file():
    
    usr_home = rd.read_in_user_home_subprefs()
    subpref_num_users = rd.read_in_subpref_num_users()
    
    subpref_fq = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/new results -- check the same/Users_and_their_calling_fq.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        usr, fq = line.split('\t')
        usr =  int(usr)
        fq = float(fq)
        subpref_fq[usr_home[usr]] += fq
        
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            subpref_fq[subpref] = subpref_fq[subpref] / float(subpref_num_users[subpref])
        
    file_name2 = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/subpref/Subpref_avg_calling_fq_check.tsv"
    f2 = open(file_name2, 'w')
    
    for subpref in range(256):
        if subpref_num_users[subpref] > 0:
            f2.write(str(subpref) + '\t' + str(subpref_fq[subpref]) + '\n')
             
    return subpref_fq

#calculate_fq_subpref_from_usr_file()