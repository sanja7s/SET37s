'''
Created on Jan 14, 2013

@author: sscepano
'''
'''
Created on Nov 21, 2012

@author: sscepano
'''

# This one serves for reading in data in full --- for finding number of users, user homes etc
from collections import defaultdict
from multiprocessing import Pool
import logging
import numpy as n
import traceback
import networkx as nx

######################################################
## save usr homes data to files
######################################################
#from read_in import home_data as rd
#from analyze.by_night_home import save_usr_home as a
######################################################

######################################################
## save usr number of calls and fq data to files
######################################################
#from read_in import fq_data as rd
#from analyze.by_calling_fq import save_usr_fq as a
######################################################

######################################################
## save usr interevent call and fq data to files
######################################################
#from read_in import interevent_call_times_data as rd
#from analyze.by_interevent_call_times import save_interevent_call_times as a
######################################################

######################################################
## save fq data to NX graph
######################################################
#from read_in import fq_data as rd
#from analyze.by_calling_fq import save_graph_data as a
#######################################################

######################################################
## plot user movements to map
######################################################
#from read_in import fq_data as rd
#from visualize.by_calling_fq import map_usr_movements as a
#from analyze.by_calling_fq import save_graph_data as s
######################################################

######################################################
## for CLUSTERING data
######################################################
#from read_in import clustering_arguments as rd
##from visualize.by_calling_fq import map_usr_movements as a
#from analyze.by_calling_fq import save_clustering_args as s
######################################################

######################################################
## for num visited subpref data
######################################################
#from read_in import num_visited_subpref_data as rd
##from visualize.by_calling_fq import map_usr_movements as a
#from analyze.by_num_visited_subprefs import save_num_visited_subprefs as s
######################################################

######################################################
## for CLUSTERING data: radius gyration
######################################################
#from read_in import clustering_arguments as rd
##from visualize.by_calling_fq import map_usr_movements as a
#from analyze.by_calling_fq import save_clustering_args as s
######################################################

#####################################################
# for CLUSTERING data: radius gyration
#####################################################
from read_in import call_timing_data as rd
#from visualize.by_calling_fq import map_usr_movements as a
from analyze.by_call_timing import data_to_file as s
#####################################################


_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')

################################################################
# # this is general function call
################################################################
# C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# data = defaultdict(int)
# for c in C:
# data = rd.read_in_file(c, data)
# #data = rd.read_in_whole_file(c, data)

###############################################################
    # this is specific for interevent time calls data
##############################################################
    C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    #C = ['A']
    
# ##########################################################
# # for all interevent times
# ###########################################################
# data = defaultdict(int)
# for i in range(500001):
# data[i] = {'last_call_time': 0, 'interevent_times': defaultdict(int)}
#
# for c in C:
# data = rd.read_in_file(c, data)
# #data = rd.read_in_whole_file(c, data)

# #######################################################################
# # this is list of users you want to analyze -- uncomment for single usr
# #######################################################################
# data = defaultdict(int)
# usr = 248907
# start = 0
#
# for c in C:
# # this is for single user
# data, start = rd.read_in_single_usr(c, data, usr, start)
# #print data

# #######################################################################
# # this is for NX graph for a SUBPREF overall user movements
# #######################################################################
# # here we read in dictionary of users into usrs_list, so that we only read for them from the files.
# for subpref in range(1,256):
# data = nx.DiGraph()
# usrs_list = defaultdict(int)
# usrs_list = rd.read_in_subpref_users(subpref)
# print "Read users " + str(subpref)
# # this we need to follow properly each user, for his next locations (afterall he had to move somehow from last calling loc to the next)
# # CAUTION for LATER WORK: here is that probably later I should limit this to some shorter time between calls,
# # otherwise he could have really moved in some other unknown routes
# # even more appealing -- we want to know daily commute patterns from home. This might confirm my HOMES found to be correct :)
# last_usr_loc = defaultdict(int)
# for usr in usrs_list:
# last_usr_loc[usr] = 0
# for c in C:
# # this is for single subpref, through all 10 weeks
# data = rd.read_in_file_2graph_multiple_users(c, data, usrs_list, last_usr_loc)
# # plot summary movements for all users
# a.plot_movements(data, subpref)
# print "Done " + str(subpref)

