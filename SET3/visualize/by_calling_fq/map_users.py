'''
Created on Jan 2, 2013

@author: sscepano
'''
# this module uses division by users into h, m, l frequency callers and plots them in 3 colors on a map
# low: yellow, medium: green and high: red
# we want to see if there is any spatial distribution, or perhaps some other related to the calling fq

import shapefile
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as n
mpl.rcParams['font.size'] = 6.5


###########################################################################################################################

file_name_fq_orig = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/Usr_call_fq python.tsv"
f_fq_orig = open(file_name_fq_orig, 'r')

file_name_fq = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/Usr_div_by_call_fq python.tsv"
f_fq = open(file_name_fq, 'r')

file_name_subpref = '/home/sscepano/D4D res/ORGANIZED/SET3/Users_divided_by_home_subprefALL.tsv'
f_subpref = open(file_name_subpref, 'r')

# read users and their exact fq
users_calling_fq = n.zeros(500001)
for line in f_fq_orig:
    usr, fq = line.split('\t')
    usr = int(usr)
    fq = float(fq[:-1])
    users_calling_fq[usr] = fq

# read users for which we found the defined frequency ranges (hand-made rule is: low fq < 0.08; medium 0.08 <= fq <= 0.3; high fq > 0.3)
users_by_calling_fq = n.zeros(500001,dtype=n.character)
for line in f_fq:
    usr, fq = line.split('\t')
    usr = int(usr)
    fq = fq[:-1]
    users_by_calling_fq[usr] = fq

users_by_calling_fq_per_subpref = {}
subpref_avg_fq = n.zeros(256)
for subpref in range(1, 256):
    users_by_calling_fq_per_subpref[subpref] = {'l': 0, 'm': 0, 'h': 0}
for line in f_subpref:
    avg_fq = 0
    line_elems = line.split('\t')
    subpref = int(line_elems[0][:-1])
    if subpref <> -1:
        users_by_calling_fq_per_subpref.keys().append(subpref)
        for i in range (1, len(line_elems)-2):
            usr = int(line_elems[i])
            fq = users_by_calling_fq[usr]
            fq_orig = users_calling_fq[usr]
            avg_fq += fq_orig
            users_by_calling_fq_per_subpref[subpref][fq] += 1
        print line_elems[len(line_elems)-2]
        usr = int(line_elems[len(line_elems)-2])
        fq = users_by_calling_fq[usr]
        fq_orig = users_calling_fq[usr]
        avg_fq += fq_orig
        users_by_calling_fq_per_subpref[subpref][fq] += 1
        subpref_avg_fq[subpref] = avg_fq / float((len(line_elems)-1))
    
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

f_subpref.close()
f_fq.close()
f2.close()


###########################################################################################################################

m = Basemap(llcrnrlon=-9, \
                llcrnrlat=3.8, \
                urcrnrlon=-1.5, \
                urcrnrlat = 11, \
                resolution = 'h', \
                projection = 'tmerc', \
                lat_0 = 7.38, \
                lon_0 = -5.30)

figure_name_h = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/map by fq calling/High_fq_callers_percent.png"
figure_name_m = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/map by fq calling/Medium_fq_callers_percent.png"
figure_name_l = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/map by fq calling/Low_fq_callers_percent.png"
figure_name_avg = "/home/sscepano/D4D res/allstuff/SET3 frequent callers from python/map by fq calling/Avg_calling_fq.png"
print(figure_name_h,figure_name_m,figure_name_l,figure_name_avg)
    

# read the shapefile archive
s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')

# draw coast lines and fill the continents
m.drawcoastlines()
#m.fillcontinents()

# data to plot on the map    
lons = []
lats = []
num = []

# if wanna plot number of users whose this is home subpref
for subpref in range(1,256):
    lons.append(subpref_coord[subpref][0])
    lats.append(subpref_coord[subpref][1])
    total = users_by_calling_fq_per_subpref[subpref]['h'] + users_by_calling_fq_per_subpref[subpref]['m'] + users_by_calling_fq_per_subpref[subpref]['l']
    if total <> 0:
        pct = int((float(users_by_calling_fq_per_subpref[subpref]['h']) / float(total)) * 100)
    else:
        pct = 0
    num.append(pct)
 
x, y = m(lons, lats)
m.scatter(x, y, color='red')

for name, xc, yc in zip(num, x, y):
    plt.text(xc, yc, name)

plt.savefig(figure_name_h, format = "png")    

plt.clf()    

# read the shapefile archive
s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')

# data to plot on the map    
lons = []
lats = []
num = []

# if wanna plot number of users whose this is home subpref
for subpref in range(1,256):
    lons.append(subpref_coord[subpref][0])
    lats.append(subpref_coord[subpref][1])
    total = users_by_calling_fq_per_subpref[subpref]['h'] + users_by_calling_fq_per_subpref[subpref]['m'] + users_by_calling_fq_per_subpref[subpref]['l']
    if total <> 0:
        pct = int((float(users_by_calling_fq_per_subpref[subpref]['m']) / float(total)) * 100)
    else:
        pct = 0
    num.append(pct)
 
x, y = m(lons, lats)
m.scatter(x, y, color='green')

for name, xc, yc in zip(num, x, y):
    plt.text(xc, yc, name)
    
m.drawcoastlines()

plt.savefig(figure_name_m, format = "png")        

plt.clf()   

# read the shapefile archive
s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')

# data to plot on the map    
lons = []
lats = []
num = []

# if wanna plot number of users whose this is home subpref
for subpref in range(1,256):
    lons.append(subpref_coord[subpref][0])
    lats.append(subpref_coord[subpref][1])
    total = users_by_calling_fq_per_subpref[subpref]['h'] + users_by_calling_fq_per_subpref[subpref]['m'] + users_by_calling_fq_per_subpref[subpref]['l']
    if total <> 0:
        pct = int((float(users_by_calling_fq_per_subpref[subpref]['l']) / float(total)) * 100)
    else:
        pct = 0
    num.append(pct)
 
x, y = m(lons, lats)
m.scatter(x, y, color='yellow')

m.drawcoastlines()

for name, xc, yc in zip(num, x, y):
    plt.text(xc, yc, name)

plt.savefig(figure_name_l, format = "png")       

plt.clf()   

##############################################################################################################################3

# read the shapefile archive
s = m.readshapefile('/home/sscepano/DATA SET7S/D4D/SubPrefecture/GEOM_SOUS_PREFECTURE', 'subpref')

# data to plot on the map    
lons = []
lats = []
num = []

# if wanna plot number of users whose this is home subpref
for subpref in range(1,256):
    lons.append(subpref_coord[subpref][0])
    lats.append(subpref_coord[subpref][1])
    float_label = ('%.2f' % subpref_avg_fq[subpref]).rstrip('0').rstrip('.')
    num.append(float_label)
 
x, y = m(lons, lats)
m.scatter(x, y, color='blue')

m.drawcoastlines()

for name, xc, yc in zip(num, x, y):
    plt.text(xc, yc, name)

plt.savefig(figure_name_avg, format = "png")       
