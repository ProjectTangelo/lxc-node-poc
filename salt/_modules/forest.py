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

def smokey(name):
    '''
    Remove an entry from the aliases file

    CLI Example:

    .. code-block:: bash

        salt '*' sandbox.echo alias
    '''

    return 'Only %s can prevent forest fires' % name


def read():
	me = os.popen('hostname').read().strip()
        if me == 'master':
             with open ('/opt/save.txt','r') as f:
		f.read() 
        else:
	with open('/opt/save.txt', 'r') as f:
		f.read("This is what I'm doing, my name is %s \n" % os.popen('hostname').read())
def write():
	with open('/opt/save.txt', 'a') as f:
                f.write("This is what I'm doing, my name is %s \n" % os.popen('hostname').read())



def berry():
	me = os.popen('hostname').read().strip()
	if me == 'master':
		return 'I run things, bitch'
	else:
		return 'Fuck, dude D:<'

def free():
    return os.popen('free -m').read()

def tree():
	    '''
    Remove an entry from the aliases file

    CLI Example:

    .. code-block:: bash

        salt '*' sandbox.echo alias
    '''

    return 'I am the walrus'

def master_read():

target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()
return
def master_write():
return
def minion_write():
return
def minion_read():
return

