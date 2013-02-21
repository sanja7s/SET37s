'''
Created on Jan 22, 2013

@author: sscepano
'''

from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY, MonthLocator
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2
import datetime
import matplotlib.dates as dt
from collections import defaultdict, OrderedDict
from matplotlib import pyplot as plt

def plot_times7s(week_data, weekend_data):
    
#    total_calls = defaultdict(int)
#    
#    for subpref_id in range(1,255):
#        total_calls[subpref_id] = defaultdict(int)
#        for hr in range(24):
#            total_calls[subpref_id][hr] = defaultdict(int)
#            for minute in range(60):
#                total_calls[subpref_id][hr][minute] = week_data[subpref_id][hr][minute] + weekend_data[subpref_id][hr][minute]
                
#    file_name = "/home/sscepano/D4D res/allstuff/call timing/TOTAL_calls.tsv"
#    f = open(file_name, "w")
#    
#    for subpref_id in range(1,256):
#        for hr in range(24):
#            for minute in range(60):
#                f.write(str(subpref_id) + '\t' + str(total_calls[subpref_id]) + '\n')
#        
#    from_data_to_timeplot_min_all(total_calls)

#    file_name1 = "/home/sscepano/D4D res/allstuff/call timing/subpref_num_weekday_callsv2.tsv"
#    file_name2 = "/home/sscepano/D4D res/allstuff/call timing/subpref_num_weekend_callsv2.tsv"
#    file_name3 = "/home/sscepano/D4D res/allstuff/call timing/subpref_pct_weekend_callsv2.tsv"
#    
#    f1 = open(file_name1, "w")
#    f2 = open(file_name2, "w")
#    f3 = open(file_name3, "w")
#        
#    for subpref_id in range(1,255):
#        weekday_calls = 0
#        for hr in range(24):
#            for minute in week_data[subpref_id][hr].iterkeys():
#                weekday_calls += week_data[subpref_id][hr][minute]
#        f1.write(str(subpref_id) + '\t' + str(weekday_calls) + '\n')
#        weekdend_calls = 0
#        for hr in range(24):
#            for minute in weekend_data[subpref_id][hr].iterkeys():
#                weekdend_calls += weekend_data[subpref_id][hr][minute]
#        f2.write(str(subpref_id) + '\t' + str(weekdend_calls) + '\n')
#        if weekday_calls <> 0:
#            pct_calls = weekdend_calls/float(weekday_calls)
#        else: 
#            pct_calls = 0
#        f3.write(str(subpref_id) + '\t' + str(pct_calls) + '\n')


    #from_data_to_timeplot_min_all(week_data)
    
#    cum_data = get_cumulative_call_timing_data_min(data[60])
    
#    print cum_data
#    
#    print_cumulative_call_timing_data_min(cum_data)

#    total_cum1 = get_cumulative_call_timing_data_min_total(week_data)
#    total_cum2 = get_cumulative_call_timing_data_min_total(weekend_data)
#    
#    print analyze_cum_calling_data_min1(total_cum2)
#    print analyze_cum_calling_data_min2(total_cum2)

#    wake_up_min = defaultdict(int)
#    sleep_min = defaultdict(int)
#    pct30_min = defaultdict(int)
#    pct40_min = defaultdict(int)
#    pct50_min = defaultdict(int)
#    pct90_min = defaultdict(int)
    
#    cum_data = get_cumulative_call_timing_data_min(data[120])
#    wake_up_minc = analyze_cum_calling_data_min1(cum_data)
#    sleep_minc = analyze_cum_calling_data_min2(cum_data)

#    for subpref_id in range(1,256):
#        cum_data = get_cumulative_call_timing_data_min(week_data[subpref_id])
#        wake_up_min[subpref_id] = analyze_cum_calling_data_min1(cum_data)
#        sleep_min[subpref_id] = analyze_cum_calling_data_min2(cum_data)
#        pct30_min[subpref_id] = analyze_cum_calling_data_min30pct(cum_data)
#        pct40_min[subpref_id] = analyze_cum_calling_data_min40pct(cum_data)
#        pct50_min[subpref_id] = analyze_cum_calling_data_min50pct(cum_data)
#        pct90_min[subpref_id] = analyze_cum_calling_data_min90pct(cum_data)
        
