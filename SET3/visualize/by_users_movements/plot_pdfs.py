'''
Created on Feb 14, 2013

@author: sscepano
'''

import pyplot as plt
import numpy as nn
from collections import defaultdict, OrderedDict
from read_in import fq_data as rd

def from_files_usr_movements():
    
    file_name1 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/user_number_of_edges_v1.tsv"
    file_name2 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/user_number_of_nodes_v1.tsv"
    file_name3 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/user_number_of_displacements_v1.tsv"
    
    nits = []
    its = []
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name3, 'r')    
    # read the file
    for line in f:
        i = i + 1
        it, nit = line.split('\t')
        nit = int(nit)
        it = int(it)
        nit = int(nit)
        nits.append(nit)
        its.append(it)

    mi = min(nits)
    mx = max(nits)
    print("Minimum # edges ", mi)
    print("Maximum # edges ", mx)
    
    total_nit = float(sum(nits))
    print("Total # edges ", total_nit)
    
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

    plt.plot(its7s, nits7s, 'o', linewidth=0.5, label= 'distr. of # displacements ')
    
    plt.xlabel('# displacements')
    plt.ylabel('P(# displacements)')
    plt.legend()   
    
    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
    plt.yscale('log')
    plt.xscale('log')
    #figure_name1 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/usr_num_edges.png"
    #figure_name2 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/usr_num_nodes.png"
    figure_name3 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/usr_num_displacements.png"
          
    print(figure_name3)
    plt.savefig(figure_name3, format = "png", dpi=300)      
    
    return
from_files_usr_movements()