# #######################################################################
# # this is to analyze commuting or returning patterns during one day for a single user
# #######################################################################
# data = nx.DiGraph()
# usr = 1177
#
# for c in C:
# # this is for single user
# data = rd.read_in_commuting_patterns(c, data, usr)
# #print data
#
# ####################################################
# # this is for analyzing commuting patterns
# ####################################################
# a.plot_commuting_patterns(data, usr)
# s.graph2_file2(data, usr)
    ####################################################
    
# #######################################################################
# # this is to analyze commuting or returning patterns during one day for a whole set of subpref users user
# #######################################################################
# for subpref in range(1,256):
# data = nx.DiGraph()
# #subpref = 200
# usrs_list = rd.read_in_subpref_users(subpref)
# print len(usrs_list)
#
# for c in C:
# # this is for single user
# usrs_list = rd.read_in_subpref_users(subpref)
# data = rd.read_in_commuting_patterns_multiple_users(c, data, usrs_list)
#
# ####################################################
# # this is for analyzing commuting patterns
# ####################################################
# a.plot_commuting_patterns(data, subpref, is_subpref=True)
# s.graph2_file_subpref2(data, subpref)


# #######################################################################
# # this is to analyze commuting or returning patterns during one day for a single user
# #######################################################################
# data = nx.DiGraph()
# usr = 1177
#
# for c in C:
# # this is for single user
# data = rd.read_in_commuting_patterns(c, data, usr)
# #print data
#    #######################################################################
#    # this is to analyze commuting or returning patterns during one day for a whole set of subpref users user
#    #######################################################################
#    for subpref in range(1,256):
#        data = nx.DiGraph()
#        #subpref = 200
#        usrs_list = rd.read_in_subpref_users(subpref)
#        print len(usrs_list)
#    
#        for c in C:
#            # this is for single user
#            usrs_list = rd.read_in_subpref_users(subpref)
#            data = rd.read_in_commuting_patterns_multiple_users(c, data, usrs_list)
#    
#        ####################################################
#        # this is for analyzing commuting patterns
#        ####################################################
#        a.plot_commuting_patterns(data, subpref, is_subpref=True)
#        s.graph2_file_subpref2(data, subpref)


#    #######################################################################
#    # this is to analyze commuting or returning patterns during one day for a single user
#    #######################################################################
#    data = nx.DiGraph()
#    usr = 1177
#    
#    for c in C:
#        # this is for single user
#        data = rd.read_in_commuting_patterns(c, data, usr)
#    #print data



#    #######################################################################
#    # this is for finding CLUSTERING arguments we want
#    #######################################################################
#    # here we save number of calls made from home and number of calls made outside of home subpref for each user
#    home_calls = n.zeros((500001,2), dtype=n.int)
#    # here we save last location (helps calculating) and user traveled distance
#    last_usr_loc_n_dist = n.zeros((500001,2), dtype=n.int)
#    # here we save helping center of mass coordinates, for each user two coordinates
#    #center_mass_coord = n.zeros((256,2))
#    #usr_traj = n.zeros((500001,137357,2))
#    #usr_traj = n.zeros((256,13116,2))
#    
#
## for c in C:
## home_calls, last_usr_loc_n_dist, center_mass_coord, usr_traj, radius_gyr = rd.read_in_file(c, home_calls, last_usr_loc_n_dist, center_mass_coord, usr_traj)
#
##    for c in C:
##        home_calls, last_usr_loc_n_dist, center_mass_coord, usr_traj, radius_gyr = rd.read_in_file(c, home_calls, last_usr_loc_n_dist, center_mass_coord, usr_traj)
#
#
#    for c in C:
#        home_calls, last_usr_loc_n_dist = rd.read_in_file(c, home_calls, last_usr_loc_n_dist)
#    data = n.zeros((500001,256),dtype=n.int)
#
#    for c in C:
#        data = rd.read_in_file(c, data)

