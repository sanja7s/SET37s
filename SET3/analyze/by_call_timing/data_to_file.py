'''
Created on Jan 22, 2013

@author: sscepano
'''

from visualize.by_call_timing import plot_calls_per_hour as v 
from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY, MonthLocator
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2
import datetime
import matplotlib.dates as dt
from collections import defaultdict, OrderedDict
from matplotlib import pyplot as plt


from read_in import fq_data as rd

def save_data_to_file(data):
    
    num_users = rd.read_in_subpref_num_users()
    
    #print data[60]
    #subpref = 250
    
#    for subpref in range(256):
#        from_data_to_timeplot(data[subpref], subpref)
        
        
#    for subpref in range(256):
#        cum_data = get_cumulative_call_timing_data(data[subpref])
#        from_data_to_timeplot2(cum_data, subpref)   

#    wake_up_hour = defaultdict(int)
#    sleep_hour = defaultdict(int)
#
#    for subpref in range(256):
#        cum_data = get_cumulative_call_timing_data(data[subpref])
#        sleep_hour[subpref] = analyze_cum_calling_data2(cum_data)
#        wake_up_hour[subpref] = analyze_cum_calling_data1(cum_data)   
#        
#    file_name = "/home/sscepano/D4D res/allstuff/call timing/subpref_weekend_wake_up_sleep_hour.tsv"
#    f = open(file_name,"w")
#    
#    num_users = rd.read_in_subpref_num_users()
#    
#    for subpref in wake_up_hour.iterkeys():
#        if num_users[subpref] > 0:
#            f.write(str(subpref) + '\t' + str(wake_up_hour[subpref]) + '\t' + str(sleep_hour[subpref]) + '\n')

    
    pct_night_calls = defaultdict(float)

    for subpref in range(256):
        pct_night_calls[subpref] = pct_calls_at_night(data[subpref]) 
        
    file_name = "/home/sscepano/D4D res/allstuff/call timing/subpref_weekdend_pct_night_calls.tsv"
    f = open(file_name,"w")
    
    for subpref in pct_night_calls.iterkeys():
        if num_users[subpref] > 0:
            f.write(str(subpref) + '\t' + str(pct_night_calls[subpref]) + '\n')

#    for subpref in data.iterkeys():
#        file_name = "/home/sscepano/D4D res/allstuff/call timing/subpref all files/weekends/calls_per_hour_" + str(subpref) + ".tsv"
#        f = open(file_name, "w")
#        
#        for hr in data[subpref].iterkeys():
#            f.write(str(hr) + '\t' + str(data[subpref][hr]) + '\n')
#            
#        f.close()
    
    return

def analyze_cum_calling_data1(cum_data):
    
    for hr in range(24):
        if cum_data[hr] > 0.05:
            return hr
        
    return 24

def analyze_cum_calling_data2(cum_data):
    
    for hr in range(24):
        if cum_data[hr] > 0.95:
            return hr
        
    return 24

def pct_calls_at_night(data):
    
    tot_night_calls = 0
    
    for hr in [22,23,0,1,2]:
        tot_night_calls += data[hr]
        
    pct_night_calls = tot_night_calls / float(sum(data.items()))
    
#    print sum(data.items())
#    print tot_night_calls
        
    return pct_night_calls

def get_cumulative_call_timing_data(data):
    
    cum_data = defaultdict(float)
    cur_sum = 0
    
    for hr in data.iterkeys():
        cur_sum += data[hr]
        cum_data[hr] = cur_sum
        
    for hr in range(24):
        if cum_data[23] > 0:
            cum_data[hr] = cum_data[hr] / float(cum_data[23])
    
    return cum_data


def from_data_to_timeplot(data, subpref):
    
    val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for hr in data.iterkeys():
        val[hr] = data[hr]

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.step([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], val, '-')
    ax.axvspan(0, 5, color='yellow', alpha=0.5)
    ax.set_xlim(0,23)
    ax.set_xticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23))
    
    #show()

    figure_name = "/home/sscepano/D4D res/allstuff/call timing/reg/weekends/" + str(subpref) + "_subpref_weekend_24hour_calling_pattern.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return

def from_data_to_timeplot2(data, subpref):
    
    val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for hr in data.iterkeys():
        val[hr] = data[hr]

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.step([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], val, '-')
    ax.axvspan(0, 5, color='yellow', alpha=0.5)
    ax.set_xlim(0,23)
    ax.set_xticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23))
    
    #show()

    figure_name = "/home/sscepano/D4D res/allstuff/call timing/cum_scaled/weekends/subpref_weekend_24hour_calling_pattern_" + str(subpref) + ".png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return