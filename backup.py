import os
import sys
import common
from datetime import datetime

variables=['OS_USERNAME', 'OS_PASSWORD', 'OS_TENANT_ID', 'OS_AUTH_URL', 'OS_COMPUTE_URL']
err=0
for variable in variables:
	if( os.environ.get(variable) is None ):
		print "La variable d'environnement \"%s\" n'existe pas !" % (variable)
		err=err+1

if (len(sys.argv) != 5):
	print "La commande est incorrecte !"
	print "usage: %s <instance_id> <instance_name> <weekly|daily> <rotation>" % (sys.argv[0]) 
	err=err+1

if (err > 0):
	quit()

#########################################################
os_username=os.environ.get('OS_USERNAME')
os_password=os.environ.get('OS_PASSWORD')
os_tenant_id=os.environ.get('OS_TENANT_ID')
os_auth_url=os.environ.get('OS_AUTH_URL')
os_compute_url=os.environ.get('OS_COMPUTE_URL') 

instance_id=sys.argv[1]
instance_name=sys.argv[2]
backup_type=sys.argv[3]
rotation=sys.argv[4]
#########################################################

token=authenticate(os_username, os_password, os_tenant_id, os_auth_url)

date=datetime.now()
pattern=str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute)
backup_name=instance_name + "-"  + pattern + "-" + backup_type

backup(os_auth_url, token, instance_id, backup_name, backup_type, rotation)
