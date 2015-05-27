# openstack-prospero
A lightweight tool for testing multi-site OpenStack deployments.

Usage:
Edit data/sites.yaml to enter your site information, eg controllers, computes, authurl, etc.

Run from the command-line:
./runner.py SITENAME # SITENAME is what you called your site when adding it to sites.yaml

eg Using the supplied sample data; there is a site named 'site1'
./runner.py site1
