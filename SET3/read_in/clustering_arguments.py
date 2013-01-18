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

## we take in user calls on weekdays between 7pm and 5am as being from HOME and count number of such calls
## for each user plus the number of calls on the weekends in general
#def read_in_file(c, home_calls, last_usr_loc_n_dist, center_mass_coord, usr_traj):
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
#                if center_mass_coord[usr][0] <> 0 and center_mass_coord[usr][1] <> 0:
#                    L = home_calls[usr][0] + home_calls[usr][1]
#                    usr_traj[usr][L-1][0] = subpref_pos_data[subpref][0]
#                    usr_traj[usr][L-1][1] = subpref_pos_data[subpref][1]
#                    new_cm = find_mid_point(center_mass_coord[usr][0],center_mass_coord[usr][1],subpref_pos_data[subpref][0], subpref_pos_data[subpref][1])
#                    center_mass_coord[usr][0] = new_cm[0]
#                    center_mass_coord[usr][1] = new_cm[1]
#                    radius_gyr = 0
#                    for i in range(L): 
#                        d = find_distance(usr_traj[usr][i][0], usr_traj[usr][i][1], center_mass_coord[usr][0], center_mass_coord[usr][1])
#                        radius_gyr += d*d
#                    radius_gyr = math.sqrt(radius_gyr / L)
#                    rg[usr] = radius_gyr  
#                else:
#                    center_mass_coord[usr][0] = subpref_pos_data[subpref][0]
#                    center_mass_coord[usr][1] = subpref_pos_data[subpref][1]
#    
#    print i            
#    return home_calls, last_usr_loc_n_dist, center_mass_coord, usr_traj, rg


# this is for the first set of parameters
def read_in_file(c, home_calls, last_usr_loc_n_dist):
    
    i = 0
    usr_home = read_in_user_home_subprefs()
    subpref_dist = find_subpref_distance()
    subpref_pos_data = read_in_subpref_pos_file()
    rg = defaultdict(int)
    
    
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

# this is for the second set of parameters
def read_in_file2(c, home_calls, last_usr_loc_n_dist):
    
    i = 0
    usr_home = read_in_user_home_subprefs()
    subpref_dist = find_subpref_distance()
    subpref_pos_data = read_in_subpref_pos_file()
    rg = defaultdict(int)
    
    
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
    ant_dist_data = n.zeros((1239,1239), dtype=n.int)
    
    R = 6371
    
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

def find_mid_point(lon1, lat1, lon2, lat2):
    
    mid_point_data = n.zeros((2))
             
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    
    Bx= math.cos(lat2) * math.cos(dLon)    
    By = math.cos(lat2) * math.sin(dLon)
    lat3 = math.atan2(math.sin(lat1)+math.sin(lat2), math.sqrt( (math.cos(lat1)+Bx)*(math.cos(lat1)+Bx) + By*By))
    lon3 = lon1 + math.atan2(By, math.cos(lat1) + Bx)
    
    mid_point_data[0] = lon3
    mid_point_data[1] = lat3            
                
    return mid_point_data  


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


#mid = find_mid_point(-4.014445,5.42112,-4.014445,5.42112)
#print mid[0]
#print mid[1]