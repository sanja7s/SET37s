'''
Created on Jan 16, 2013

@author: sscepano
'''
from os.path import isfile, join
from collections import defaultdict
import networkx as nx
from datetime import datetime, date
import math
import numpy as n

# this is to read in radius of gyration
# we need user trajectory in order to follow the visited places
# as radius gyration calculation at any moment needs whole list
# of so far visited places
def read_in_file0(c, usr_traj):
   
    i = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    #file_name = '100Klines.txt'
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref)
                # for each user we hold a dictionary with all the visited subprefs and the number of visits to each
                # this is done by increasing the number in the dict each time user visits the subpref
                usr_traj[usr][subpref] += 1 
    
    print i            
    return usr_traj


# we want avg traveled dist on daily basis
def read_in_file_avg_daily_traj(c, usr_traj, usr_day, usr_traj_today):
    
    subpref_dist = find_subpref_distance()
    i = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    #file_name = '100Klines.txt'
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref)
                call_time = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                call_day = call_time.date()
                
                if usr_day[usr][0] == call_day:
                    # for each user we hold a dictionary with all the visited subprefs and the number of visits to each
                    # this is done by increasing the number in the dict each time user visits the subpref
                    old_loc = usr_traj_today[usr][1]  
                    usr_traj_today[usr][0] += subpref_dist[old_loc,subpref]
                    usr_traj_today[usr][1] = subpref
                else:
                    usr_day[usr][1] += 1
                    usr_day[usr][0] = call_day
                    usr_traj[usr] += usr_traj_today[usr][0]
                    usr_traj_today[usr][1] = subpref
                    usr_traj_today[usr][0] = 0
    
    print i            
    return usr_traj, usr_day, usr_traj_today


# this is for the first set of parameters
# home calls, outside of home and total calls
# the total traveled distance by a user
def read_in_file(c, home_calls, last_usr_loc_n_dist):
    
    i = 0
    usr_home = read_in_user_home_subprefs()
    subpref_dist = find_subpref_distance()
    subpref_pos_data = read_in_subpref_pos_file()
    rg = defaultdict(int)
    
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    #file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    #file_name = '100Klines.txt'
    file_name = "usr50000.csv"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref)
                if usr_home[usr] == subpref:
                    home_calls[usr][0] += 1
                else: 
                    home_calls[usr][1] += 1
                if last_usr_loc_n_dist[usr][0] <> 0:
                    if subpref <> last_usr_loc_n_dist[usr][0]:
                        last_usr_loc_n_dist[usr][1] += subpref_dist[last_usr_loc_n_dist[usr][0]][subpref]
                else:
                    last_usr_loc_n_dist[usr][0] = subpref
             
    
    print i            
    return home_calls, last_usr_loc_n_dist


# this is an improved version with trajectory length -- I found a bug!!!
def read_in_file2(c, last_usr_loc_n_dist):
    
    i = 0
    subpref_dist = find_subpref_distance()
    
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    #file_name = '100Klines.txt'
    #file_name = "usr50000.csv"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref)
                if last_usr_loc_n_dist[usr][0] <> 0:
                    #print last_usr_loc_n_dist[usr][0]
                    if subpref <> last_usr_loc_n_dist[usr][0]:
                        last_usr_loc_n_dist[usr][1] += subpref_dist[last_usr_loc_n_dist[usr][0]][subpref]
                        last_usr_loc_n_dist[usr][0] = subpref
                else:
                    last_usr_loc_n_dist[usr][0] = subpref
             
    
    print i            
    return last_usr_loc_n_dist

## this is for the second set of parameters
#def read_in_file2(c, home_calls, last_usr_loc_n_dist):
#    
#    i = 0
#    usr_home = read_in_user_home_subprefs()
#    subpref_dist = find_subpref_distance()
#    subpref_pos_data = read_in_subpref_pos_file()
#    rg = defaultdict(int)
#    
#    
#    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
#    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
#    #file_name = '100Klines.txt'
#    f_path = join(D4D_path_SET3,file_name)
#    if isfile(f_path) and file_name != '.DS_Store':
#            file7s = open(f_path, 'r')
#            for line in file7s:
#                i = i + 1
#                usr, call_time, subpref = line.split('\t')
#                usr = int(usr)
#                subpref = int(subpref)
#                if usr_home[usr] == subpref:
#                    home_calls[usr][0] += 1
#                else: 
#                    home_calls[usr][1] += 1
#                if last_usr_loc_n_dist[usr][0] <> 0:
#                    if subpref <> last_usr_loc_n_dist[usr][0]:
#                        last_usr_loc_n_dist[usr][1] += subpref_dist[last_usr_loc_n_dist[usr][0]][subpref]
#                else:
#                    last_usr_loc_n_dist[usr][0] = subpref
#             
#    
#    print i            
#    return home_calls, last_usr_loc_n_dist

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


