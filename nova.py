import json
from novaclient.v2 import client
import sys
from shared import *

###
# Connect to Nova. Create a VM. Check that it's UP/ACTIVE/pingable?.
###

def nova_check(site):

  sitedata = yamldata['sites'][site]
  user = sitedata['user']
  password = sitedata['pass']
  tenant = sitedata['tenant']
  authurl = sitedata['authurl']

  try:
    nc = client.Client(username=user, auth_url='http://10.0.2.15:5000/v2.0/', auth_token=token, tenant_id='', service='compute')
    nova.flavors.list()
    writelog('Nova check passed', 'error')

  except Exception,e:
    writelog('Nova check failed', 'error')


nova_check('site1')
