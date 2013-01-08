'''
Created on Jan 7, 2013

@author: sscepano
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 7.

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

# read the file showing how many users we found per each subpref
file_name = '/home/sscepano/D4D res/ORGANIZED/SET3/Night Homes/Num_of_users_per_home_subpref.tsv'
f = open(file_name, 'r')

no_users = {}

for line in f:
    subpref, no = line.split('\t')
    subpref = int(subpref[:-1])
    no = int(no)
    no_users.keys().append(subpref)
    if subpref <> -1:
        no_users[subpref] = no

# read subpref center coordinates    
file_name2 = '/home/sscepano/DATA SET7S/D4D/SUBPREF_POS_LONLAT.TSV'
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

# data to plot on the map    
lons = []
lats = []
num = []

# if wanna plot number of users whose this is home subpref
for subpref in no_users.iterkeys():
    print(subpref)
    lons.append(subpref_coord[subpref][0])
    lats.append(subpref_coord[subpref][1])
    num.append(no_users[subpref])

# if wanna plot subpref ids only
#for subpref in range(1,256):
#    if subpref in [22, 32, 38, 49, 51, 72, 81, 83, 87, 88, 98, 105, 111, 112, 135, 136, 221, 239, 245, 255]:
#        lons.append(subpref_coord[subpref][0])
#        lats.append(subpref_coord[subpref][1])
#        num.append(subpref)    
    
x, y = m(lons, lats)
m.scatter(x, y, color='green')

for name, xc, yc in zip(num, x, y):
    # draw the pref name in a yellow (shaded) box
        plt.text(xc, yc, name)

# draw coast lines and fill the continents
m.drawcoastlines()
m.fillcontinents()

#plt.text(x, y, num)

m.plot()

f.close()
f2.close()

plt.show()
