# Run with Python 3
import re
import json
import requests

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
token = json.loads(resp.text)['access_token']

# 3. Get all learning events
page = 1
events = []
while True:
	api_url = 'https://stepik.org/api/events?type=learn' + '&page=' + str(page)
	data = json.loads(requests.get(api_url, headers={'Authorization': 'Bearer '+ token}).text)
	events += data['events']
	if not data['meta']['has_next']:
		break
	page += 1

# 4. Print them all
print('\t\t\t'.join(['ID', 'Time', 'Action', 'URL']))
for event in events:
	match = re.search(r'href=[\'"]?([^\'" >]+)', event['html_text'])
	url = match.group(0) if match else 'none'
	print('\t\t'.join([str(event['id']), event['time'], event['action'], url]))
