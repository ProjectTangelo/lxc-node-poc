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

# Import salt libs
import salt.utils
from salt.utils import which as _which
from salt.exceptions import SaltInvocationError


__outputter__ = {
    'tree': 'txt',
}

__ALIAS_RE = re.compile(r'([^:#]*)\s*:?\s*([^#]*?)(\s+#.*|$)')

script, UID, N, CID  = argv


def printMasterTable():
    with open('/opt/usernodes.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
    

def addToMasterTable():
    with open('/opt/master.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([UID]+[N]+[CID])

