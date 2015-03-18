from __future__ import absolute_import

import os 
import re 
import stat
import random 
import tempfile

import salt.utils
from salt.utils import which as _which 
from salt.exception import SaltInvocationError

__outputter__ = {
    'tree' : 'txt',
    }
    
__ALIAS_RE = re.compile(r'([^:#]*)\s*:?\s*([^#]*?)(\s+#.*|$)')
    
def createFileMasterNodes():
f = open('opt/MasterNodesFile', 'w')

def createFileMinionNodes():
f = open('opt/MinionNodesFile', 'w')
