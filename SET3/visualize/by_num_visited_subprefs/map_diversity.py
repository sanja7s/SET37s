'''
Created on Feb 20, 2013

@author: sscepano
'''

from analyze.by_num_visited_subprefs import diversity as d
from read_in import fq_data as rd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from collections import defaultdict, OrderedDict

import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.


def read_in_rg():
    
    subpref_rg = defaultdict(float)

    file_name = "/home/sscepano/D4D res/allstuff/diversity of travel/subpref_diversity_index.tsv"
    f = open(file_name, 'r')
    
    for line in f:
        subpref, rg = line.split('\t')
        subpref =  int(subpref)
        rg = float(rg[:-1])
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
    
    for subpref in rg.iterkeys():
        if subpref_num_usr[subpref] > 0:
            rg_scaled[subpref] = float((rg[subpref] - rg_min) / float(rg_max - rg_min))
        else:
            rg_scaled[subpref] = 1
    

    
    return rg_scaled


def map_diversity():
    
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
            #print shapedict
            name = shapedict["ID_DEPART"]
            subpref_id = shapedict["ID_SP"]
            num = ["%.2f" % rg[subpref_id]]
            # add information about ring number to dictionary.
            shapedict['RINGNUM'] = ring+1
            shapedict['SHAPENUM'] = npoly+1
            shpinfo.append(shapedict)
        #print subpref_id
        #print name
        lines = LineCollection(shpsegs,antialiaseds=(1,))
        lines.set_facecolors(str(rg[subpref_id]))
        lines.set_edgecolors('k')
        lines.set_linewidth(0.3)
        ax.add_collection(lines)
    
    plt.savefig('/home/sscepano/D4D res/allstuff/diversity of travel/diversity_map.png',dpi=500)
    
    return

#map_diversity()


def from_file_total_plot(file_name):
    
    # we will read values to this two arrays
    nits = []
    its = []
    
    # a loop where we populate those two arrays from the file
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        it, nit = line.split('\t')
        # nit je vrijednost diversity indexa
        nit = float(nit)
        # it je user ili subpref
        it = int(it)
        nits.append(nit)
        its.append(it)

#    mi = min(nits)
#    mx = max(nits)
#    print("Minimum usr diversity ", mi)
#    print("Maximum usr diversity ", mx)
#    
#    total_nit = float(sum(nits))
#    print("Total usr diversity ", total_nit)
#    
#    pdf_nits = defaultdict(int)
#    
#    # we count in a dictionary how many times each diversity index has appeared
#    for j in range(0, len(nits)):
#        pdf_nits[nits[j]] += 1
#        
#    ordered = OrderedDict(sorted(pdf_nits.items(), key=lambda t: t[0]))
#    
#    #print ordered
#    
#    nits7s = []
#    its7s = []
#    
#    test = 0
#    
#    for j in ordered.iterkeys():
#        nits7s.append(ordered[j]/500000.0)
#        test += ordered[j]/500000.0
#        its7s.append(j)
#        
#    print test
#
##    for j in ordered.iterkeys():
##        nits7s.append(ordered[j]/237.0)
##        test += ordered[j]/237.0
##        its7s.append(j)
#        
#    print test
        
############################################################################################################################
# THIS is to plot number of users pdf
############################################################################################################################

    plt.figure(7)

    #plt.plot(its7s, nits7s, linewidth=0.5, label= 'distribution of div index')
#    plt.xlabel('div index')
#    plt.ylabel('P(div index)')
#    plt.legend()   
    
    fig1 = plt.figure(1)
    ax = fig1.add_subplot(111)
    n, bins, rectangles = ax.hist(nits, 100, normed=True)
    plt.xlabel('subpref div index')
    plt.ylabel('frequency')
    plt.legend()   

    
    # this is if we want loglog lot, otheriwse comment and uncomment next line for regular plot file   
#    plt.yscale('log')
#    plt.xscale('log')

    #figure_name = "/home/sscepano/D4D res/allstuff/diversity of travel/diversity_total_hist.png"
    
    figure_name = "/home/sscepano/D4D res/allstuff/diversity of travel/diversity_subpref_hist.png"
          
    print(figure_name)
    plt.savefig(figure_name, format = "png", dpi=300)      
    
    return


#from_file_total_plot("/home/sscepano/D4D res/allstuff/diversity of travel/usr_diversity_index.tsv")
from_file_total_plot("/home/sscepano/D4D res/allstuff/diversity of travel/subpref_diversity_index.tsv")