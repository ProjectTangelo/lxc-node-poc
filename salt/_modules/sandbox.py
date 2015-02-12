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
    'echo': 'txt',
}

__ALIAS_RE = re.compile(r'([^:#]*)\s*:?\s*([^#]*?)(\s+#.*|$)')


def echo(alias):
    '''
    Remove an entry from the aliases file

    CLI Example:

    .. code-block:: bash

        salt '*' sandbox.echo alias
    '''

    return {'a' : 3, 'b' : 'a', 'k':{'a' : 3, 'b' : 'a'}}