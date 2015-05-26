#!/usr/bin/env python
import sys
from keystone import *
from nova import *

site = sys.argv[1]
keystone_check(site)
nova_check(site)
