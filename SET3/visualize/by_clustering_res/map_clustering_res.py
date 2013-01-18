'''
Created on Jan 18, 2013

@author: sscepano
'''
from read_in import clustering_results as rd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.

subpref_cluster = rd.read_in_subpref_assigned_clusters()

fig = plt.figure(1)
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

from shapelib import ShapeFile
import dbflib
from matplotlib.collections import LineCollection
from matplotlib import cm

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
    print subpref_id
    print name
    lines = LineCollection(shpsegs,antialiaseds=(1,))
    if subpref_cluster[subpref_id][1] == 1:
        lines.set_facecolors('r')
    if subpref_cluster[subpref_id][1] == 2:
        lines.set_facecolors('b')
    if subpref_cluster[subpref_id][1] == 3:
        lines.set_facecolors('g')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/clustering_divion1_3clusters.png',dpi=1000)
#plt.show()

###################################################################################################3

fig = plt.figure(2)
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
    print subpref_id
    print name
    lines = LineCollection(shpsegs,antialiaseds=(1,))
    if subpref_cluster[subpref_id][0] == 1:
        lines.set_facecolors('r')
    if subpref_cluster[subpref_id][0] == 2:
        lines.set_facecolors('b')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/clustering_divion1_2_clusters.png',dpi=1000)
#plt.show()