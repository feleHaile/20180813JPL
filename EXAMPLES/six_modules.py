#!/usr/bin/env python
import sys
from six import print_, iteritems # <1>
from six.moves import html_parser # <2>

for module, obj in iteritems(sys.modules): # <3>
    if 'html' in module.lower(): # <4>
        print_(module) # <5>


