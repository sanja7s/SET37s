'''
Created on Jan 8, 2013

@author: sscepano
'''

import pyplot as plt
import numpy as n

# we find this from the file by reading it once before
max_num_calls = 137356 + 1

# here we read from file with users and their number of calls and we calculate number of users who had certain number of calls
# we use an array of length 137356 as that is the maximum number of calls we found for a user
def from_file_num_calls(file_name): 
   
    # here we store the num of calls made by a user
    usr_and_his_num_calls = n.zeros(500001, dtype=n.int)
    # here we store the fq of calls made by a user, but we calculate it from the num_calls
    fq_distr = n.zeros(max_num_calls)
    # from the previous array obtained by counting users who made the same total number of calls
    nc_distr = n.zeros(max_num_calls, dtype=n.int)
    # here we just save percents of users
    nc_distr_pct = n.zeros(max_num_calls)
    
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        u, nc = line.split('\t')
        nc = int(nc)
        u = int(u)
        usr_and_his_num_calls[u] = nc
        nc_distr[nc] += 1

    mi = min(usr_and_his_num_calls)
    mx = max(usr_and_his_num_calls)
    print("Minimum number of calls ", mi)
    print("Maximum number of calls ", mx)
    
    total_u = float(sum(nc_distr))
    print("Total users found ", total_u)
    
#   test_file_out = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/Obtained_num_calls_and_its_pct.tsv"
#   fto =  open(test_file_out,"w")
    for j in range(0, max_num_calls):
        nc_distr_pct[j] = (nc_distr[j] / total_u) * 100
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

    plt.plot(nc_distr_pct, 'ro', linewidth=0.5, label= 'pdf Num of calls')
    
    plt.xlabel('N, num of calls')
    plt.ylabel('% Users')
    plt.legend()   
    
#    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
#    plt.yscale('log')
#    plt.xscale('log')
#    figure_name = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/SET3 distr of num of calls loglog.png" 
    
    #this is a regular plot file, then comment the previous loglog block
    figure_name = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/SET3 distr of num of calls.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
    
###############################################################################################################################
# THIS is to plot fq pdf
###############################################################################################################################

    plt.figure(2)
    
    fq = []
    
    for j in range(max_num_calls):
        fq.append( float(j / 3360.0))

    ffq = []
    
    for j in range(max_num_calls):
        ffq.append(nc_distr_pct[j])
        
   
#    test_file_out2 = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/Calculated_fq_calls_and_its_pct2.tsv"
#    fto2 =  open(test_file_out2,"w")
#    for j in range(0, max_num_calls):
#        fto2.write(str(fq[j]) + '\t' + str(ffq[j]) + '\n')    


    # Finally understood here -- when I give two arrays: x, y (at least append values IN ORDER like here) -- pyplot will plot y versus x
    plt.plot(fq, ffq, 'g.', linewidth=0.3, label= 'pdf fq of calls')
    
    plt.xlabel('fq of calls')
    plt.ylabel('% Users')
    plt.legend()   
    
    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
    plt.yscale('log')
    plt.xscale('log')
    figure_name = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/SET3 distr of fq of calls loglog.png" 
    
#    # this is a regular plot file, then comment the previous loglog block
#    figure_name = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/1/SET3 distr of fq of calls.png"
      
    print(figure_name)
    plt.savefig(figure_name, format = "png")   
    

    return   

# invoke the function for plotting number of calls and frequency probability distribution (percents of users)
from_file_num_calls("/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/new results -- check the same/Users_and_their_total_calls_number.tsv")