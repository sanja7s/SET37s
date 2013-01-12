'''
Created on Jan 10, 2013

@author: sscepano
'''

#def from_data_to_graphs(interval):
    
#    random_users = [777, 20120, 51300, 117711, 12345]
#    
#    x_axis = []
#    y_axis = []
#    
#    for usr in random_users:
#        
#        i = 0
#        for it in interval[usr].iterkeys():
#            x_axis.append(i)
#            y_axis.append(interval[usr][it])

from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY, MonthLocator
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2
import datetime
import matplotlib.dates as dt
from collections import defaultdict, OrderedDict
from matplotlib import pyplot as plt

## (Year, month, day) tuples suffice as args for quotes_historical_yahoo
##date1 = datetime.date( 2011, 12, 1 )
##date2 = datetime.date( 2011, 12, 2 )
#
#date1 = datetime.datetime( 2011, 12, 1, 12, 0)
#date2 = datetime.datetime( 2011, 12, 15, 12, 0)
#
#date7s = []
#
#d = date1
#delta = datetime.timedelta(hours=1)
#while d <= date2:
#    print d.strftime("%Y-%m-%d %H %M")
#    #print dt.date2num(d)
#    date7s.append(d)
#    d += delta
#
#print len(date7s)
#mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
#alldays    = DayLocator()              # minor ticks on the days
#weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
#dayFormatter = DateFormatter('%d')      # Eg, 12
##
##quotes = quotes_historical_yahoo('INTC', date1, date2)
##if len(quotes) == 0:
##    raise SystemExit
##print quotes
##
#values = [int]*len(date7s)
#for i in range(len(date7s)):
#    #values[i] = i%25
#    values[i] = 0
#    
#values[10] = 1
#values[22] = 1
##
##print quotes    
##    
##dates = [q[0] for q in quotes]
##print dates
##opens = [q[1] for q in quotes]
##print opens
##
###print len(opens)
###print len(dates)
#
#fig = figure()
#fig.subplots_adjust(bottom=0.2)
#ax = fig.add_subplot(111)
#ax.xaxis.set_major_locator(mondays)
#ax.xaxis.set_minor_locator(alldays)
#ax.xaxis.set_major_formatter(weekFormatter)
##ax.xaxis.set_minor_formatter(dayFormatter)
##
###plot_day_summary(ax, quotes, ticksize=3)
###ax.plot_date(dates, opens, '-')
###plot_day_summary(ax, quotes, ticksize=3)
###candlestick(ax, quotes, width=0.6)
#ax.plot_date(date7s, values, '-')
##
#ax.xaxis_date()
#ax.autoscale_view()
#ax.set_ylim(-1,2)
#setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')
#
#show()


def from_file_interevents(file_name, usr):
    
    date7s = []
    interevents = []
    
    interval = defaultdict(int)
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        dt, it = line.split('\t')
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S') 
        it = int(it)
        #date7s.append(dt)
        #interevents.append(it)
        interval[dt] = it
        
    ordered = OrderedDict(sorted(interval.items(), key=lambda t: t[0]))
    
    for dt in ordered.iterkeys():
        date7s.append(dt)
        it = interval[dt]
        interevents.append(it)
    
    print i
    
    print date7s
    print interevents
   
    
    loc = MonthLocator()
#    loc2 = WeekdayLocator(byweekday=(SU))
    alldays    = DayLocator()               # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
    dayFormatter = DateFormatter('%d')      # Eg, 12

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)
    #
    ##plot_day_summary(ax, quotes, ticksize=3)
    ##ax.plot_date(dates, opens, '-')
    ##plot_day_summary(ax, quotes, ticksize=3)
    ##candlestick(ax, quotes, width=0.6)
    #ax.plot_date(date7s, interevents, '-')
    ax.step(date7s,interevents)
    ax.xaxis_date()
    delta = datetime.timedelta(days=1)
    
    num_dates = len(date7s)
    min_date = date7s[0]
    max_date = date7s[num_dates - 1]
    weekend_date = min_date.date()
    while weekend_date <= max_date.date():
        if weekend_date.weekday() in [5, 6]:
            ax.axvspan(weekend_date - delta, weekend_date, color='yellow', alpha=0.5)
        weekend_date += delta 
    ax.autoscale_view()
    #ax.set_ylim(-1,2)
    setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    
    #show()
    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/usr_" + str(usr) + ".png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return

#from_file_interevents("/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/Single_user_date_intervals_448117.tsv", 448117)



def from_file_interevents_2weeks(file_name, usr):
    
    file_name = file_name + str(usr) + "C.tsv"
    
    date7s = []
    interevents = []
    
    interval = defaultdict(int)
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        dt, it = line.split('\t')
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S') 
        it = int(it)
        #date7s.append(dt)
        #interevents.append(it)
        interval[dt] = it
        
    ordered = OrderedDict(sorted(interval.items(), key=lambda t: t[0]))
    
    for dt in ordered.iterkeys():
        date7s.append(dt)
        it = interval[dt]
        interevents.append(it)
    
    print i
    
    print date7s
    print interevents
   
    
    loc = WeekdayLocator(byweekday=(MO,TU,WE,TH,FR))
