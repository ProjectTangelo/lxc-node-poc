# -*- coding: utf-8 -*-
'''
Manage the information in the aliases file
'''


from __future__ import absolute_import

# Import python libs
import os
import re
import stat
import random
import tempfile
import csv

# Import salt libs
import salt.utils
from salt.utils import which as _which
from salt.exceptions import SaltInvocationError


__outputter__ = {
    'tree': 'txt',
}

__ALIAS_RE = re.compile(r'([^:#]*)\s*:?\s*([^#]*?)(\s+#.*|$)')
# free and total memory
# free and total diskspace
#hostname
# all of the above
#os.popend("_____".read() :(string)
        
def master_read():
    with open('/opt/master.csv', 'r+') as csvfile:
        buffy = csvfile.read()
        return buffy
        #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #for row in spamreader:
        #    stuff=', '.join(row)
        #return stuff
def master_write(node_id, uid, lxc_id):
    with open('/opt/master.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([node_id,uid,lxc_id])
        return 1
def master_delete(node_id, uid, lxc_id):
    rows = master_read().strip()
    rows = map( lambda x : x.split(' '),rows.strip().split('\n'))
    out = []
    k=0
    for row in rows:
        row = map(lambda x : x.strip(), row)
    	is_match = str(row[0]) == str(node_id) and str(row[1]) == str(uid) and str(row[2]) == str(lxc_id) 
        if is_match:
        	do_write = True
    		del rows[k]
        else:
            k +=1
    
    if do_write:
    	with open('/opt/master.csv', 'wr+') as f:
    		f.write( "\n".join(map(lambda x : ' '.join(x), rows)) )
    		
    return rows
