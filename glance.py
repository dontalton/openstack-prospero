from glanceclient import Client
from shared import *


def glance_check(site):

  # gotta wrap this up and pass it around rather than redefining it
  sitedata = yamldata['sites'][site]
  user = sitedata['user']
  password = sitedata['pass']
  tenant = sitedata['tenant']
  authurl = sitedata['authurl']
  glance_endpoint = sitedata['glanceurl']
  token = get_token(site)

  try:
    glance = Client('2', endpoint=glance_endpoint, token=token)
    image_id = glance.images.create(name='don image', container_format='bare', \
                                    disk_format='qcow2')['id']
    image = open('images/cirros-0.3.4-x86_64-disk.img', 'rb')
    glance.images.upload(image_id=image_id, image_data=image)
    glance.images.delete(image_id=image_id)
    writelog('API: Glance check passed', 'info')

  except Exception,e:
    writelog('API: Glance check failed', 'error')

def glance_create(site):
  # create an image for nova to use
  print 'placeholder'

def glance_delete(id):
  print 'placeholder'
