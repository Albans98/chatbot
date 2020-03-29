"""# **API TEST**

[pour tester](https://gurujsonrpc.appspot.com/)

[web api](https://jooble.org/api/about)
"""

import http.client

host = 'jooble.org'
key = '824f5d8e-312e-44a9-add7-17ab2b9519c7'

connection = http.client.HTTPSConnection(host)
#request headers
headers = {"Content-type": "application/json"}
#json query
#body = '{ "keywords": "it", "location": "Bern"}'
body = '{"keywords": "manager", "location": "Paris", "radius": "50","salary": "2000" }'
connection.request('POST','/api/' + key, body, headers)
response = connection.getresponse()
#print(response.read().decode())

import json

# Decode UTF-8 bytes to Unicode, and convert single quotes 
# to double quotes to make it valid JSON
my_json = response.read().decode()
print(my_json)
print("--"*20)

data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)