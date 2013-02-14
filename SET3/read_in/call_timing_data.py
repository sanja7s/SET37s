'''
Created on Jan 22, 2013

@author: sscepano
'''
from os.path import isfile, join
from datetime import date,timedelta
from collections import defaultdict


#import fq_data as rd2
#usr_subpref = rd2.read_in_user_home_subprefs()

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
                call_hour = int(call_time[11:13])
                call_min = int(call_time[14:17][:-1])
                #print (call_hour, call_min)
                #print call_hour
                subpref = int(subpref)
                if subpref <> -1:
                    #print subpref
                    data[subpref][call_hour][call_min] += 1
  
    print i            
    return data


def read_in_file_weekends_min(c, week_data, weekend_data):
    
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
                call_hour = int(call_time[11:13])
                call_min = int(call_time[14:17][:-1])
                subpref = int(subpref)
                if subpref <> -1:
                    call_date = date(int(call_time[:4]), int(call_time[5:7]), int(call_time[8:10]))
                    if call_date.weekday() >= 5:
                        weekend_data[subpref][call_hour][call_min] += 1
                    else:
                        week_data[subpref][call_hour][call_min] += 1

    print i            
    return week_data, weekend_data



def read_in_file_weekdays(c, data):
    
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
                #call_hour = int(call_time[11:13])
                #print call_hour
                subpref = int(subpref)
                call_date = date(int(call_time[:4]), int(call_time[5:7]), int(call_time[8:10]))
                if subpref <> -1:
                    data[subpref][call_date.weekday()] += 1
                
  
    print i            
    return data