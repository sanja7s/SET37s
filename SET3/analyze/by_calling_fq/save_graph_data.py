'''
Created on Jan 12, 2013

@author: sscepano
'''
import networkx as nx
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

from visualize.by_calling_fq import map_usr_movements as v
from visualize.by_commuting_patterns import map_commutes as v2

from read_in import fq_data as rd
from read_in import  gSpan_res as rd2

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 5.5
import networkx as nx
import matplotlib.colors as colors
import matplotlib.cm as cm
from math import log

from collections import defaultdict

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 5.5
import networkx as nx
import matplotlib.colors as colors
import matplotlib.cm as cm
from math import log

from collections import defaultdict

from shapelib import ShapeFile
import dbflib
from matplotlib.collections import LineCollection
from matplotlib import cm

def data_2_file(G):
    
    return

def plot_gspan_res(G, subpref_id, color_val):
    
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

    file_name = "/home/sscepano/gSpan7s/all_users_" + str(subpref_id) + ".tsv.fp"
    f = open(file_name, "r")
    
    G = nx.DiGraph()
    
    
    idx = 0
    
    for line in f:
        elems = line.split(' ')
        
        if elems[0] == 't':
            color_val = scalarMap.to_rgba(values[idx])
            plt = plot_gspan_res(G, subpref_id, color_val)
            G = nx.DiGraph()
            node_labels = defaultdict(int)
            idx += 1
            continue
        
        if elems[0] == 'v':
            node_labels[int(elems[1])] = int(elems[2])
            continue
            
        if elems[0] == 'e':
            G.add_edge(node_labels[int(elems[1])], node_labels[int(elems[2])])
            
     
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/gSpan res/" + str(subpref_id) + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi = 500)   
    plt.clf()
     
    return

def graph2_file3(G):
    
#    movements_stats = np.zeros(500001)
#    
#    for i in range(500001):
#        for u,v,d in G[i].edges(data=True):
#            movements_stats[i] += d['weight']
#    
#    fig2 = plt.figure(2)
#    ax = fig2.add_subplot(111)
#    nn, bins, rectangles = ax.hist(movements_stats, 100, normed=True)
#    
#    plt.xlabel('# of movements')
#    plt.ylabel('fq of # num movements')
#    plt.legend()   
##    plt.yscale('log')
##    plt.xscale('log')
#    
#    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/usr_movements_hist.png" 
#    print(figure_name)
#    plt.savefig(figure_name, format = "png")  
#    plt.show() 
    
#    file_name = "movements_fq.tsv"
#    f = open(file_name, 'w')
    
#    for i in range(len(movements_stats)):
#        f.write(str(i) + '\t' + str(movements_stats2[i]) + '\n')

#    for subpref_id in range(255):
#
#        #subpref_id = 237
#    
#        usrs_list = rd.read_in_subpref_users(subpref_id)
#        
#        file_name2 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/subprefs/all_users_" + str(subpref_id) + ".tsv"
#        f2 = open(file_name2, "w")
#        j = 0
#        
#        for i in range(500001):
#            if usrs_list[i] == 1:
#                j += 1
#                f2.write('t # ' + str(j) + '\n')
#                
#                max_node = 0
#                min_node = 256
#                
#                nodes_order = defaultdict(int)
#                
#                cnt = 0
#                
#                for node in G[i].nodes():
#                    if node <> -1:
#                        if node > max_node:
#                            max_node = node
#                        if node < min_node:
#                            min_node = node
#                        nodes_order[node] = cnt
#                        cnt += 1 
#                            
#                
#                for node in G[i].nodes():
#                    if node <> -1:
#                        f2.write('v ' + str(nodes_order[node]) + ' ' + str(node) + '\n')
#                
#                for u,v,d in G[i].edges(data=True):
#                    if u <> - 1 and v <> -1 and u <> v:
#                        if d['weight'] <= 10:
#                            weight = 0
#                        elif d['weight'] <= 100:
#                            weight = 10
#                        elif d['weight'] <= 1000:
#                            weight = 100
#                        elif d['weight'] <= 10000:
#                            weight = 1000
#                        else:
#                            weight = 10000
#                        f2.write('e ' + str(nodes_order[u]) + ' ' + str(nodes_order[v]) + ' ' + str(weight) + '\n')
#                
#        print j

