'''
Created on Feb 11, 2013

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

from collections import defaultdict

def plot_gspan_res(G):
    
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
    

    for u, v, d in G.edges(data=True):
        lo = []
        la = []   
        lo.append(lons[u])
        lo.append(lons[v])
        la.append(lats[u])
        la.append(lats[v])
        x, y = m(lo, la)
        m.plot(x,y)
           
#    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/gSpan res/238.png" 
#    print(figure_name)
#    plt.savefig(figure_name, format = "png")  

    return plt

def gspan_res():

    file_name = "/home/sscepano/gSpan7s/all_users_238.tsv.fp"
    f = open(file_name, "r")
    
    G = nx.DiGraph()
    
    subpref_id = 238
    
    for line in f:
        elems = line.split(' ')
        
        if elems[0] == 't':
            plt = plot_gspan_res(G)
            G = nx.DiGraph()
            node_labels = defaultdict(int)
            continue
        
        if elems[0] == 'v':
            node_labels[int(elems[1])] = int(elems[2])
            continue
            
        if elems[0] == 'e':
            G.add_edge(node_labels[int(elems[1])], node_labels[int(elems[2])])
     
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/gSpan res/238.png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")   
     
    return