def find_subpref_distance():
    
    ant_pos_data = read_in_subpref_pos_file()   
    ant_dist_data = n.zeros((1239,1239), dtype=n.float)
    
    R = 6371
    file_name = "/home/sscepano/D4D res/allstuff/distances/subpref_distances_file.tsv"
    f = open(file_name,"w")
    
    for subpref1 in range(256):
        for subpref2 in range(256):
                lon1 = ant_pos_data[subpref1][0]
                lat1 = ant_pos_data[subpref1][1]
                lon2 = ant_pos_data[subpref2][0]
                lat2 = ant_pos_data[subpref2][1]
                
                dLat = math.radians(lat2-lat1)
                dLon = math.radians(lon2-lon1)
                lat1 = math.radians(lat1)
                lat2 = math.radians(lat2)
                a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                dist = R * c
                
                ant_dist_data[subpref1][subpref2] = dist
                f.write(str(subpref1) + '\t' + str(subpref2) + '\t' + str(dist) + '\n')
                               
    return ant_dist_data  



def find_distance(lon1, lat1, lon2, lat2):
   
    R = 6371
                
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = R * c
    
    return dist  



def find_subpref_mid_point():
    
    pos_data = read_in_subpref_pos_file()   
    mid_point_data = n.zeros((256,256))
    
    for subpref1 in range(256):
        for subpref2 in range(256):
                lon1 = pos_data[subpref1][0]
                lat1 = pos_data[subpref1][1]
                lon2 = pos_data[subpref2][0]
                lat2 = pos_data[subpref2][1]
                
                dLat = math.radians(lat2-lat1)
                dLon = math.radians(lon2-lon1)
                Bx= math.cos(lat2) * math.sin(dLon)
                By = math.cos(lat2) * math.sin(dLon)
                lat1 = math.radians(lat1)
                lat2 = math.radians(lat2)
                lat3 = math.atan2(math.sin(lat1)+math.sin(lat2), math.sqrt( (math.cos(lat1)+Bx)*(math.cos(lat1)+Bx) + By*By))
                lon3 = lon1 + math.atan2(By, math.cos(lat1) + Bx)
                
                mid_point_data[subpref1][subpref2][0] = lon3
                mid_point_data[subpref1][subpref2][1] = lat3
                
                
    return mid_point_data  

# this was a more general function for midpoint I found for lons and lats
def find_mid_point(lon, lat, w):
      
    X = defaultdict(float)
    Y = defaultdict(float)
    Z = defaultdict(float)
    
    for i in range(len(lon)):         
        lat[i] = math.radians(lat[i])
        lon[i] = math.radians(lon[i])
    
        X[i] = math.cos(lat[i])*math.cos(lon[i])
        Y[i] = math.cos(lat[i])*math.sin(lon[i])
        Z[i] = math.sin(lat[i])
        
    #W = float(len(lon))
    W = float(sum(w))
    #print W
    
    x = 0
    y = 0
    z = 0
        
#    x = sum(X) / W
#    print sum(X)
#    y = sum(Y) / W
#    z = sum(Z) / W

    for i in range(len(lon)):
        x += X[i] * w[i]
    
    for i in range(len(lon)):
        y += Y[i] * w[i]
        
    for i in range(len(lon)):
        z += Z[i] * w[i]
        
    x = x / W
    y = y / W
    z = z / W
    
    lon_mid = math.atan2(y,x)
    hyp = math.sqrt(x*x + y*y)
    lat_mid = math.atan2(z, hyp)
    
    lon_mid = math.degrees(lon_mid)
    lat_mid = math.degrees(lat_mid)
                
    return lon_mid, lat_mid  


# subpref positions
def read_in_subpref_pos_file():
    
    subpref_pos_data = n.zeros((256,2))
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D"
    file_name = "SUBPREF_POS_LONLAT.TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                subpref, lon, lat = line.split('\t')
                subpref = int(subpref)
                lon = float(lon)
                lat = float(lat)
                subpref_pos_data[subpref][0] = lon
                subpref_pos_data[subpref][1] = lat
                
    return subpref_pos_data

#w = [1095.75, 730.5, 365.25]
#lon = [-74.0059731, -87.6297982, -84.3879824]
#lat = [40.7143528, 41.8781136, 33.7489954]

#w = [1, 1]
#lon = [-74.0059731, -74.0059731]
#lat = [40.7143528, 40.7143528]
#mid_lon, mid_lat = find_mid_point(lon, lat, w)
#print mid_lon
#print mid_lat

#subpref_dist = find_subpref_distance()
#print subpref_dist[182][183]


# here we save last location (helps calculating) and user travelled distance
#last_usr_loc_n_dist = n.zeros((2), dtype=n.float)
#
#last_usr_loc_n_dist = read_in_file_test(last_usr_loc_n_dist)
#
#print last_usr_loc_n_dist[1]