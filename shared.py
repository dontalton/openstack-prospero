import yaml
import coloredlogs, logging

f = open('data/sites.yaml')
yamldata = yaml.load(f)

def writelog(msg, level='info'):
    coloredlogs.install()
    if level == 'error':
        logging.error(msg)
    else:
       logging.info(msg)
