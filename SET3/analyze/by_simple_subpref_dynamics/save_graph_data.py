'''
Created on Jan 23, 2013

@author: sscepano
'''
import networkx as nx
import matplotlib.pyplot as plt
from pylab import *
from collections import defaultdict

def read_in_subpref_num_users():
    
    subpref_num_usr = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes/Num_of_users_per_home_subpref.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, num_usr = line.split('\t')
        subpref =  int(subpref[:-1])
        num_usr = int(num_usr)
        subpref_num_usr[subpref] = num_usr
             
    return subpref_num_usr        

def save2gml(G):
    
    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/simple dynamics/subpref_total_movements_cleaned.gml")
    
    #G.remove_node(0)
    
    print G.nodes()
    
#    max = 1
#    min = 1
#    for u,v,d in G.edges(data=True):
#        if d['weight'] > max:
#            max = d['weight']
#        if d['weight'] < min:
#            min = d['weight']
#            
#    max7s = float(max)
#    print max7s
#    print min
    
#    fig = figure()
#    axes = fig.add_subplot(111)
#    
#    pos=nx.spring_layout(G) 
#    nx.draw(G, pos, ax=axes)
#    edge_labels=dict([((u,v,),d['weight'])
#        for u,v,d in G.edges(data=True)])
#    nx.draw_networkx_edge_labels(G, pos, edge_labels,  ax=axes)
#    
#    #plt.show()
#    
#    figure_name = "/home/sscepano/D4D res/allstuff/simple dynamics/subpref_total_movements.png" 
#    print(figure_name)
#    plt.savefig(figure_name, format = "png")    


    
    
    return

def reprocess_gml():
    
    #G = nx.DiGraph()
    G = nx.read_gml("/home/sscepano/D4D res/allstuff/simple dynamics/v1/subpref_total_movements_cleaned.gml")
    
    num_usr = read_in_subpref_num_users()
    
    for edge in G.edges(data=True):
        subpref1 = edge[0]
        subpref2 = edge[1]
        if num_usr[subpref1] > 0 and num_usr[subpref2] > 0:
            edge[2]['weight'] /= (float(num_usr[subpref1])*float(num_usr[subpref2])) * 100
        
    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/simple dynamics/v2/subpref_total_movements_scaled2.gml")
    
    return G



#reprocess_gml()