'''
Created on Jan 7, 2013

@author: sscepano
'''

from collections import defaultdict, OrderedDict

def data_to_files(data):

    fq = defaultdict(float)
    
    total_hours = 24 * 7 * 20

    for usr in data.iterkeys():
        fq[usr] = float(data[usr]) / float(total_hours)
    
    file_out = 'Users_and_their_total_calls_number.tsv'
    f = open(file_out, 'w')
    
    file_out2 = 'Users_and_their_calling_fq.tsv'
    f2 = open(file_out2, 'w')
    
    for usr in data.iterkeys():
        f.write(str(usr) + '\t' + str(data[usr]) + '\n')
        f2.write(str(usr) + '\t' + str(fq[usr]) + '\n')
      
    f.close()
    f2.close()