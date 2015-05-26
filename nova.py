import json
import sys
from novaclient.v2 import client
from keystoneclient.auth.identity import v2
from keystoneclient import session
from shared import *

###
# Get a token from Keystone, then connect to Nova.
# Create a VM. Check that it's UP/ACTIVE/pingable?.
###

def nova_check(site):

  sitedata = yamldata['sites'][site]
  user = sitedata['user']
  password = sitedata['pass']
  tenant = sitedata['tenant']
  authurl = sitedata['authurl']

  try:
    # keystone auth, nova client instantiation
    auth = v2.Password(auth_url=authurl, username=user, password=password, tenant_name='admin')
    sess = session.Session(auth=auth)
    nova = client.Client('2.0', session=sess)
    writelog('Connected to Nova service', 'info')
  except Exception,e:
    writelog('Failed to connect to Nova service', 'error')
