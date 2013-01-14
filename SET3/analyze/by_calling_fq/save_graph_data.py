'''
Created on Jan 12, 2013

@author: sscepano
'''
import networkx as nx
import matplotlib.pyplot as plt
from pylab import *

def graph2_file2(G, usr):
    # this one is for patterns
    
    fig = figure()
    axes = fig.add_subplot(111)
    
    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/usr_movements_" + str(usr) + ".gml")
    
    pos=nx.spring_layout(G) 
    nx.draw(G, pos, ax=axes)
    edge_labels=dict([((u,v,),d['weight'])
        for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels,  ax=axes)
    
    #plt.show()
    
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/usr_movements_" + str(usr) + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return

def graph2_file(G, c, usr):
    # this one is for movements
    
    fig = figure()
    axes = fig.add_subplot(111)
    
    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/User movements graphs/" + c + "/gml/usr_movements_" + str(usr) + ".gml")
    
    pos=nx.spring_layout(G) 
    nx.draw(G, pos, ax=axes)
    edge_labels=dict([((u,v,),d['weight'])
        for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels,  ax=axes)
    
    #plt.show()
    
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/" + c + "/png/usr_movements_" + str(usr) + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return

def graph2_file_subpref2(G, subpref):
    
    # for patterns
    
    fig = figure()
    axes = fig.add_subplot(111)
    
    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/subprefs/subpref_patterns_" + str(subpref) + ".gml")
    
    pos=nx.spring_layout(G) 
    nx.draw(G, pos, ax=axes)
    edge_labels=dict([((u,v,),d['weight'])
        for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels,  ax=axes)
    
    #plt.show()
    
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/subprefs/subpref_patterns" + str(subpref) + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
    
    return