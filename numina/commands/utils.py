from json import loads

def check_if_expired(response):
	j_res = loads(response.text)
	if "status" in j_res and j_res["status"] == 'Token is expired':
		print('Your authentication token is expired request a new one at https://dashboard.numina.co/authenticate and update the cli via numina authenticate <your token>')
		return True
	return False
