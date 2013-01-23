'''
Created on Jan 23, 2013

@author: sscepano
'''
import networkx as nx
import matplotlib.pyplot as plt
from pylab import *

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