#    print wake_up_minc
#    print sleep_minc
    
#    save_times_to_file(wake_up_min)
    #save_times_to_file(pct90_min)
    
#    avg_min_subpref = defaultdict(float)
#    total_subpref0 = defaultdict(float)
#    
#    for subpref_id in range(1,256):
#        weekday_calls = 0
#        mins = 0
#        for hr in range(24):
#            for minute in week_data[subpref_id][hr].iterkeys():
#                weekday_calls += week_data[subpref_id][hr][minute]
#                mins += 1
#        avg_min_subpref[subpref_id] = weekday_calls / float(mins)
#        total_subpref0[subpref_id]  = weekday_calls
#        #print float(mins)
#        
#    midnight_pct = defaultdict(float)
#    
#    #print float(mins)
#    #print avg_min_subpref[220]
#    
#    file_name = "/home/sscepano/D4D res/allstuff/call timing/subpref_pct_midnight_fq.tsv"
#    f = open(file_name, "w")
#    
#    for subpref_id in range(1,256):
#        midnight_hour = 0
#        for minute in week_data[subpref_id][0].iterkeys():
#            midnight_hour += week_data[subpref_id][hr][minute]
#        if avg_min_subpref[subpref_id] > 0:
#            midnight_pct[subpref_id] = midnight_hour / float(avg_min_subpref[subpref_id] * 60)
#            f.write(str(subpref_id) + '\t' + str(midnight_pct[subpref_id]) + '\n')
#    
    
    
    
    
    avg_min_subpref = defaultdict(float)
    total_subpref = defaultdict(float)
    
    for subpref_id in range(1,256):
        weekday_calls = 0
        mins = 0
        for hr in range(24):
            for minute in weekend_data[subpref_id][hr].iterkeys():
                weekday_calls += weekend_data[subpref_id][hr][minute]
                mins += 1
        avg_min_subpref[subpref_id] = weekday_calls / float(mins)
        total_subpref[subpref_id]  = weekday_calls
        
#    print total_subpref[7] + total_subpref0[7]
        
    midnight_pct = defaultdict(float)
    
    
    print avg_min_subpref[254]
    
    file_name = "/home/sscepano/D4D res/allstuff/call timing/weekend_subpref_pct_midnight1v7s_fq.tsv"
    file_name2 = "/home/sscepano/D4D res/allstuff/call timing/weekend_subpref_01avg_fq.tsv"
    f = open(file_name, "w")
    f2 = open(file_name2, "w")
    
    for subpref_id in range(1,256):
        midnight_hour = 0
        for minute in weekend_data[subpref_id][1].iterkeys():
            midnight_hour += weekend_data[subpref_id][1][minute]
        if avg_min_subpref[subpref_id] > 0:
            midnight_pct[subpref_id] = midnight_hour / float(avg_min_subpref[subpref_id] * 60)
            f.write(str(subpref_id) + '\t' + str(midnight_pct[subpref_id]) + '\n')
            
            
    for subpref_id in range(1,256):
        found = False
        for hr in [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3]:
            for minute in weekend_data[subpref_id][hr].iterkeys():
                if not found:
                    if weekend_data[subpref_id][hr][minute] >= avg_min_subpref[subpref_id]*0.1:
                        subpref_05_min = 60*hr+minute
                        found = True      
        f2.write(str(subpref_id) + '\t' + str(subpref_05_min) + '\n')

    
    return

def plot_times(data):
    
#    for subpref_id in range(1,255):
#        from_data_to_timeplot_min(data[subpref_id],subpref_id)

    #from_data_to_timeplot_min_all(data)
    
#    cum_data = get_cumulative_call_timing_data_min(data[60])
    
#    print cum_data
#    
#    print_cumulative_call_timing_data_min(cum_data)

