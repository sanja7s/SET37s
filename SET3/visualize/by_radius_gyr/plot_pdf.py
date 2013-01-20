'''
Created on Jan 20, 2013

@author: sscepano
'''

import pyplot as plt
import numpy as nn

# we find this from the file by reading it once before
max_num_calls = 137356 + 1

def from_file_radius_gyr(file_name): 
   
    usr_rg = nn.zeros(500001)
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        u, rg = line.split('\t')
        rg = float(rg)
        u = int(u)
        usr_rg[u] = rg
       

    mi = min(usr_rg)
    mx = max(usr_rg)
    print("Minimum number of calls ", mi)
    print("Maximum number of calls ", mx)
    
#    total_u = float(sum(nc_distr))
#    print("Total users found ", total_u)
    
#   test_file_out = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/Obtained_num_calls_and_its_pct.tsv"
#   fto =  open(test_file_out,"w")
#    for j in range(0, max_num_calls):
#        nc_distr_pct[j] = (nc_distr[j] / total_u) * 100
#        fto.write(str(j) + '\t' + str(nc_distr_pct[j]) + '\n')

#    # I was just checking that the total percents sums up to 100 and they do but it looked funny as we have so small values
#    total = 0    
#    for i in range (max_num_calls):
#        total += percent_users[i]
#    print ("Check ", total)

############################################################################################################################
# THIS is to plot number of users pdf
############################################################################################################################

    fig1 = plt.figure(1)
    ax = fig1.add_subplot(111)
    n, bins, rectangles = ax.hist(usr_rg, 100, normed=True)

    #plt.plot(nc_distr_pct, 'ro', linewidth=0.5, label= 'pdf Num of calls')
    
    plt.xlabel('rg [km]')
    plt.ylabel('P(rg)')
    plt.legend()   
    
#    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
    plt.yscale('log')
    plt.xscale('log')
    figure_name = "/home/sscepano/D4D res/allstuff/rg/pdf rg loglog.png"
    
#    #this is a regular plot file, then comment the previous loglog block
#    figure_name = "/home/sscepano/D4D res/allstuff/rg/pdf rg.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
    
################################################################################################################################
## THIS is to plot fq pdf
################################################################################################################################
#
#    plt.figure(2)
#    
#    fq = []
#    
#    for j in range(max_num_calls):
#        fq.append( float(j / 3360.0))
#
#    ffq = []
#    
#    for j in range(max_num_calls):
#        ffq.append(nc_distr_pct[j])
#        
#   
##    test_file_out2 = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/Calculated_fq_calls_and_its_pct2.tsv"
##    fto2 =  open(test_file_out2,"w")
##    for j in range(0, max_num_calls):
##        fto2.write(str(fq[j]) + '\t' + str(ffq[j]) + '\n')    
#
#
#    # Finally understood here -- when I give two arrays: x, y (at least append values IN ORDER like here) -- pyplot will plot y versus x
#    plt.plot(fq, ffq, 'g.', linewidth=0.3, label= 'pdf fq of calls')
#    
#    plt.xlabel('fq of calls')
#    plt.ylabel('% Users')
#    plt.legend()   
#    
#    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
#    plt.yscale('log')
#    plt.xscale('log')
#    figure_name = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/SET3 distr of fq of calls loglog.png" 
#    
##    # this is a regular plot file, then comment the previous loglog block
##    figure_name = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/SET3 distr of fq of calls.png"
#      
#    print(figure_name)
#    plt.savefig(figure_name, format = "png")   
    

    return   

# invoke the function for plotting number of calls and frequency probability distribution (percents of users)
from_file_radius_gyr("/home/sscepano/D4D res/ORGANIZED/SET3/Clustering/usr res/usr_radius_gyration.tsv")