#    #######################################################################
#    # this is for finding CLUSTERING arguments we want: radius gyration
#    #######################################################################
#    usr_traj = defaultdict(int)
#    for usr in range(500001):
#        usr_traj[usr] = defaultdict(int)
#    for c in C:
#        usr_traj = rd.read_in_file0(c, usr_traj)
#    #######################################################################
#    # this is for finding CLUSTERING argument trajectory length that I wanted to improve!!!
#    #######################################################################
#    # here we save last location (helps calculating) and user traveled distance
#    last_usr_loc_n_dist = n.zeros((500001,2), dtype=n.float)
#    
#    for c in C:
#        last_usr_loc_n_dist = rd.read_in_file2(c, last_usr_loc_n_dist)
#
#
#    _log.info("Data loaded.")
#    while True:
#        raw_input("Press enter to start a process cycle:\n")
#        try:
#            reload(s)
#        except NameError:
#            _log.error("Could not reload the module.")
#        try:
#            # THIS THE FUNCTION YOU ARE TESTING


#    #######################################################################
#    # this is for finding CLUSTERING argument timing of calls in the subpref (not calculated only from the home users!!!)
#    #######################################################################
#    # here we save last location (helps calculating) and user traveled distance
#    data = defaultdict(int)
#    for subpref in range(256):
#        data[subpref] = defaultdict(int)
#    
#    for c in C:
#        data = rd.read_in_file(c, data)

    #######################################################################
    # this is for finding CLUSTERING argument timing of calls in the subpref (not calculated only from the home users!!!)
    #######################################################################
    # here we save last location (helps calculating) and user traveled distance
    week_data = defaultdict(int)
    weekend_data = defaultdict(int)
    for subpref in range(256):
        week_data[subpref] = defaultdict(int)
        weekend_data[subpref] = defaultdict(int)
    
    for c in C:
        week_data, weekend_data = rd.read_in_file_weekends(c, week_data, weekend_data)


    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            reload(s)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            
# #####################################################
# # save usr homes data to files
# #####################################################
# a.data_to_files(data)
# #a.data_to_files(data, True)
# #####################################################

# #####################################################
# # save usr homes data to files
# #####################################################
# a.data_to_files(data)
# #a.data_to_files(data, True)
# #####################################################
            #####################################################
            # save single usr homes data to files
            #####################################################
            #a.plot_movements(data, subpref)
            #a.data_to_files(data, True)
            #####################################################

# print 'OVER'
## ####################################################
## # this is for analyzing commuting patterns
## ####################################################
## a.plot_commuting_patterns(data, usr)
## s.graph2_file2(data, usr)
## ####################################################

#            print 'OVER'
##            ####################################################
##            # this is for analyzing commuting patterns
##            ####################################################
##            a.plot_commuting_patterns(data, usr)
##            s.graph2_file2(data, usr)
##            ####################################################


#            ####################################################
#            # this is for CLUSTERING algorithms
#            ####################################################
#            #s.save_data_to_matrix(home_calls, last_usr_loc_n_dist, radius_gyr)
#            data = s.calculate_radius_gyration_from_data(usr_traj)
#            s.data_to_file0(data)
#            
#            ####################################################

            ####################################################
            # this is for CLUSTERING algorithm TRAJ length
            ####################################################
            #s.save_data_to_matrix(home_calls, last_usr_loc_n_dist, radius_gyr)
            s.save_data_to_file(weekend_data) 
            #s.save_data_to_file(weekend_data) 
            
            ####################################################
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()