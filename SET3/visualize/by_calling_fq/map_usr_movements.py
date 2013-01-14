'''
Created on Jan 12, 2013

@author: sscepano
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 5.5
import networkx as nx
import matplotlib.colors as colors
import matplotlib.cm as cm
from math import log

def plot_movements(G, subpref):
    
    subpref_str =  str(subpref)
    
    m = Basemap(llcrnrlon=-9, \
                    llcrnrlat=3.8, \
                    urcrnrlon=-1.5, \
                    urcrnrlat = 11, \
                    resolution = 'h', \
                    projection = 'tmerc', \
                    lat_0 = 7.38, \
                    lon_0 = -5.30)
   
    # read the shapefile archive
    s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')
    
    m.drawcoastlines()

    # data to plot on the map    
    lons = [int]*256
    lats = [int]*256
    num = []
    
    # read in coordinates fo subprefs
    file_name2 = "/home/sscepano/DATA SET7S/D4D/SUBPREF_POS_LONLAT.TSV"
    f2 = open(file_name2, 'r')
    
    # read subpref coordinates
    subpref_coord = {}
    for line in f2:
        subpref_id, lon, lat = line.split('\t')
        lon = float(lon)
        lat = float(lat)
        subpref_id = int(subpref_id)
        subpref_coord.keys().append(subpref_id)
        subpref_coord[subpref_id] = (lon, lat)
    
    f2.close()
    
    # if wanna plot number of users whose this is home subpref
    for subpref in range(1,256):
        lons[subpref] = subpref_coord[subpref][0]
        lats[subpref] = subpref_coord[subpref][1]
    
    
    if G.has_node(-1): 
        G.remove_node(-1)

    max = 1
    min = 1
    for u,v,d in G.edges(data=True):
        if d['weight'] > max:
            max = d['weight']
        if d['weight'] < min:
            min = d['weight']
            
    max7s = float(max)
    print max7s
    print min
        
#    edge_width=[]
#    for u,v,d in G.edges(data=True):
#        edge_width.append(d['weight'])
        #print d['weight']
    
#    pos=dict([((n,),m(lons[n], lats[n]))
#        for n in G.nodes()])
#   
     
#    for node in G.nodes():
#        #print node
#        x, y = m(lons[node], lats[node])
#        pos.keys().append(node)
#        pos[node] = (x, y)
    
 
    for u, v, d in G.edges(data=True):
        lo = []
        la = []   
        lo.append(lons[u])
        lo.append(lons[v])
        la.append(lats[u])
        la.append(lats[v])
        x, y = m(lo, la)
        linewidth7s = d['weight'] / max7s
        linewidth7s = linewidth7s * 700
        m.plot(x,y, linewidth= linewidth7s)
        
#############################################  
##    lo = []
##    la = []   
##    lo.append(lons[7])
##    lo.append(lons[11])
##    la.append(lats[7])
##    la.append(lats[11])
##    x, y = m(lo, la)  
##    m.plot(x,y, linewidth= 0.3)
#        
#    #cmap=cm.get_cmap('gist_rainbow',256)
#    #cmap = plt.cm.Blues
#    
#    #nx.draw_networkx_nodes(G, pos,  node_color='w', node_size=55,alpha=0.3, linewidths = 0.000001 ) 
#    #nx.draw_networkx_labels(G, pos,  font_size=7,alpha=0.7 )    
#    #nx.draw_networkx_edges(G, pos, arrows=False, edge_vmin = min, edge_vmax = max, edge_color = edge_width, edge_cmap = cmap)
#    #nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7.5, font_color = 'r')
#    #nx.draw(G, pos, edge_color = edge_width, edge_cmap = cmap)
#    
#    #plt.show()
##
#############################################

    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/ALL/non_scaled_subprefs/subpref_usr_movements_vPYP" + subpref_str + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")  
    
#    print G.number_of_nodes()  
#    print G.number_of_edges()  
    
    plt.clf()
    
    m = Basemap(llcrnrlon=-9, \
                    llcrnrlat=3.8, \
                    urcrnrlon=-1.5, \
                    urcrnrlat = 11, \
                    resolution = 'h', \
                    projection = 'tmerc', \
                    lat_0 = 7.38, \
                    lon_0 = -5.30)
   
    # read the shapefile archive
    s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')
    
    m.drawcoastlines()
    
    for u, v, d in G.edges(data=True):
        lo = []
        la = []   
        lo.append(lons[u])
        lo.append(lons[v])
        la.append(lats[u])
        la.append(lats[v])
        x, y = m(lo, la)
        linewidth7s = d['weight'] / max7s
        linewidth7s = linewidth7s *70 + 0.17
        m.plot(x,y, linewidth= linewidth7s)
        
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/ALL/scaled_subprefs/subpref_usr_movements_vPYP_SCALED" + subpref_str + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")  
     
    return


#plot_movements(2)

def plot_commuting_patterns(G, usr):
    
    usr_str =  str(usr)
    
    m = Basemap(llcrnrlon=-9, \
                    llcrnrlat=3.8, \
                    urcrnrlon=-1.5, \
                    urcrnrlat = 11, \
                    resolution = 'h', \
                    projection = 'tmerc', \
                    lat_0 = 7.38, \
                    lon_0 = -5.30)
   
    # read the shapefile archive
    s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')
    
    m.drawcoastlines()

    # data to plot on the map    
    lons = [int]*256
    lats = [int]*256
    num = []
    
    # read in coordinates fo subprefs
    file_name2 = "/home/sscepano/DATA SET7S/D4D/SUBPREF_POS_LONLAT.TSV"
    f2 = open(file_name2, 'r')
    
    # read subpref coordinates
    subpref_coord = {}
    for line in f2:
        subpref_id, lon, lat = line.split('\t')
        lon = float(lon)
        lat = float(lat)
        subpref_id = int(subpref_id)
        subpref_coord.keys().append(subpref_id)
        subpref_coord[subpref_id] = (lon, lat)
    
    f2.close()
    
    # if wanna plot number of users whose this is home subpref
    for subpref in range(1,256):
        lons[subpref] = subpref_coord[subpref][0]
        lats[subpref] = subpref_coord[subpref][1]
    
    
    if G.has_node(-1): 
        G.remove_node(-1)

    max = 1
    min = 1
    for u,v,d in G.edges(data=True):
        if d['weight'] > max:
            max = d['weight']
        if d['weight'] < min:
            min = d['weight']
            
    max7s = float(max)
    print max7s
    print min
        
#    edge_width=[]
#    for u,v,d in G.edges(data=True):
#        edge_width.append(d['weight'])
        #print d['weight']
    
#    pos=dict([((n,),m(lons[n], lats[n]))
#        for n in G.nodes()])
#   
     
#    for node in G.nodes():
#        #print node
#        x, y = m(lons[node], lats[node])
#        pos.keys().append(node)
#        pos[node] = (x, y)
    
 
    for u, v, d in G.edges(data=True):
        lo = []
        la = []   
        lo.append(lons[u])
        lo.append(lons[v])
        la.append(lats[u])
        la.append(lats[v])
        x, y = m(lo, la)
        linewidth7s = d['weight'] / max7s
        linewidth7s = linewidth7s
        m.plot(x,y, linewidth= linewidth7s)
        
#############################################  
##    lo = []
##    la = []   
##    lo.append(lons[7])
##    lo.append(lons[11])
##    la.append(lats[7])
##    la.append(lats[11])
##    x, y = m(lo, la)  
##    m.plot(x,y, linewidth= 0.3)
#        
#    #cmap=cm.get_cmap('gist_rainbow',256)
#    #cmap = plt.cm.Blues
#    
#    #nx.draw_networkx_nodes(G, pos,  node_color='w', node_size=55,alpha=0.3, linewidths = 0.000001 ) 
#    #nx.draw_networkx_labels(G, pos,  font_size=7,alpha=0.7 )    
#    #nx.draw_networkx_edges(G, pos, arrows=False, edge_vmin = min, edge_vmax = max, edge_color = edge_width, edge_cmap = cmap)
#    #nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7.5, font_color = 'r')
#    #nx.draw(G, pos, edge_color = edge_width, edge_cmap = cmap)
#    
#    #plt.show()
##
#############################################

    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/A/users/non-scaled/usr_commuting_" + usr_str + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")  
    
#    print G.number_of_nodes()  
#    print G.number_of_edges()  
    
    plt.clf()
    
    m = Basemap(llcrnrlon=-9, \
                    llcrnrlat=3.8, \
                    urcrnrlon=-1.5, \
                    urcrnrlat = 11, \
                    resolution = 'h', \
                    projection = 'tmerc', \
                    lat_0 = 7.38, \
                    lon_0 = -5.30)
   
    # read the shapefile archive
    s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')
    
    m.drawcoastlines()
    
    for u, v, d in G.edges(data=True):
        lo = []
        la = []   
        lo.append(lons[u])
        lo.append(lons[v])
        la.append(lats[u])
        la.append(lats[v])
        x, y = m(lo, la)
        linewidth7s = d['weight'] / max7s
        linewidth7s = linewidth7s + 0.17
        m.plot(x,y, linewidth= linewidth7s)
        
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/A/users/scaled/usr_commuting_" + usr_str + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")  
     
    return