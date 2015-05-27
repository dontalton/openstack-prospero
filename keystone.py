import json
import keystoneclient.v2_0
import sys
from shared import *

### KEYSTONE
# Connect to Keystone. Create a test tenant, then delete it.
###

def keystone_check(site):

  sitedata = yamldata['sites'][site]
  user = sitedata['user']
  password = sitedata['pass']
  tenant = sitedata['tenant']
  authurl = sitedata['authurl']

  try:
      keystone_client  = keystoneclient.v2_0.client.Client(username=user, \
                             password=password, tenant_name=tenant, \
                             auth_url=authurl)
      keystone_roles   = keystoneclient.v2_0.roles.RoleManager(keystone_client)
      openstack_users  = keystoneclient.v2_0.users.UserManager(keystone_client, \
                             keystone_roles)
      keystone_manager = keystoneclient.v2_0.tenants.TenantManager(keystone_client, \
                             keystone_roles, openstack_users)

      tenant_list = keystone_client.tenants.list()

      for i in tenant_list:
          if i.name == 'test':
              keystone_manager.delete(i.id)

      tenant = keystone_client.tenants.create(tenant_name="rallysprint", \
                   description="rally sprint test tenant", enabled=True)
    
      tenant.delete()
      writelog('API: Keystone check passed', 'info')

  except Exception,e:
      writelog('API: Keystone check failed', 'error')
