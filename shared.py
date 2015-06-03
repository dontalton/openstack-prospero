import yaml
import keystoneclient.v2_0
import coloredlogs, logging
from urllib2 import urlopen


f = open('data/sites.yaml')
yamldata = yaml.load(f)

def writelog(msg, level='info'):
    coloredlogs.install(level=logging.ERROR)
    if level == 'error':
        logging.error(msg)
    else:
       print(msg)

def get_token(site):
  sitedata = yamldata['sites'][site]
  user = sitedata['user']
  password = sitedata['pass']
  tenant = sitedata['tenant']
  authurl = sitedata['authurl']

  keystone_client  = keystoneclient.v2_0.client.Client(username=user, \
                         password=password, tenant_name=tenant, \
                         auth_url=authurl)

  token = keystone_client.get_raw_token_from_identity_service(auth_url=authurl, \
                           username=user, password=password, tenant_name='admin')

  return token['token']['id']

def check_services(site):
    sitedata = yamldata['sites'][site]
    auth_url = sitedata['authurl']
    glance_url = sitedata['glanceurl']
    try:
        data = urlopen(auth_url, timeout=2).read()
        glance_check = urlopen(glance_url, timeout=2).read()
        print 'Services are responding, commencing with tests' + '\n'
        return True
    except:
        return False
