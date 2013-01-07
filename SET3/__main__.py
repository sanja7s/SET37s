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

######################################################
## save usr homes data to files
######################################################
#from read_in import home_data as rd
#from analyze.by_night_home import save_usr_home as a
######################################################

#####################################################
# save usr number of calls and fq data to files
#####################################################
from read_in import fq_data as rd
from analyze.by_calling_fq import save_usr_fq as a
#####################################################


_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')
    
    C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    data = defaultdict(int)
    for c in C:
        data = rd.read_in_file(c, data)
        #data = rd.read_in_whole_file(c, data)
    
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

            #####################################################
            # save usr homes data to files
            #####################################################
            a.data_to_files(data)
            #a.data_to_files(data, True)
            #####################################################
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()