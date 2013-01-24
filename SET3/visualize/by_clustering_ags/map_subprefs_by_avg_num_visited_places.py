'''
Created on Jan 24, 2013

@author: sscepano
'''
from read_in import fq_data as rd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from collections import defaultdict

import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.

def read_in_rg():
    
    subpref_rg = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/subpref_avg_num_visited_pl.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, rg = line.split('\t')
        subpref =  int(subpref)
        rg = float(rg)
        subpref_rg[subpref] = rg
        
    return subpref_rg

def read_in_subpref_num_users():
    
    subpref_num_usr = defaultdict(float)
    
    file_name = "/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes/Num_of_users_per_home_subpref.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, num_usr = line.split('\t')
        subpref =  int(subpref[:-1])
        num_usr = int(num_usr)
        subpref_num_usr[subpref] = num_usr
             
    return subpref_num_usr  

def get_scaled_rg():
    
    rg = read_in_rg()
    rg_scaled = defaultdict(float)
    subpref_num_usr = read_in_subpref_num_users()
    
    rg_max = 0
    rg_min = 50
    
    for subpref in rg.iterkeys():
        if subpref_num_usr[subpref] > 0:
            if rg[subpref] > rg_max:
                rg_max = rg[subpref]
            if rg[subpref] < rg_min:
                rg_min = rg[subpref]
            
#    print rg_max
#    print rg_min        
    
    for subpref in rg.iterkeys():
        if subpref_num_usr[subpref] > 0:
            rg_scaled[subpref] = (rg[subpref] - rg_min) / (rg_max - rg_min)
    
#    for subpref in rg.iterkeys():
#        if subpref_num_usr[subpref] > 0:        
#            print subpref
#            print rg[subpref]
#            print rg_scaled[subpref]
    
    return rg_scaled

#get_scaled_rg()

#subpref_avg_fq = rd.read_in_subpref_avg_fq()
rg = get_scaled_rg()
 
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
        num = ["%.2f" % rg[subpref_id]]
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
    lines.set_facecolors(str(1 - rg[subpref_id]))
    lines.set_edgecolors('k')
    lines.set_linewidth(0.3)
    ax.add_collection(lines)

    
plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/subpref res/maps/grayscale_num_visited_pl_map.png',dpi=1000)
#plt.show()
