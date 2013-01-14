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

#####################################################
# plot user movements to map
#####################################################
from read_in import fq_data as rd
from visualize.by_calling_fq import map_usr_movements as a
#####################################################


_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')

################################################################    
#    # this is general function call
################################################################
#    C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#    data = defaultdict(int)
#    for c in C:
#        data = rd.read_in_file(c, data)
#        #data = rd.read_in_whole_file(c, data)

###############################################################
    # this is specific for interevent time calls data
##############################################################
    C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    #C = ['A']
    
#    ##########################################################
#    # for all interevent times
#    ###########################################################  
#    data = defaultdict(int)
#    for i in range(500001):
#        data[i] = {'last_call_time': 0, 'interevent_times': defaultdict(int)}
#      
#    for c in C:
#        data = rd.read_in_file(c, data)
#        #data = rd.read_in_whole_file(c, data)

#    #######################################################################
#    # this is list of users you want to analyze -- uncomment for single usr
#    #######################################################################
#    data = defaultdict(int)
#    usr = 248907
#    start = 0
#
#    for c in C:
#        # this is for single user
#        data, start = rd.read_in_single_usr(c, data, usr, start)
#    #print data

    #######################################################################
    # this is for NX graph for a SUBPREF overall user movements
    #######################################################################
    # here we read in dictionary of users into usrs_list, so that we only read for them from the files.
    for subpref in range(1,256):
        data = nx.DiGraph()
        usrs_list = defaultdict(int)
        usrs_list = rd.read_in_subpref_users(subpref)
        print "Read users " + str(subpref)
        # this we need to follow properly each user, for his next locations (afterall he had to move somehow from last calling loc to the next)
        # CAUTION  for LATER WORK: here is that probably later I should limit this to some shorter time between calls,
        # otherwise he could have really moved in some other unknown routes
        # even more appealing -- we want to know daily commute patterns from home. This might confirm my HOMES found to be correct :)
        last_usr_loc = defaultdict(int)
        for usr in usrs_list:
            last_usr_loc[usr] = 0
        for c in C:
            # this is for single subpref, through all 10 weeks
            data = rd.read_in_file_2graph_multiple_users(c, data, usrs_list, last_usr_loc)
        # plot summary movements for all users
        a.plot_movements(data, subpref)
        print "Done " + str(subpref)

    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            reload(a)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            
#            #####################################################
#            # save usr homes data to files
#            #####################################################
#            a.data_to_files(data)
#            #a.data_to_files(data, True)
#            #####################################################

#            #####################################################
#            # save usr homes data to files
#            #####################################################
#            a.data_to_files(data)
#            #a.data_to_files(data, True)
#            #####################################################
            #####################################################
            # save single usr homes data to files
            #####################################################
            #a.plot_movements(data, subpref)
            #a.data_to_files(data, True)
            #####################################################
            print 'OVER'
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()