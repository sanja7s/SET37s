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

from shapelib import ShapeFile
import dbflib
from matplotlib.collections import LineCollection
from matplotlib import cm

from collections import defaultdict

def plot_map(subpref_id):
    
    fig = plt.figure(subpref_id)
    #Custom adjust of the subplots
    plt.subplots_adjust(left=0.05,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
    ax = plt.subplot(111)
    
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
    
    shp = ShapeFile(r'/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE')
    dbf = dbflib.open(r'/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE')
    
    msg = "Out of bounds"
    color_col = []
    
    for npoly in range(shp.info()[0]):
        shpsegs = []
        shpinfo = []
        
        
        shp_object = shp.read_object(npoly)
        verts = shp_object.vertices()
        rings = len(verts)
        for ring in range(rings):
            lons, lats = zip(*verts[ring])
            x, y = m(lons, lats)
            shpsegs.append(zip(x,y))
            if ring == 0:
                shapedict = dbf.read_record(npoly)
            #print shapedict
            name = shapedict["ID_DEPART"]
            subpref_id2 = shapedict["ID_SP"]
            #color_col
            
            # add information about ring number to dictionary.
            shapedict['RINGNUM'] = ring+1
            shapedict['SHAPENUM'] = npoly+1
            shpinfo.append(shapedict)

        lines = LineCollection(shpsegs,antialiaseds=(1,))
        if subpref_id == subpref_id2:
            lines.set_facecolors('g')
        lines.set_edgecolors('k')
        lines.set_linewidth(0.3)
        ax.add_collection(lines)
    
    return m

def plot_gspan_res(G, subpref_id, color_val, m):

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
        m.plot(x,y, color = color_val)


    return plt

def gspan_res(subpref_id):
    
    #subpref_id = 159
    
    import matplotlib.pyplot as plt
    import matplotlib.colors as colors
    import matplotlib.cm as cmx
    import numpy as np
    
    # define some random data that emulates your indeded code:
    NCURVES = 100
    np.random.seed(101)
    values = range(NCURVES)
    
    jet = cm = plt.get_cmap('jet') 
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
    print scalarMap.get_clim()

    file_name = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/gSpan res/subpref/subprefs/10/all_users_" + str(subpref_id) + ".tsv.fp"
    #file_name = "/home/sscepano/gSpan7s/high_movers.tsv.fp"
    #file_name = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/gSpan64/low/1pct/low_movers.tsv.fp"
    f = open(file_name, "r")
    
    G = nx.DiGraph()
    
    m = plot_map(subpref_id)
    
    idx = 0
    
    for line in f:
        elems = line.split(' ')
        
        if elems[0] == 't':
            color_val = scalarMap.to_rgba(values[idx])
            plt = plot_gspan_res(G, subpref_id, color_val, m)
            G = nx.DiGraph()
            node_labels = defaultdict(int)
            idx += 1
            continue
        
        if elems[0] == 'v':
            node_labels[int(elems[1])] = int(elems[2])
            continue
            
        if elems[0] == 'e':
            G.add_edge(node_labels[int(elems[1])], node_labels[int(elems[2])])
            
     
    figure_name = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/gSpan res/subpref/" + str(subpref_id) + ".png" 
    #figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/gSpan res/high_movers.png" 
    #figure_name = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/gSpan res/low/1pct/low_movers.png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi = 500)   
    plt.clf()
     
    return


#r_done = [ 65, 194, 132, 154, 69, 39, 123, 171]
#r = [174, 52]

#for i in r:
#    gspan_res(i)

gspan_res(195)

#for i in range(1,255):
#    gspan_res(i)

