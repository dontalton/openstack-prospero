from glanceclient import Client
from shared import *

site = 'site1'
sitedata = yamldata['sites'][site]
user = sitedata['user']
password = sitedata['pass']
tenant = sitedata['tenant']
authurl = sitedata['authurl']
glance_endpoint = sitedata['glanceurl']
token = get_token(site)


glance = Client('1', endpoint=glance_endpoint, token=token)
images = glance.images.list()
print images

for i in images:
  print i

#with open('images/cirros-0.3.4-x86_64-disk.img', 'wb') as f:
#        for chunk in image.data:
#            f.write(chunk)

#print image.status

#image.delete()
#image.list