#    file_name3 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/ALL/all_users.tsv"
#    f3 = open(file_name3, "w")
#
#    j = 0
#    for i in range(500001):
#            j += 1
#            f3.write('t # ' + str(j) + '\n')
#            
#            max_node = 0
#            min_node = 256
#            
#            nodes_order = defaultdict(int)
#            
#            cnt = 0
#            
#            for node in G[i].nodes():
#                if node <> -1:
#                    if node > max_node:
#                        max_node = node
#                    if node < min_node:
#                        min_node = node
#                    nodes_order[node] = cnt
#                    cnt += 1 
#                        
#            
#            for node in G[i].nodes():
#                if node <> -1:
#                    f3.write('v ' + str(nodes_order[node]) + ' ' + str(node) + '\n')
#            
#            for u,v,d in G[i].edges(data=True):
#                if u <> - 1 and v <> -1 and u <> v:
#                    if d['weight'] <= 10:
#                        weight = 0
#                    elif d['weight'] <= 100:
#                        weight = 10
#                    elif d['weight'] <= 1000:
#                        weight = 100
#                    elif d['weight'] <= 10000:
#                        weight = 1000
#                    else:
#                        weight = 10000
#                    f3.write('e ' + str(nodes_order[u]) + ' ' + str(nodes_order[v]) + ' ' + str(weight) + '\n')
#            
#    print j

#    minval = 1
#    maxval = 1
#
#    distr_num_of_edges = np.zeros(500001)
#    
#    for i in range(500001):
#        testval = G[i].number_of_edges()
#        if minval > testval:
#            minval = testval
#        if maxval < testval:
#            maxval = testval
#        distr_num_of_edges[i] = testval
#            
#    print minval
#    print maxval
#    
#    print distr_num_of_edges
#    
#    for i in range(500001):
#        testval = G[i].number_of_edges()
#        
#        if testval <= 10:
#            save_users_graphs_for_input_gspan("/home/sscepano/D4D res/allstuff/USER GRAPHS stats/lowmediumhigh/low_movers.tsv",G[i], i)
#        elif testval <= 100:
#            save_users_graphs_for_input_gspan("/home/sscepano/D4D res/allstuff/USER GRAPHS stats/lowmediumhigh/medium_movers.tsv",G[i], i)
#        else:
#            save_users_graphs_for_input_gspan("/home/sscepano/D4D res/allstuff/USER GRAPHS stats/lowmediumhigh/high_movers.tsv",G[i], i)
    
#    fig3 = plt.figure(3)
#    ax = fig3.add_subplot(111) 
#    nn, bins, rectangles = ax.hist(distr_num_of_edges, 100, normed=True)
#    
#    plt.xlabel('# of edges')
#    plt.ylabel('fq of # num edges')
#    plt.legend()   
#    plt.yscale('log')
#    plt.xscale('log')
#    
#    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/usr_edges_loglog.png" 
#    print(figure_name)
#    plt.savefig(figure_name, format = "png")  
#    plt.show() 

    #rd2.gspan_res()
    
#    r = [123, 171 ]
#    
#    for i in [237,238,220,60,144, 65, 194, 132, 154, 69, 39]:
#        gspan_res(i)
    
    
#    file_name1 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/user_number_of_edges_v1.tsv"
#    file_name2 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/user_number_of_nodes_v1.tsv"
#    file_name3 = "/home/sscepano/D4D res/allstuff/USER GRAPHS stats/user_number_of_displacements_v1.tsv"
#    
#    f1 = open(file_name1, "w")
#    f2 = open(file_name2, "w")
#    f3 = open(file_name3, "w")
#    
#    for i in range(500001):
#        if i == 3:
#            print i, G[i].nodes()
#        f1.write(str(i) + '\t' + str(G[i].number_of_edges()) + '\n')
#        f2.write(str(i) + '\t' + str(G[i].number_of_nodes()) + '\n')
#        sum_edge_weight = 0
#        for u,v,d in G[i].edges(data=True):
#            sum_edge_weight += d['weight']
#        f3.write(str(i) + '\t' + str(sum_edge_weight) + '\n')
    
    
    return

