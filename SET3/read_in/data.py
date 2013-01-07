'''
Created on Jan 7, 2013

@author: sscepano
'''
from os.path import isfile, join
from datetime import date,timedelta
from collections import defaultdict

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
                subpref = subpref[:-1]
                data[usr] = data.get(usr, {})
                call_hour = int(call_time[11:13])
                call_date = date(int(call_time[:4]), int(call_time[5:7]), int(call_time[8:10]))
                #print(call_date)
                #print(call_date.weekday())
                if call_date.weekday() < 5:
                    if call_hour > 19 or call_hour <= 5:
                        try:
                            data[usr][subpref] += 1
                        except KeyError:
                            data[usr][subpref] = 1
                else:
                    try:
                        data[usr][subpref] += 1
                    except KeyError:
                        data[usr][subpref] = 1
    
    print i            
    return data

# Tested not used atm function
def read_in_file_multiprocessing(c):
    
    i = 0
    data = defaultdict(int)
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                subpref = subpref[:-1]
                data[usr] = data.get(usr, {})
                call_hour = int(call_time[11:13])
                call_date = date(int(call_time[:4]), int(call_time[5:7]), int(call_time[8:10]))
                #print(call_date)
                #print(call_date.weekday())
                if call_date.weekday() < 5:
                    if call_hour > 19 or call_hour <= 5:
                        try:
                            data[usr][subpref] += 1
                        except KeyError:
                            data[usr][subpref] = 1
                else:
                    try:
                        data[usr][subpref] += 1
                    except KeyError:
                        data[usr][subpref] = 1
    
    print i            
    return data

def read_in_whole_file(c, data):
    
    i = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                subpref = subpref[:-1]
                data[usr] = data.get(usr, {})
                try:
                    data[usr][subpref] += 1
                except KeyError:
                    data[usr][subpref] = 1
    
    print i            
    return data