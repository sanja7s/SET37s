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

#####################################################
# save fq data to NX graph
#####################################################
from read_in import fq_data as rd
from analyze.by_calling_fq import save_graph_data as a
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
    #C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    C = ['A']
    
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
    # this is for NX graph for a SINGLE user movements
    #######################################################################
    data = nx.DiGraph()
    #data = rd.read_in_subprefs()
    usr = 777

    for c in C:
        # this is for single user
        data = rd.read_in_file_2graph(c, data, usr)
    #print data
    
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
            a.graph2_file(data, c, usr)
            #a.data_to_files(data, True)
            #####################################################
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()