def save_users_graphs_for_input_gspan(file_name, G, j):

    f3 = open(file_name, "a")
    f3.write('t # ' + str(j) + '\n')
    
    max_node = 0
    min_node = 256
    
    nodes_order = defaultdict(int)
    
    cnt = 0
    
    for node in G.nodes():
        if node <> -1:
            if node > max_node:
                max_node = node
            if node < min_node:
                min_node = node
            nodes_order[node] = cnt
            cnt += 1 
                
    
    for node in G.nodes():
        if node <> -1:
            f3.write('v ' + str(nodes_order[node]) + ' ' + str(node) + '\n')
    
    for u,v,d in G.edges(data=True):
        if u <> - 1 and v <> -1 and u <> v:
            if d['weight'] <= 10:
                weight = 0
            elif d['weight'] <= 100:
                weight = 10
            elif d['weight'] <= 1000:
                weight = 100
            elif d['weight'] <= 10000:
                weight = 1000
            else:
                weight = 10000
            f3.write('e ' + str(nodes_order[u]) + ' ' + str(nodes_order[v]) + ' ' + str(weight) + '\n')
    
    return

def graph2_file2(G, usr):
    
  
    # this one is for patterns
    
#    fig = figure()
#    axes = fig.add_subplot(111)
    
    #nx.write_gml(G, "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/1/usr_movements_" + str(usr) + ".gml")
    
#    pos=nx.spring_layout(G) 
#    nx.draw(G, pos, ax=axes)
#    edge_labels=dict([((u,v,),d['weight'])
#        for u,v,d in G.edges(data=True)])
#    nx.draw_networkx_edge_labels(G, pos, edge_labels,  ax=axes)
    
    #plt.show()
    
#    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/Graph files gml/usr/usr_movements_" + str(usr) + ".png" 
#    print(figure_name)
#    plt.savefig(figure_name, format = "png")    
    
  
    
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



def map_communities_and_commutes(G):
    
    G_mod = nx.read_gml("/home/sscepano/D4D res/allstuff/User movements graphs/commuting patterns/1/total_commuting_G_scaled_weights_11COM_713_7115.gml")
    
    col = [str]*256
    for i in range(256):
        col[i] = 'w'
    
    for node in G_mod.nodes_iter(data=True):
        #print node[1]['label']
        col_gephi = node[1]['graphics']['fill']
        while (len(col_gephi) < 7):
            col_gephi += '0'
        subpref_gephi = int(float(node[1]['label']))
        print subpref_gephi, col_gephi
        col[subpref_gephi] = col_gephi   
    #print col
    
    plt.clf()
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
    
    from shapelib import ShapeFile
    import dbflib
    from matplotlib.collections import LineCollection
    from matplotlib import cm
    
    shp = ShapeFile(r'/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE')
    dbf = dbflib.open(r'/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE')
    
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
            subpref_id = shapedict["ID_SP"]
            # add information about ring number to dictionary.
            shapedict['RINGNUM'] = ring+1
            shapedict['SHAPENUM'] = npoly+1
            shpinfo.append(shapedict)
        #print subpref_id
        #print name
        lines = LineCollection(shpsegs,antialiaseds=(1,))
        lines.set_facecolors(col[subpref_id])
        lines.set_edgecolors('gray')
        lines.set_linewidth(0.3)
        ax.add_collection(lines)
    
    m.drawcoastlines()
    
    plt.show()

