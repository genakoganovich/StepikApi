# Run with Python 3
import requests

# 1. Get your keys at https://stepik.org/oauth2/applications/
# (client type = confidential, authorization grant type = client credentials)
client_id = "n4mnzQGfDEfOhFixwBvLV2mZJJLvf86pzfMMiPF5"
client_secret = "40ON9IPJRDAngUkVbGBTEjCBAwc2wB7lV8e71jJUPKabdKq6KBTUBKb1xGkh82KtAI1AqISrL3Zi4sTfhCBVh27YvlV6Y5klpXXV5loUWvuhMSRiN3HRZzVDO0fLBibv"

# 2. Get a token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
response = requests.post('https://stepik.org/oauth2/token/',
                         data={'grant_type': 'client_credentials'},
                         auth=auth)
token = response.json().get('access_token', None)
if not token:
    print('Unable to authorize with provided credentials')
    exit(1)

# 3. Call API (https://stepik.org/api/docs/) using this token.
api_url = 'https://stepik.org/api/courses/67'
course = requests.get(api_url,
                      headers={'Authorization': 'Bearer ' + token}).json()

print(course)
