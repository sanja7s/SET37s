'''
Created on Jan 7, 2013

@author: sscepano
'''
from os.path import isfile, join
from collections import defaultdict
import networkx as nx
from datetime import datetime, date

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


#def read_in_subprefs():
#
#    D4DPath = "/home/sscepano/DATA SET7S/D4D"
#    file7s = "SUBPREF_POS_LONLAT.TSV"
#    f = open(join(D4DPath,file7s), 'r')
#    
#    aG = nx.DiGraph()
#    
#    for line in f:
#        sid, slon, slat = line.split('\t')
#        aid = int(sid)
#        alon = float(slon)
#        alat = float(slat[:-1])
#        aG.add_node(aid, lon = alon, lat = alat)
#        
#    return aG

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


def read_in_file_2graph_multiple_users(c, G, usrs_list, last_usr_loc):
    
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
                if usr in usrs_list:
                    subpref = int(subpref)
                    if last_usr_loc[usr] == 0:
                        last_usr_loc[usr] = subpref
                        continue
                    i = i + 1
                    old_subpref = last_usr_loc[usr]
                    if G.has_edge(old_subpref, subpref):
                        G[old_subpref][subpref]['weight'] += 1
                    else:
                        G.add_edge(old_subpref, subpref, weight = 1)
                    last_usr_loc[usr] = subpref
        
    
    print i            
    return G

def read_in_subpref_avg_fq():
    
    subpref_avg_fq = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/subpref/Subpref_avg_calling_fq.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, avg_fq = line.split('\t')
        subpref =  int(subpref)
        avg_fq = float(avg_fq)
        subpref_avg_fq[subpref] = avg_fq
        
        
    return subpref_avg_fq

def read_in_gs1():
    
    subpref_gs1 = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/res/2/pca_kmeans_gs1.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, gs1 = line.split('\t')
        subpref =  int(subpref)
        gs1 = float(gs1)
        subpref_gs1[subpref] = gs1
        
    return subpref_gs1

def read_in_subpref_num_places():
    
    subpref_avg_pl = defaultdict(int)
    
    file_name = "/home/sscepano/D4D res/allstuff/distr of num of visited subprefs/1/subpref_scaled_num_visited_subprefs.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, avg_pl = line.split('\t')
        subpref =  int(subpref)
        avg_pl = int(avg_pl)
        subpref_avg_pl[subpref] = avg_pl       
        
    return subpref_avg_pl

def read_in_subpref_num_users():
    
    subpref_num_usr = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes/Num_of_users_per_home_subpref.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, num_usr = line.split('\t')
        subpref =  int(subpref[:-1])
        num_usr = int(num_usr)
        subpref_num_usr[subpref] = num_usr
             
    return subpref_num_usr        



def read_in_BACK_traj_only():
    
    subpref_traj = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/read_in_BACK_traj_only.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, traj = line.split('\t')
        subpref =  int(subpref)
        traj = int(traj)
        subpref_traj[subpref] = traj
             
    return subpref_traj    

def read_in_BACK_num_of_visits_outisde_only():
    
    subpref_avg_num_vis = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/read_in_BACK_num_outisde_visits_only.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, num_vis = line.split('\t')
        subpref =  int(subpref)
        num_vis = int(num_vis)
        subpref_avg_num_vis[subpref] = num_vis
             
    return subpref_avg_num_vis    


