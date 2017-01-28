import json
import requests

def token(os_username, os_password, os_tenant_id, os_auth_url):
	"ok"
	data = {
		"auth": {
			"tenantId": os_tenant_id,
			"passwordCredentials": {
				"username": os_username,
				"password": os_password
			}
		}
	}
	
	payload=json.dumps(data)
	
	headers = { 'content-type': "application/json" }
	
	response = requests.request("POST", os_auth_url + '/tokens', data=payload, headers=headers)
		
	data = json.loads(response.text)
	
	token=data['access']['token']['id']
	
	return token;

def backup( os_compute_endpoint, token, instance_id, backup_name, backup_type, rotation ):
	"This prints a passed string into this function"
	
	url = os_compute_endpoint + "/servers/" + instance_id + "/action"
	
	data = {
		"createBackup" : {
			"name" : backup_name,
			"backup_type" : backup_type,
			"rotation" : str(rotation)
		}
	}	
	
	payload=json.dumps(data)
	
	headers = { 'x-auth-token': token, 'content-type': "application/json" }
	
	response = requests.request("POST", url, data=payload, headers=headers)
	
	return;
