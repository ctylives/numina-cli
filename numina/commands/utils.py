from json import loads

def check_if_expired(response):
    j_res = loads(response.text)
    if "status" in j_res and j_res["status"] == 'Token is expired':
        print('Your authentication token is expired request a new one at https://dashboard.numina.co/authenticate and update the cli via numina authenticate <your token>')
        return True
    return False

def get_saved_token():
    try:
        authfile = open('token.txt', 'r')
    except IOError:
        print("Please enter an authentication token before using other api features. (numina authenticate <token>)")
        return False
    token = authfile.read()
    token = token.replace('"', '')
    authfile.close()
    return token
