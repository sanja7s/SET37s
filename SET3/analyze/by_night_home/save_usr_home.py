'''
Created on Jan 7, 2013

@author: sscepano
'''

from collections import defaultdict, OrderedDict

# we save from data read in through __main__ the night/total home and for all subprefs we save users who have the home in those

def data_to_files(data, total = True):

    home = defaultdict(int)
    home_simple = defaultdict(int)
    
    testi = 0

    for usr in data.iterkeys():
        if data[usr] <> 0:
            testi += 1
            home[usr] = OrderedDict(sorted(data[usr].items(), key=lambda t: t[1], reverse=True)) 
    
    if total == True:
        fileout = 'Users_and_their_homes_total.tsv'
    else:                
        fileout = 'Users_and_their_homes.tsv'
    f = open(fileout, 'w')
    
    for usr in home.iterkeys():
        try:
            f.write(usr + '\t' + home[usr].popitem(last=False)[0] + '\n')
            home_simple[usr] = home[usr].popitem(last=False)[0]
        except KeyError:
            print(usr)
            
    f.close()
         
    subpref_home = defaultdict(int)    
    for usr in home_simple.iterkeys():
        try:
            subpref_home[home_simple[usr]].append(usr)
        except AttributeError:
            subpref_home[home_simple[usr]] = [usr]
    
    testi = 0
    for subpref in subpref_home.iterkeys():
        print subpref_home[subpref]
        testi += 1
        if testi > 1:
            break
    
    if total == True:    
        fileout2 = 'Subprefs_and_their_users_total.tsv'
    else:
        fileout2 = 'Subprefs_and_their_users.tsv'
    f2 = open(fileout2, 'w')
    
    count_users_check = 0
    
    for subpref in subpref_home.iterkeys():
        f2.write(subpref + ':')
        for usr in subpref_home[subpref]:
            f2.write('\t' + usr)
            count_users_check += 1
        f2.write('\n')
        
    f2.close()   
    print count_users_check
    print len(subpref_home)
    
    for i in range (256):
        if str(i) not in subpref_home.iterkeys():
            print i
            
    return