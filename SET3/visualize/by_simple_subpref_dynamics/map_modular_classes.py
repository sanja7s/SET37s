'''
Created on Jan 23, 2013

@author: sscepano
'''
import networkx as nx

G = nx.read_gml("/home/sscepano/D4D res/allstuff/simple dynamics/v1/cleaned_mod_v1.gml")
col = [str]*256

for i in range(256):
    col[i] = 'w'

for node in G.nodes_iter(data=True):
    #print node[1]['label']
    col_gephi = node[1]['graphics']['fill']
    while (len(col_gephi) < 7):
        col_gephi += '0'
    col[int(float(node[1]['label']))] = col_gephi
    
    
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.

from shapelib import ShapeFile
import dbflib
from matplotlib.collections import LineCollection
from matplotlib import cm


###########################################################################################

fig = plt.figure(3)
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
#        if max(lons) > 721. or min(lons) < -721. or max(lats) > 91. or min(lats) < -91:
#            raise ValueError,msg
        x, y = m(lons, lats)
        shpsegs.append(zip(x,y))
        if ring == 0:
            shapedict = dbf.read_record(npoly)
        #print shapedict
        name = shapedict["ID_DEPART"]
        subpref_id = shapedict["ID_SP"]
        #color_col
        
        # add information about ring number to dictionary.
        shapedict['RINGNUM'] = ring+1
        shapedict['SHAPENUM'] = npoly+1
        shpinfo.append(shapedict)
    #print subpref_id
    #print name
    lines = LineCollection(shpsegs,antialiaseds=(1,))
    lines.set_facecolors(col[subpref_id])
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/simple dynamics/v1/cleaned_mod_v1.png',dpi=1000)
#plt.show()

###################################################################################################3
            