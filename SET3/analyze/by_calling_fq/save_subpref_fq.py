'''
Created on Jan 30, 2013

@author: sscepano
'''
from collections import defaultdict, OrderedDict

def data_2_file(data):
    
    fq = defaultdict(float)
    
    total_hours = 24 * 7 * 20

    for subpref in data.iterkeys():
        fq[subpref] = float(data[subpref]) / float(total_hours)
#    
#    file_out = '/home/sscepano/D4D res/allstuff/CLUSTERING/subpref no home res/Subprefs_and_their_total_calls_number_no_home.tsv'
#    f = open(file_out, 'w')
#    
#    file_out2 = '/home/sscepano/D4D res/allstuff/CLUSTERING/subpref no home res/Subprefs_and_their_calling_fq_no_home.tsv'
#    f2 = open(file_out2, 'w')
#    
#    for subpref in data.iterkeys():
#        f.write(str(subpref) + '\t' + str(data[subpref]) + '\n')
#        f2.write(str(subpref) + '\t' + str(fq[subpref]) + '\n')
        
    fq_scaled = get_scaled_fq(fq)
#    file_out3 = '/home/sscepano/D4D res/allstuff/CLUSTERING/subpref no home res/Subprefs_and_their_scaled_fq.tsv'
#    f3 = open(file_out3, 'w')
#    
#    for subpref in fq_scaled.iterkeys():
#        f3.write(str(subpref) + '\t' + str(fq_scaled[subpref]) + '\n')
#      
#    f.close()
#    f2.close()
#    f3.close()
    
    print fq_scaled 
    
    map_fq(fq_scaled)
    
    return


def get_scaled_fq(data):
    
    fq_scaled = defaultdict(float)
    
    fq_max = 0
    fq_min = 50
    
    for subpref in data.iterkeys():
        if data[subpref] > fq_max:
            fq_max = data[subpref]
        if data[subpref] < fq_min:
            fq_min = data[subpref]
            
    for subpref in data.iterkeys():
        fq_scaled[subpref] = (data[subpref] - fq_min) / (fq_max - fq_min)
     
    return fq_scaled



def map_fq(fq_scaled):
    
    print fq_scaled
    
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    
    import matplotlib as mpl
    mpl.rcParams['font.size'] = 10.
    mpl.rcParams['axes.labelsize'] = 8.
    mpl.rcParams['xtick.labelsize'] = 6.
    mpl.rcParams['ytick.labelsize'] = 6.
    
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
            #num = ["%.2f" % data[subpref_id]]
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
        #print float("%.7f" % fq_scaled[subpref_id])
        lines.set_facecolors(str(1.0 - fq_scaled[str(subpref_id)]))
        lines.set_edgecolors('k')
        lines.set_linewidth(0.3)
        ax.add_collection(lines)
    
        
    plt.savefig('/home/sscepano/D4D res/allstuff/CLUSTERING/subpref no home res/scaled_subpref_Calling_fq2.png',dpi=1000)
    #plt.show()
    
    return