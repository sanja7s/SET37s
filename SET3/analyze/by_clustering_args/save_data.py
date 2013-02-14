'''
Created on Feb 14, 2013

@author: sscepano
'''

from collections import defaultdict, OrderedDict
import pyplot as plt
from read_in import fq_data as rd

def save_to_file(usr_traj, usr_day):
    
    avg_usr_traj = defaultdict(float)
    
    for usr in range(500001):
        avg_usr_traj[usr] = usr_traj[usr] / float(usr_day[usr][1])
        
        
    file_name = "/home/sscepano/D4D res/allstuff/traj/avg daily/usr_avg_Daily_traj.tsv"
    f = open(file_name, "w")
    
    for usr in range(500001):
        f.write(str(usr) + '\t' + str(avg_usr_traj[usr] + '\n'))
        
        
        
        
#    file_name_st = "/home/sscepano/D4D res/allstuff/traj/avg daily/subpref_avg_Daily_traj.tsv"
#    fst = open(file_name_st, "w")    
#    
#    for subpref in range(1,256):    
#        subpref_sum = 0
#        usrs_sum = 0
#        users_list = rd.read_in_subpref_users(subpref)
#        file_names = "/home/sscepano/D4D res/allstuff/traj/avg daily/subpref/subpref_usr_avg_daily_traj_" + str(subpref) + ".tsv"
#        fs = open(file_names, "w")
#        for usr in range(500001):
#            if users_list[usr] == 1:
#                fs.write(str(usr) + '\t' + str(avg_usr_traj[usr]) + '\n')
#                subpref_sum += avg_usr_traj[usr]
#                usrs_sum += 1
#        fst.write(str(subpref) + '\t' + str(subpref_sum/float(usrs_sum)) + '\n')
#        subpref_usrs = rd.read_in_subpref_num_users()[subpref]
#        if subpref_usrs == usrs_sum:
#            print 'yes ' + str(subpref)
#        else:
#            print 'no ' + str(subpref)
                 
        
    return

def save_to_plot(avg_usr_traj):
    
    nits = []
    its = []
    
    # a loop where we populate those two arrays from the file
    i = 0
#    f = open(file_name, 'r')    
#    # read the file
    for usr in range(500001):
        i = i + 1
        nits.append(int(avg_usr_traj[usr]))
        its.append(usr)

    mi = min(nits)
    mx = max(nits)
    print("Minimum radius of gyr ", mi)
    print("Maximum radius of gyr ", mx)
    
    total_nit = float(sum(nits))
    print("Total radius of gyr ", total_nit)
    
    pdf_nits = defaultdict(int)
    
    for j in range(0, len(nits)):
        pdf_nits[nits[j]] += 1
        
    ordered = OrderedDict(sorted(pdf_nits.items(), key=lambda t: t[0]))
    
    nits7s = []
    its7s = []
    
    test = 0
    
    for j in ordered.iterkeys():
        nits7s.append(ordered[j]/500000.0)
        test += ordered[j]/500000.0
        its7s.append(j)
        
    print test
        
############################################################################################################################
# THIS is to plot number of users pdf
############################################################################################################################

    plt.figure(7)

    plt.plot(its7s, nits7s, 'o', linewidth=0.5, label= 'distribution of Rg')
    
    plt.xlabel('rg [km]')
    plt.ylabel('P(rg)')
    plt.legend()   
    
    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
    plt.yscale('log')
    plt.xscale('log')
    figure_name = "/home/sscepano/D4D res/allstuff/traj/avg daily/avg_daily_traj_total.png"
          
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi=300)    
    
    return