def read_in_commuting_patterns(c, G, usr_chosen):
    
    count_total_daily_patterns = 0
    usr_loc_today = defaultdict(int)
    usr_loc_today[usr_chosen] = []
    current_day = date.today() 
    found_chosen = False
    
    usr_home_subprefs = read_in_user_home_subprefs()
    usr_home = usr_home_subprefs[usr_chosen]
    count_home_matches = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                if usr == usr_chosen:
                    found_chosen = True
                    call_time = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                    subpref = int(subpref)
                    # if we are just starting
                    if current_day == date.today():
                        current_day = call_time.date()
                        usr_loc_today[usr] = [subpref]
                    else:
                        # if read in a different day from the one so far, lets finish it with the previous one
                        if current_day <> call_time.date():
                            e = len(usr_loc_today[usr])
                            found_pattern = False
                            for end in range(e-1, 1, -1):
                                last_loc = usr_loc_today[usr][end]
                                for i in range(end-2):
                                    if last_loc == usr_loc_today[usr][i]:
                                        found_pattern = True
                                        count_total_daily_patterns += 1
                                        if last_loc == usr_home:
                                            count_home_matches += 1
                                        k = 0
                                        while k < end-1:
                                            first_subpref = usr_loc_today[usr][k]
                                            second_subpref = usr_loc_today[usr][k+1]
                                            if G.has_edge(first_subpref, second_subpref):
                                                G[first_subpref][second_subpref]['weight'] += 1
                                            else:
                                                G.add_edge(first_subpref, second_subpref, weight = 1)
                                            print 'check'
                                            k += 1
                                        break
                                if found_pattern:
                                    break
                            usr_loc_today[usr] = [subpref]
                            current_day = call_time.date()
                        else:
                            last_index =len(usr_loc_today[usr])-1
                            if usr_loc_today[usr][last_index] <> subpref:
                                usr_loc_today[usr].append(subpref)
                else:
                    if found_chosen == True:
                        print ("Total patterns found ", count_total_daily_patterns)
                        print ("Home matches found ", count_home_matches)
                        return G   
                        
                    
def read_in_commuting_patterns_multiple_users(c, G, usr_list):
    
    # here we save # of all patterns found
    count_total_daily_patterns = 0
    # here we save all subprefs recorded for a user today
    usr_loc_today = defaultdict(int)
    current_day = defaultdict(int)
    # we assign empty arrays to our chosen users at start
    for usr in usr_list:
        usr_loc_today[usr] = []
        # we take today for some check as no day will match in the dataset
        current_day[usr] = date.today() 
    # to check when we go to a new user and if we were on a chosen user to delete it from users so we know
    old_usr = 0
    
    # dict with home for each user
    usr_home_subprefs = read_in_user_home_subprefs()
    # here we count how many of patters found are from home back to home
    count_home_matches = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                # if no users are given we can go out
                # also if we empty our users list means we found all users
                if len(usr_list) == 0:
                        print ("Total patterns found ", count_total_daily_patterns)
                        print ("Home matches found ", count_home_matches)  
                        return G
                # here we delete previous user if for him we had finished processing data
                if old_usr <> 0 and usr <> old_usr:
                    if usr_list[old_usr] == 1:
                        del usr_list[old_usr]
                # just in case delete accidentally assigned keys -- as with default dict, every check to a key assigns zero value
                if usr_list[usr] == 0:
                    del usr_list[usr]
                # and then we do the processing if the user is from our list
                else:
                    # it will become next old_usr
                    old_usr = usr
                    call_time = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                    subpref = int(subpref)
                    # if we are just starting with this user
                    if current_day[usr] == date.today():
                        current_day[usr] = call_time.date()
                        usr_loc_today[usr] = [subpref]
                    else:
                        # if read in a different day from the one so far, lets finish it with the previous one
                        if current_day[usr] <> call_time.date():
                            e = len(usr_loc_today[usr])
                            found_pattern = False
                            for end in range(e-1, 1, -1):
                                last_loc = usr_loc_today[usr][end]
                                for i in range(end-2):
                                    if last_loc == usr_loc_today[usr][i]:
                                        found_pattern = True
                                        count_total_daily_patterns += 1
                                        if last_loc == usr_home_subprefs[usr]:
                                            count_home_matches += 1
                                        k = 0
                                        while k < end-1:
                                            first_subpref = usr_loc_today[usr][k]
                                            second_subpref = usr_loc_today[usr][k+1]
                                            if G.has_edge(first_subpref, second_subpref):
                                                G[first_subpref][second_subpref]['weight'] += 1
                                            else:
                                                G.add_edge(first_subpref, second_subpref, weight = 1)
                                            #print 'check'
                                            k += 1
                                        break
                                if found_pattern:
                                    break
                            usr_loc_today[usr] = [subpref]
                            current_day[usr] = call_time.date()
                        else:
                            last_index =len(usr_loc_today[usr])-1
                            if usr_loc_today[usr][last_index] <> subpref:
                                usr_loc_today[usr].append(subpref)

                        
    print ("Total patterns found ", count_total_daily_patterns)
    print ("Home matches found ", count_home_matches)                    
    return G                      
                   
                   
                   