#    # data to plot on the map    
#    lons = [int]*256
#    lats = [int]*256
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
#        node1 = G.nodes(data=True)[u][1]['label']
#        node2 = G.nodes(data=True)[v][1]['label']
#        print u, node1
#        print v, node2
#        print d
#        scaled_weight[node1][node2] = (d['weight'] - min7s) / (max7s - min7s)
#        
##    for u,v,d in G.edges(data=True):
##        print u,v,d
##        node1 = G.nodes(data=True)[u][1]['label']
##        node2 = G.nodes(data=True)[v][1]['label']
##        print node1, G_mod.nodes(data=True)[u][1]['label']
##        print node2, G_mod.nodes(data=True)[v][1]['label']
#    
# 
#    for u, v, d in G.edges(data=True):
#        node1 = G.nodes(data=True)[u][1]['label']
#        node2 = G.nodes(data=True)[v][1]['label']
#        print node1
#        print node2
#        lo = []
#        la = []   
#        print u
#        print v
#        lo.append(lons[node1])
#        lo.append(lons[node2])
#        la.append(lats[node1])
#        la.append(lats[node2])
#        #m.drawgreatcircle(lons[u],lats[u], lons[v],lats[v])
#        x, y = m(lo, la)
#        #linewidth7s = d['weight']
#        #linewidth7s = d['weight'] / max7s
#        #lons, lats = n.meshgrid(lo,la)
#        linewidth7s = scaled_weight[node1][node2] * 7 + 0.2
#        m.plot(x,y, 'b', linewidth = linewidth7s)
#        #wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
#        #mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
#        #m.contour(x,y,linewidth=linewidth7s)
#        #m.quiver(x,y,lons, lats, latlon=True)
##        if linewidth7s > 1:
##            print linewidth7s
#        
#     
#    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/commuting patterns/1/maps/mod_classes_SCALED_11COM_713_7115.png"
#    print(figure_name)
#    plt.savefig(figure_name, format = "png",dpi=1000) 
    
    return

def read_in_subpref_num_users():
    
    subpref_num_usr = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes/Num_of_users_per_home_subpref.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, num_usr = line.split('\t')
        subpref =  int(subpref[:-1])
        num_usr = int(num_usr)
        subpref_num_usr[subpref] = num_usr
             
    return  subpref_num_usr



def save_commuting_graph():
    
#    print G.nodes()
#    print G.edges(data=True)
#    
#    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/1/total_commuting_G.gml")
#    
#    print GA.nodes()
#    print GA.edges(data=True)
#    
#    nx.write_gml(G, "/home/sscepano/D4D res/allstuff/User movements graphs/communting patterns/1/total_commuting_GA.gml")

    #v.map_commuting_all(G)
    
    #map_communities_and_commutes(G)
    
#    G = nx.read_gml("/home/sscepano/D4D res/allstuff/User movements graphs/commuting patterns/1/total_commuting_G.gml")
#    
#    G1 = process_weights(G)
#    nx.write_gml(G1, "/home/sscepano/D4D res/allstuff/User movements graphs/commuting patterns/1/total_commuting_G_scaled_weights.gml")
#    
#    print G1.edges(data=True)

    G1 = nx.read_gml("/home/sscepano/D4D res/allstuff/User movements graphs/commuting patterns/1/total_commuting_G_scaled_weights.gml")
    
#    print G1.nodes(data=True)
#    
#    print G1.nodes(data=True)[1][1]['label']

    map_communities_and_commutes(G1)
    
    return G1

def process_weights(G):
    
    G1 = nx.DiGraph()
    subpref_usrs = read_in_subpref_num_users()
    
    for u,v,d in G.edges(data=True):
        current_weight = d['weight']
        if subpref_usrs[u] > 0 and subpref_usrs[v] > 0:
            new_weight = (current_weight / float(subpref_usrs[u] * subpref_usrs[v])) * 1000000.0
            #G1[u][v]['weight'] = new_weight
            G1.add_edge(u, v, weight=new_weight)
    
    return G1




#save_commuting_graph()