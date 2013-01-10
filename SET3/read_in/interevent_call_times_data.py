'''
Created on Jan 9, 2013

@author: sscepano
'''

from os.path import isfile, join
from datetime import datetime

# for each of 500 000 users we find his own dictionary of interevent (between call) times: 
# {usr: {last_call_time, {interval: num_times_found}}}

def read_in_file(c, interval):
    
    i = 0
    old_usr = 0
    start = 0

    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                i = i + 1
                if usr == old_usr:   
                    end = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                    delt = end - start
                    delt = delt.days * 24 * 60 + delt.seconds / 60
                    interval[usr]['interevent_times'][delt] += 1
                    interval[usr]['last_call_time'] = end
                    start = end
                else: 
                    if interval[usr]['last_call_time'] == 0:
                        start = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                        interval[usr]['last_call_time'] = start
                        old_usr = usr
                    else:
                        start = interval[usr]['last_call_time']
                        end = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                        interval[usr]['last_call_time'] = end
                        delt = end - start
                        delt = delt.days * 24 * 60 + delt.seconds / 60
                        interval[usr]['interevent_times'][delt] += 1
             
    
    print i            
    return interval


