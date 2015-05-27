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
    writelog('API: Nova check passed', 'info')

  except Exception,e:
    writelog('API: Nova check failed', 'error')

def nova_test_guest(id):
  # ping shit
  # check log
  print 'placeholder'

def nova_migrate_guest(id):
  # this tests all compute nodes
  # for i in nova.get.available.computes:
  #   nova migrate blah
  #   nova_test_guest(blah)
  print 'placeholder'

def nova_create_guest():
  # glance_create -> returns image id
  # while not up active, sleep
  # if not active after 60 seconds, delete, exit
  # once active:
  #  nova_test_guest(id)
  #  nova_migrate_guest(id)
  print 'placeholder'
