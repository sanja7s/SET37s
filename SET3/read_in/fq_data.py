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
                    