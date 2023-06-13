# Run with Python 3
import requests
from random import randint
import shutil
import math

# 1. Get your keys at https://stepik.org/oauth2/applications/ (client type = confidential,
# authorization grant type = client credentials)
client_id = "n4mnzQGfDEfOhFixwBvLV2mZJJLvf86pzfMMiPF5"
client_secret = "40ON9IPJRDAngUkVbGBTEjCBAwc2wB7lV8e71jJUPKabdKq6KBTUBKb1xGkh82KtAI1AqISrL3Zi4sTfhCBVh27YvlV6Y5klpXXV5loUWvuhMSRiN3HRZzVDO0fLBibv"

# 2. Get a token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
resp = requests.post('https://stepik.org/oauth2/token/',
                     data={'grant_type': 'client_credentials'},
                     auth=auth
                     )
token = resp.json()['access_token']

# 3. Call API (https://stepik.org/api/docs/) using this token.


# Get leaders by count
def get_leaders(count):
    pages = math.ceil(count / 20)
    leaders = []
    for page in range(1, pages + 1):
        api_url = 'https://stepik.org/api/leaders/?page={}'.format(page)
        response = json.loads(requests.get(api_url, headers={'Authorization': 'Bearer '+ token}).text)
        leaders += response['leaders']
        if not response['meta']['has_next']:
            break

    return leaders

# Get user by id
def get_user(id):
    api_url = 'https://stepik.org/api/users/{}/'.format(id)
    return requests.get(api_url, headers={'Authorization': 'Bearer '+ token}).json()['users'][0]


# Download avatar by user id
def download_avatar(id, filename):
    avatar_url = get_user(id)['avatar']
    response = requests.get(avatar_url, stream=True)
    with open('{}.png'.format(filename), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

# Get leader user randomly from 100 leaders and download his avatar
rand_leader_id = get_leaders(100)[randint(0, 99)]['user']
download_avatar(rand_leader_id, 'leader')