#    total_cum = get_cumulative_call_timing_data_min_total(data)
#    
#    print analyze_cum_calling_data_min1(total_cum)
#    print analyze_cum_calling_data_min2(total_cum)

    wake_up_min = defaultdict(int)
    sleep_min = defaultdict(int)
    pct30_min = defaultdict(int)
    pct40_min = defaultdict(int)
    pct50_min = defaultdict(int)
    pct90_min = defaultdict(int)
    
#    cum_data = get_cumulative_call_timing_data_min(data[120])
#    wake_up_minc = analyze_cum_calling_data_min1(cum_data)
#    sleep_minc = analyze_cum_calling_data_min2(cum_data)

    for subpref_id in range(1,256):
        cum_data = get_cumulative_call_timing_data_min(data[subpref_id])
        wake_up_min[subpref_id] = analyze_cum_calling_data_min1(cum_data)
        sleep_min[subpref_id] = analyze_cum_calling_data_min2(cum_data)
        pct30_min[subpref_id] = analyze_cum_calling_data_min30pct(cum_data)
        pct40_min[subpref_id] = analyze_cum_calling_data_min40pct(cum_data)
        pct50_min[subpref_id] = analyze_cum_calling_data_min50pct(cum_data)
        pct90_min[subpref_id] = analyze_cum_calling_data_min90pct(cum_data)
        
#    print wake_up_minc
#    print sleep_minc
    
    save_times_to_file(sleep_min)
    #save_times_to_file(pct90_min)
    
    return

def save_times_to_file(data):
    
    file_name = "/home/sscepano/D4D res/allstuff/call timing/week_wake_up_minute.tsv"
    #file_name = "/home/sscepano/D4D res/allstuff/call timing/weekedend_sleep_minute.tsv"
    #file_name = "/home/sscepano/D4D res/allstuff/call timing/weekdend_30pct_minute.tsv"
    #file_name = "/home/sscepano/D4D res/allstuff/call timing/40pct_minute.tsv"
    #file_name = "/home/sscepano/D4D res/allstuff/call timing/weekend_50pct_minute.tsv"
    #file_name = "/home/sscepano/D4D res/allstuff/call timing/weekdend_90pct_minute.tsv"
    
    f=open(file_name,"w")
    
    for minute in data.iterkeys():
        f.write(str(minute) + '\t' +str(data[minute]) + '\n')
    
    return

def analyze_cum_calling_data_min90pct(cum_data):
    
    for hr in range(1440):
        if cum_data[hr] > 0.90:
            return hr
        
    return 24

def analyze_cum_calling_data_min50pct(cum_data):
    
    for hr in range(1440):
        if cum_data[hr] > 0.50:
            return hr
        
    return 24


def analyze_cum_calling_data_min40pct(cum_data):
    
    for hr in range(1440):
        if cum_data[hr] > 0.40:
            return hr
        
    return 24

def analyze_cum_calling_data_min30pct(cum_data):
    
    for hr in range(1440):
        if cum_data[hr] > 0.30:
            return hr
        
    return 24

def analyze_cum_calling_data_min1(cum_data):
    
    for hr in range(1440):
        if cum_data[hr] > 0.20:
            return hr
        
    return 24

def analyze_cum_calling_data_min2(cum_data):
    
    for hr in range(1440):
        if cum_data[hr] > 0.80:
            return hr
        
    return 24


def from_data_to_timeplot_min(data, subpref):
    
    from matplotlib.ticker import FuncFormatter, MultipleLocator
    
    #minutes = np.linspace(0,24*60,24*60)
    
#    for i in range(24*60):
#        min[i] = i
    
    minutes = []
    val = []
    
    for hr in range(24):
        for minut in range(60):
            try:
