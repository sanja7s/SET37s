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


###########################################################################################

subpref_cluster3 = rd.read_in_subpref_assigned_3clusters()

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
    #print subpref_id
    #print name
    lines = LineCollection(shpsegs,antialiaseds=(1,))
    if subpref_cluster3[subpref_id] == 1:
        lines.set_facecolors('r')
    if subpref_cluster3[subpref_id] == 2:
        lines.set_facecolors('b')
    if subpref_cluster3[subpref_id] == 3:
        lines.set_facecolors('g')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/1/kmeans5args_3clusters.png',dpi=1000)
#plt.show()

###################################################################################################3

subpref_cluster2 = rd.read_in_subpref_assigned_2clusters() 

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
    if subpref_cluster2[subpref_id] == 1:
        lines.set_facecolors('r')
    if subpref_cluster2[subpref_id] == 2:
        lines.set_facecolors('b')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/1/kmeans5args_2clusters.png',dpi=1000)
#plt.show()


###################################################################################################3

subpref_cluster = rd.read_in_subpref_assigned_4clusters() 

fig = plt.figure(4)
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
    if subpref_cluster[subpref_id] == 1:
        lines.set_facecolors('r')
    if subpref_cluster[subpref_id] == 2:
        lines.set_facecolors('b')
    if subpref_cluster[subpref_id] == 3:
        lines.set_facecolors('g')
    if subpref_cluster[subpref_id] == 4:
        lines.set_facecolors('c')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/1/kmeans5args_4clusters.png',dpi=1000)



###################################################################################################3

subpref_cluster = rd.read_in_subpref_assigned_5clusters() 

fig = plt.figure(5)
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
    if subpref_cluster[subpref_id] == 1:
        lines.set_facecolors('r')
    if subpref_cluster[subpref_id] == 2:
        lines.set_facecolors('b')
    if subpref_cluster[subpref_id] == 3:
        lines.set_facecolors('g')
    if subpref_cluster[subpref_id] == 4:
        lines.set_facecolors('c')
    if subpref_cluster[subpref_id] == 5:
        lines.set_facecolors('m')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/1/kmeans5args_5clusters.png',dpi=1000)

###################################################################################################3

subpref_cluster = rd.read_in_subpref_assigned_6clusters() 

fig = plt.figure(6)
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
    if subpref_cluster[subpref_id] == 1:
        lines.set_facecolors('r')
    if subpref_cluster[subpref_id] == 2:
        lines.set_facecolors('b')
    if subpref_cluster[subpref_id] == 3:
        lines.set_facecolors('g')
    if subpref_cluster[subpref_id] == 4:
        lines.set_facecolors('c')
    if subpref_cluster[subpref_id] == 5:
        lines.set_facecolors('m')
    if subpref_cluster[subpref_id] == 5:
        lines.set_facecolors('y')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/1/kmeans5args_6clusters.png',dpi=1000)



###################################################################################################3

subpref_cluster = rd.read_in_subpref_assigned_7clusters() 

fig = plt.figure(7)
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
    if subpref_cluster[subpref_id] == 1:
        lines.set_facecolors('r')
    if subpref_cluster[subpref_id] == 2:
        lines.set_facecolors('b')
    if subpref_cluster[subpref_id] == 3:
        lines.set_facecolors('g')
    if subpref_cluster[subpref_id] == 4:
        lines.set_facecolors('c')
    if subpref_cluster[subpref_id] == 5:
        lines.set_facecolors('m')
    if subpref_cluster[subpref_id] == 6:
        lines.set_facecolors('y')
    if subpref_cluster[subpref_id] == 7:
        lines.set_facecolors('w')
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)
    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/1/kmeans5args_7clusters.png',dpi=1000)

