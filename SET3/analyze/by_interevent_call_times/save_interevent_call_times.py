'''
Created on Jan 9, 2013

@author: sscepano
'''

from collections import defaultdict 

def data_to_files(interval):

    ########################################################################################################  
    # save statistics for all users in one total file
    ########################################################################################################
    file_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/Intervals_per_user_total.tsv"
    f = open(file_name,"w")

    interval_total = defaultdict(int)

    for usr in interval.iterkeys():
        for it in interval[usr]['interevent_times'].iterkeys():
            interval_total[it] += interval[usr]['interevent_times'][it]
            
    for it in interval_total.iterkeys():
        f.write(str(it) + '\t' + str(interval_total[it]) + '\n')
        

###################################################################################################
#   # save statistics for a couple of random users just in case
###################################################################################################
    #random_users = [777, 20120, 51300, 117711, 12345]
    #random_users = [7771, 201201, 51301, 111, 5, 78900]
    random_users = [71, 301221, 451301, 7891, 555, 180900]

    for usr in random_users:
        
        file_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/Intervals_per_user_" + str(usr) + ".tsv"
        f = open(file_name,"w")

        interval_total = defaultdict(int)

        for it in interval[usr]['interevent_times'].iterkeys():
            interval_total[it] += interval[usr]['interevent_times'][it]
            
        for it in interval_total.iterkeys():
            f.write(str(it) + '\t' + str(interval_total[it]) + '\n')

    #########################################################################################################            
    # save statistics for user groups based on subprefrences 
    # first read in subpref users
    ########################################################################################################
    subpref_file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes/Subprefs_and_their_users.tsv"
    f_subpref = open(subpref_file_name,"r")
    
    subpref_usrs = {}        
    for line in f_subpref:
        line_elems = line.split('\t')
        subpref = int(line_elems[0][:-1])
        # we skip -1 as we don't know 'where' is this subpref
        if subpref <> -1:
            subpref_usrs.keys().append(subpref)
            subpref_usrs[subpref] = []
            for i in range (1, len(line_elems)):
                usr = int(line_elems[i])
                subpref_usrs[subpref].append(usr)
    
    # now for each subpref save one interval or interevent file                        
    for subpref in subpref_usrs.iterkeys():
        subpref_interval = defaultdict(int)
        for usr in subpref_usrs[subpref]:
            for it in interval[usr]['interevent_times'].iterkeys():
                subpref_interval[it] += interval[usr]['interevent_times'][it]
                    
        file_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/Intervals_per_subpref_" + str(subpref) + ".tsv"
        f = open(file_name,"w")
                      
        for it in subpref_interval.iterkeys():
            f.write(str(it) + '\t' + str(subpref_interval[it]) + '\n')    
    
    
    return


def single_usr_data_to_files(interval, usr):
    
    ########################################################################################################  
    # save SINGLE USER statistics for all users
    ########################################################################################################
    file_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/Single_user_date_intervals_" + str(usr) + ".tsv"
    f = open(file_name,"w")
    
    for date7s in interval.iterkeys():
        f.write(str(date7s) + '\t' + str(interval[date7s]) + '\n')
    
    return