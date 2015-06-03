#!/usr/bin/env python
import sys
import urllib2
from keystone import *
from nova import *
from glance import *

site = sys.argv[1]

if check_services(site):
    keystone_check(site)
    nova_check(site)
    glance_check(site)
else:
    print "Unable to reach the API services"