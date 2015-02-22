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
# free and total memory
# free and total diskspace
#hostname
# all of the above
#os.popend("_____".read() :(string)

def get_mem_free():
	text = os.popen('free -m').read().strip().split("\n")[1].split(" ")
	text = filter(lambda x : len(x) > 0, text)[1:]
	return text[1]
#	m = re.search('AAA(.+?)ZZZ', text)
#	if m:
#		found = m.group(1)
#	 try:
#        	return int(s)
#    	except ValueError:
#		return None
#
#	return found
#	number = int(filter(str.isdigit, text))
#	return number