#                append(val,data[hr][minut])
#                append(minutes,60*hr+minut)
                val.append(data[hr][minut])
                minutes.append(60*hr+minut)
                #print data[hr][minut]
            except: KeyError
            
    #print minutes
    #print val

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    plt.plot(minutes,val)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(lambda t,p : '%02d:%02d' % (t//60, t%60)))
    ax.xaxis.set_major_locator(MultipleLocator(120))
    #show()
    fig = plt.gcf()
    fig.autofmt_xdate(rotation=90, ha='center')
    #plt.show()
    plt.xlim((0,1440))
    figure_name = "/home/sscepano/D4D res/allstuff/call timing/weekedaysMIN/subpref_calling_pattern_weekday" + str(subpref) + ".png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi=200)    
    
    return

def from_data_to_timeplot_min_all(data):
    
    #minutes = np.linspace(0,24*60,24*60)
    
#    for i in range(24*60):
#        min[i] = i
    
    minutes = []
    val = []
    
    
    for hr in range(24):
        for minut in range(60):
            try:
#                append(val,data[hr][minut])
#                append(minutes,60*hr+minut)
                total=0
                for subpref in range(1,255):
                    try:
                        total += data[subpref][hr][minut]
                    except: KeyError
                val.append(total)
                minutes.append(60*hr+minut)
                #print data[hr][minut]
            except: KeyError
            
    print minutes
    print val

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    plt.plot(minutes,val)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(lambda t,p : '%02d:%02d' % (t//60, t%60)))
    ax.xaxis.set_major_locator(MultipleLocator(120))
    plt.xlim((0,1440))
    #show()
    fig = plt.gcf()
    fig.autofmt_xdate(rotation=90, ha='center')
    #show()

    figure_name = "/home/sscepano/D4D res/allstuff/call timing/MINUTES/calling_pattern_total.png"
    #figure_name = "/home/sscepano/D4D res/allstuff/call timing/weekedaysMIN/weekdays_calling_pattern_total.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi=200)    
    
    return

def get_cumulative_call_timing_data_min_total(data):
    
    cum_data = defaultdict(float)
    cur_sum = 0
    
    for hr in range(24):
        for minut in range(60):
            try:
                total=0
                for subpref in range(1,255):
                    try:
                        total += data[subpref][hr][minut]
                    except: KeyError
                cur_sum += total
                cum_data[hr*60+minut] = cur_sum
            except: KeyError
        
    for hr in range(24):
        for minut in range(60):
            if cum_data[1439] > 0:
                cum_data[hr*60+minut] = cum_data[hr*60+minut] / float(cum_data[1439])
    
    return cum_data

def get_cumulative_call_timing_data_min(data):
    
    cum_data = defaultdict(float)
    cur_sum = 0
    
    for hr in range(24):
        #print hr, data[hr]
        for minut in data[hr].iterkeys():
            try:
                cur_sum += data[hr][minut]
                cum_data[hr*60+minut] = cur_sum
            except: KeyError
        
    for hr in range(24):
        for minut in data[hr].iterkeys():
            try:
                if cum_data[1439] > 0:
                    cum_data[hr*60+minut] = cum_data[hr*60+minut] / float(cum_data[1439])
            except: KeyError
    
    return cum_data

def print_cumulative_call_timing_data_min(cum_data):
    
    minutes = []
    val = []
    
    
    for m in range(1440):
        try:
            total = cum_data[m]
            val.append(total)
            minutes.append(m)
        except: KeyError
            
    print minutes
    print val

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    plt.plot(minutes,val)
    ax = plt.gca()
    
    #show()

    figure_name = "/home/sscepano/D4D res/allstuff/call timing/MINUTES/cum_calling_pattern_total.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi=200)    
    
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


def from_data_to_timeplot3(data, subpref):
    
    val = [0,0,0,0,0,0,0,0]
    
    for hr in data.iterkeys():
        val[hr+1] = data[hr]

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.step([0,1,2,3,4,5,6,7], val, '-')
    ax.axvspan(5, 7, color='yellow', alpha=0.5)
    ax.set_xlim(0,7)
    ax.set_xticks((0,1,2,3,4,5,6,7))
    
    #show()

    # figure_name = "/home/sscepano/D4D res/allstuff/call timing/by day maps/" + str(subpref) + "_subpref_weekly_calls.png"
    figure_name = "/home/sscepano/D4D res/allstuff/call timing/total_weekly_calls.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return