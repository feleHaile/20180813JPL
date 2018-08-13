#!/usr/bin/env python

from six import b, u, print_

s1 = "abc\u263A"    # <1>
s2 = b("abc")
s3 = u("abc\u263A")


print_("s1:", s1, type(s1))
print_("s2:", s2, type(s2))
print_("s3:", s3, type(s3))
