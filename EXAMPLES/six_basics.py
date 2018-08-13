#!/usr/bin/env python
import six

six.print_("Hello, compatible world")  # <1>

# or

from six import print_

print_("Hello, compatible world") # <2>
