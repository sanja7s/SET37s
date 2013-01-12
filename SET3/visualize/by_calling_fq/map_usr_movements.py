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

def plot_movements(G, c):
    
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
    #m.fillcontinents()
    
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
    for subpref in range(1,255):
        lons[subpref] = subpref_coord[subpref][0]
        lats[subpref] = subpref_coord[subpref][1]
    
#    pos=nx.spring_layout(G) 
#    nx.draw(G, pos)
#    edge_labels=dict([((u,v,),d['weight'])
#        for u,v,d in G.edges(data=True)])
    
    if G.has_node(-1): 
        G.remove_node(-1)
    pos = {}
    
    max = 1
    for u,v,d in G.edges(data=True):
        if d['weight'] > max:
            max = d['weight']
            
    max = float(max)
        
    edge_width=[]
    for u,v,d in G.edges(data=True):
        edge_width.append(d['weight']/max)
    
#    pos=dict([((n,),m(lons[n], lats[n]))
#        for n in G.nodes()])
#   

     
    for node in G.nodes():
        print node
        x, y = m(lons[node], lats[node])
        pos.keys().append(node)
        pos[node] = (x, y)
    
        
    cmap=cm.get_cmap()
    
    #nx.draw_networkx_nodes(G, pos,  node_color='w', node_size=55,alpha=0.3, linewidths = 0.000001 ) 
    nx.draw_networkx_labels(G, pos,  font_size=7,alpha=0.7 )    
    nx.draw_networkx_edges(G, pos, arrows=False, alpha = 0.7, edge_vmin = 0, edge_vmax = 1, edge_color = edge_width, edge_cmap = cmap)
    #nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7.5, font_color = 'r')
    
    #plt.show()
    
    figure_name = "/home/sscepano/D4D res/allstuff/User movements graphs/" + c + "/png/subpref_usr_movements_" + c + ".png" 
    print(figure_name)
    plt.savefig(figure_name, format = "png")    
     
    return