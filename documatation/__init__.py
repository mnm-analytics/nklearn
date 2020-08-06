import json
import requests

def upload2imgur(client_id, p):
    '''check client_id in "https://imgur.com/account/settings/apps"
    '''
    url = 'https://api.imgur.com/3/upload'
    headers = {'authorization': f'Client-ID {client_id}'}
    files = {'image': (open(p, 'rb'))}
    return json.loads(r.text)['data']['link']

def get_tag(client_id, p):
    url = upload2imgur(client_id, p)
    return "![](%s)" % url

if __name__ == "__main__":
    pass