def read_in_commuting_patterns_all_subprefs(c, G):
    
    # here we save # of all patterns found
    count_total_daily_patterns = 0
    # here we save all subprefs recorded for a user today
    usr_loc_today = defaultdict(int)
    # helping array
    current_day = defaultdict(int)
    # we assign empty arrays to our chosen users at start
    for usr in range(500001):
        usr_loc_today[usr] = []
        current_day[usr] = date.today() 
    
    # in this matrix we will save all users who made the commuting path in this week
    # later will function run_weekly_check() count all users who took the path 3 times at least
    # and only then increase the commuting edges weight
    weekly_patterns = defaultdict()
    for subpref in range(256):
        weekly_patterns[subpref] = defaultdict()
        for subpref2 in range(256):
            weekly_patterns[subpref][subpref2] = defaultdict(int)
    
    # dict with home for each user
    usr_home_subprefs = read_in_user_home_subprefs()
    # here we count how many of patters found are from home back to home
    count_home_matches = 0
    
    weekly_check = True
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    #file_name = "100Klines.txt"
    #file_name= "usr50000.csv"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref)
                
                if subpref == -1:
                    #print "skip -1"
                    continue
                
                call_time = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
#                print current_day[usr]
#                print call_time.date()
                        
                # if read in a different day from the one so far, lets finish with the previous one
                if current_day[usr] <> call_time.date():
                    print current_day[usr]
                    # this finds possible commuting today for the user usr
                    e = len(usr_loc_today[usr])
                    print "e " + str(e)
                    print usr_loc_today[usr]
                    found_pattern = False
                    for end in range(e-1, 1, -1):
                        last_loc = usr_loc_today[usr][end]
                        print "Last loc " + str(last_loc)
                        for i in range(end-1):
                            print "\t" + "loc check i " + str(i) + " " + str(usr_loc_today[usr][i])
                            if last_loc == usr_loc_today[usr][i]:
                                found_pattern = True
                                count_total_daily_patterns += 1
                                if last_loc == usr_home_subprefs[usr]:
                                    count_home_matches += 1
                                k = 0
                                while k < end-1:
                                    first_subpref = usr_loc_today[usr][k]
                                    second_subpref = usr_loc_today[usr][k+1]
                                    weekly_patterns[first_subpref][second_subpref][usr] += 1
                                    k += 1
                                break
                            if found_pattern:
                                break
                    usr_loc_today[usr] = [subpref]
                    current_day[usr] = call_time.date()
                else:
                    last_index =len(usr_loc_today[usr])-1
                    if usr_loc_today[usr][last_index] <> subpref:
                        usr_loc_today[usr].append(subpref)
                
                # here we do the check for the week
                if c == 'A' and call_time.date() >= datetime.strptime('2011-12-08', '%Y-%m-%d').date() and weekly_check:
                    weekly_check = False
                    #print weekly_patterns[60]
                    G = run_weekly_check(G, weekly_patterns)
                    weekly_patterns = defaultdict()
                    for subpref in range(256):
                        weekly_patterns[subpref] = defaultdict()
                        for subpref2 in range(256):
                            weekly_patterns[subpref][subpref2] = defaultdict(int)

                        
    print ("Total patterns found ", count_total_daily_patterns)
    print ("Home matches found ", count_home_matches)     
    
    # I think here we will do the second weekly check for the 2weeks period
    G = run_weekly_check(G, weekly_patterns)
                   
    return G      


def run_weekly_check(G, weekly_patterns):
    #print "Weekly check"
    for subpref1 in weekly_patterns.iterkeys():
        for subpref2 in weekly_patterns[subpref1].iterkeys():
            for usr in weekly_patterns[subpref1][subpref2].iterkeys():
                if weekly_patterns[subpref1][subpref2][usr] > 3:
                    if G.has_edge(subpref1, subpref2):
                        G[subpref1][subpref2]['weight'] += 1
                    else:
                        G.add_edge(subpref1, subpref2, weight = 1)

    return G                