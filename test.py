import json
import keystoneclient.v2_0
import sys

### pretty colors
green = '\033[92m'
red   = '\033[91m'
clear = '\033[0m'

tenant='admin'
openstack_user='admin'
openstack_pass='clean'
keystone_auth_url='http://10.0.2.15:5000/v2.0'


### KEYSTONE
# Connect to Keystone. Create a test tenant, then delete it.
###

try:
    keystone_client  = keystoneclient.v2_0.client.Client(username=openstack_user, \
                           password=openstack_pass, tenant_name=tenant, \
                           auth_url=keystone_auth_url)
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

    print "Keystone check: " + green + "[pass]" + clear

except Exception,e:
    print "Keystone check: " + red + "[fail]" + clear
