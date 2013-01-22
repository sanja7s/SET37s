'''
Created on Jan 19, 2013

@author: sscepano
'''

from read_in import fq_data as rd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.

#subpref_avg_fq = rd.read_in_subpref_avg_fq()
gs1 = rd.read_in_gs1()

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
        x, y = m(lons, lats)
        shpsegs.append(zip(x,y))
        if ring == 0:
            shapedict = dbf.read_record(npoly)
        print shapedict
        name = shapedict["ID_DEPART"]
        subpref_id = shapedict["ID_SP"]
        num = ["%.2f" % gs1[subpref_id]]
#        for name, xc, yc in zip(num, x, y):
#            plt.text(xc, yc, name)
        #color_col
        
        # add information about ring number to dictionary.
        shapedict['RINGNUM'] = ring+1
        shapedict['SHAPENUM'] = npoly+1
        shpinfo.append(shapedict)
    #print subpref_id
    #print name
    lines = LineCollection(shpsegs,antialiaseds=(1,))
    lines.set_facecolors(str(1 - gs1[subpref_id]))
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)

    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/res/maps/2/gs/pca_10args_gs1.png',dpi=1000)
plt.show()