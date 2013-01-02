'''
Created on Jan 2, 2013

@author: sscepano
'''
# this module divides users into 3 categories by calling fq:
# low medium and high fq callers
# hand-made rule is: low fq < 0.08; medium 0.08 <= fq <= 0.3; high fq > 0.3

file_name_in = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/Usr_call_fq python.tsv"
file_name_out = "/home/sscepano/D4D res/ORGANIZED/SET3/Distr of Num and Fq of Calls/Usr_div_by_call_fq python2.tsv"

fi = open(file_name_in, 'r')
fo = open(file_name_out, 'w')
i=0
for line in fi:
    i = i + 1
    usr, fq = line.split('\t')
    usr = int(usr)
    fq = float(fq[:-1])
    if fq < 0.08:
        fo.write(str(usr) + '\t' + 'l' + '\n')
    elif fq <= 0.3:
        fo.write(str(usr) + '\t' + 'm' + '\n')
    else:
        fo.write(str(usr) + '\t' + 'h' + '\n')

print i        
fi.close        
fo.close