#    loc2 = WeekdayLocator(byweekday=(SU))
    alldays    = DayLocator()               # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # Eg, Jan 12
    dayFormatter = DateFormatter('%d')      # Eg, 12

    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)
    #
    ##plot_day_summary(ax, quotes, ticksize=3)
    ##ax.plot_date(dates, opens, '-')
    ##plot_day_summary(ax, quotes, ticksize=3)
    ##candlestick(ax, quotes, width=0.6)
    #ax.plot_date(date7s, interevents, '-')
    ax.step(date7s,interevents)
    ax.xaxis_date()
    delta = datetime.timedelta(days=1)
    
    num_dates = len(date7s)
    min_date = date7s[0]
    max_date = date7s[num_dates - 1]
    weekend_date = min_date.date()
    while weekend_date <= max_date.date():
        if weekend_date.weekday() in [5, 6]:
            ax.axvspan(weekend_date - delta, weekend_date, color='yellow', alpha=0.5)
        weekend_date += delta 
    ax.autoscale_view()
    #ax.set_ylim(-1,2)
    setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    
    #show()
    # figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/A/usr_" + str(usr) + ".png"
    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/C/usr_" + str(usr) + ".png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return

usr = 248907
from_file_interevents_2weeks("/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/C/Single_user_date_intervals_", usr)




def from_file_interevents_aggregated_1week(file_name, usr):
    
    date7s = [0,0,0,0,0,0,0]
    interevents = []
    
    interval = defaultdict(int)
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        dt, it = line.split('\t')
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S') 
        it = int(it)
        #date7s.append(dt)
        #interevents.append(it)
        interval[dt] = it
        
    ordered = OrderedDict(sorted(interval.items(), key=lambda t: t[0]))
    
    print dt
    
    for dt in ordered.iterkeys():
        date7s[dt.weekday()] += interval[dt]
#    
    print i
    
    print date7s
    print interevents
   
    fig = figure()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.step([0,1,2,3,4,5,6], date7s, '-')
    ax.axvspan(5, 7, color='yellow', alpha=0.5)
    ax.set_xlim(-1,7)
    
    print(date7s[0])
    
#    show()

    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/1week_agr_usr_" + str(usr) + ".png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return

#from_file_interevents_aggregated_1week("/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/single usr stats/Single_user_date_intervals_248907.tsv", 248907)


def from_file_pdf_interevent_times(file_name): 
      
    nits = []
    its = []
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        it, nit = line.split('\t')
        nit = int(nit)
        it = int(it)
        nits.append(nit)
        its.append(it)

    mi = min(nits)
    mx = max(nits)
    print("Minimum number of calls ", mi)
    print("Maximum number of calls ", mx)
    
    total_nit = float(sum(nits))
    print("Total users found ", total_nit)
    
    
#   test_file_out = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/Obtained_num_calls_and_its_pct.tsv"
#   fto =  open(test_file_out,"w")
    for j in range(0, len(nits)):
        nits[j] = (nits[j] / total_nit) * 100
#        # this is to plot smaller part of regular plot
#        if nits[j] > 0.0001:
#            nits[j] = 0
#            its[j] = 0
            #nits.remove(nits[j])
            #its.remove(its[j])
#        fto.write(str(j) + '\t' + str(nc_distr_pct[j]) + '\n')

#    # I was just checking that the total percents sums up to 100 and they do but it looked funny as we have so small values
#    total = 0    
#    for i in range (max_num_calls):
#        total += percent_users[i]
#    print ("Check ", total)

############################################################################################################################
# THIS is to plot number of users pdf
############################################################################################################################

    plt.figure(1)

    plt.plot(its, nits, '-.', linewidth=0.5, label= 'pdf Interevent times')
    
    plt.xlabel('I, intervent time')
    plt.ylabel('P(I)')
    plt.legend()   
    
#    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
#    plt.yscale('log')
#    plt.xscale('log')
#    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/plots/Interevent_times_distribution loglog.png" 
    
    # this is a regular plot file, then comment the previous loglog block
    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/plots/Interevent_times_distribution.png"
#    # this si to plost smaller part of regular plot
#    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/plots/Interevent_times_distribution_part.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
    
    return


#from_file_pdf_interevent_times("/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/Intervals_per_user_total.tsv")


def from_file_pdf_interevent_times_subpref(file_name, subpref): 
    
    file_name = file_name + str(subpref) + ".tsv"
      
    nits = []
    its = []
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        it, nit = line.split('\t')
        nit = int(nit)
        it = int(it)
        nits.append(nit)
        its.append(it)

    mi = min(nits)
    mx = max(nits)
    print("Minimum number of calls ", mi)
    print("Maximum number of calls ", mx)
    
    total_nit = float(sum(nits))
    print("Total calls count ", total_nit)
    
    
#   test_file_out = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/Obtained_num_calls_and_its_pct.tsv"
#   fto =  open(test_file_out,"w")
    for j in range(0, len(nits)):
        nits[j] = (nits[j] / total_nit) * 100
#        fto.write(str(j) + '\t' + str(nc_distr_pct[j]) + '\n')

#    # I was just checking that the total percents sums up to 100 and they do but it looked funny as we have so small values
#    total = 0    
#    for i in range (max_num_calls):
#        total += percent_users[i]
#    print ("Check ", total)

############################################################################################################################
# THIS is to plot number of users pdf
############################################################################################################################

    plt.figure(subpref)

    plt.plot(its, nits, '.', linewidth=0.5, label= 'pdf Interevent times')
    
    plt.xlabel('I, intervent time')
    plt.ylabel('P(I)')
    plt.legend()   
    
    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
    plt.yscale('log')
    plt.xscale('log')
    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/plots/Intervent distributions v2/Interevent_times_distribution loglog_subpref_" + str(subpref) + ".png"
    
#    # this is a regular plot file, then comment the previous loglog block
#    figure_name = "/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/plots/Interevent_times_distribution_subpref_" + str(subpref) + ".png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
    
    return


#subpref = 77
#for subpref in range(1,256):
#    try:
#        from_file_pdf_interevent_times_subpref("/home/sscepano/D4D res/allstuff/SET3 intervals from python/1/Intervals_per_subpref_", subpref)
#    except IOError:
#        print ("No suboref " + str(subpref)) 

