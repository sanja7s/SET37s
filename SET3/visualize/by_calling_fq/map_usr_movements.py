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

def plot_commuting_patterns(G, usr, is_subpref=False):
    
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
        linewidth7s = linewidth7s * 7
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
    
    if is_subpref:
        figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/ALL/subprefs/non-scaled/subpref_commuting_" + usr_str + ".png" 
    else:
        figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/ALL/users/non-scaled/usr_commuting_" + usr_str + ".png" 
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
        linewidth7s = linewidth7s + 0.2
        m.plot(x,y, linewidth= linewidth7s)
    
    if is_subpref:
        figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/ALL/subprefs/scaled/subpref_commuting_" + usr_str + ".png" 
    else:    
        figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/ALL/users/scaled/usr_commuting_" + usr_str + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")  
     
    return


from collections import defaultdict

def get_scaled(x):
    
    x_scaled = [float]*len(x)
    
    x_max = 0
    x_min = 50
    
    for i in range(len(x)):
        if x[i] > x_max:
            x_max = x[i]
        if x[i] < x_min:
            x_min = x[i]  
    
    for i in range(len(x)):
        x_scaled[i] = (x[i] - x_min) / (x_max - x_min)
    
    return x_scaled

def map_commutning_all(G, GA):
    
#    plt.clf()
#    
#    m = Basemap(llcrnrlon=-9, \
#                    llcrnrlat=3.8, \
#                    urcrnrlon=-1.5, \
#                    urcrnrlat = 11, \
#                    resolution = 'h', \
#                    projection = 'tmerc', \
#                    lat_0 = 7.38, \
#                    lon_0 = -5.30)
#   
#    # read the shapefile archive
#    s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')
#    
#    m.drawcoastlines()
#
#    # data to plot on the map    
#    lons = [int]*256
#    lats = [int]*256
#    num = []
#    
#    # read in coordinates fo subprefs
#    file_name2 = "/home/sscepano/DATA SET7S/D4D/SUBPREF_POS_LONLAT.TSV"
#    f2 = open(file_name2, 'r')
#    
#    # read subpref coordinates
#    subpref_coord = {}
#    for line in f2:
#        subpref_id, lon, lat = line.split('\t')
#        lon = float(lon)
#        lat = float(lat)
#        subpref_id = int(subpref_id)
#        subpref_coord.keys().append(subpref_id)
#        subpref_coord[subpref_id] = (lon, lat)
#    
#    f2.close()
#    
#    # if wanna plot number of users whose this is home subpref
#    for subpref in range(1,256):
#        lons[subpref] = subpref_coord[subpref][0]
#        lats[subpref] = subpref_coord[subpref][1]
#    
#    
#    if G.has_node(-1): 
#        G.remove_node(-1)
#
#    max7s = 1
#    min7s = 1
#    for u,v,d in G.edges(data=True):
#        if d['weight'] > max7s:
#            max7s = d['weight']
#        if d['weight'] < min7s:
#            min7s = d['weight']
#            
#    max7s = float(max7s)
#    print max7s
#    print min7s
#    
#    scaled_weight = defaultdict(int)
#    for i in range(256):
#        scaled_weight[i] = defaultdict(int)
#    
#    for u,v,d in G.edges(data=True):
#        scaled_weight[u][v] = (d['weight'] - min7s) / (max7s - min7s)
#    
#    #scaled_weight = get_scaled(scaled_weight)
#        
##    edge_width=[]
##    for u,v,d in G.edges(data=True):
##        edge_width.append(d['weight'])
#        #print d['weight']
#    
##    pos=dict([((n,),m(lons[n], lats[n]))
##        for n in G.nodes()])
##   
#     
##    for node in G.nodes():
##        #print node
##        x, y = m(lons[node], lats[node])
##        pos.keys().append(node)
##        pos[node] = (x, y)
#    
# 
#    for u, v, d in G.edges(data=True):
#        lo = []
#        la = []   
#        lo.append(lons[u])
#        lo.append(lons[v])
#        la.append(lats[u])
#        la.append(lats[v])
#        x, y = m(lo, la)
#        #linewidth7s = d['weight']
#        #linewidth7s = d['weight'] / max7s
#        linewidth7s = scaled_weight[u][v] * 6.5 + 0.15
#        m.plot(x,y, linewidth= linewidth7s)
#        if linewidth7s > 1:
#            print linewidth7s
#        
#     
#    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/commuting patterns/1/maps/total_commuting7s.png"
#    print(figure_name)
#    plt.savefig(figure_name, format = "png",dpi=1000)  
#    
    
    return
