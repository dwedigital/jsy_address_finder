import requests
import json

url = "https://www.jerseypost.com/Umbraco/Surface/Tools/AddressSearch/"

data = request.get_json()
query = data['query']
payload = {'query': query}
payload = json.dumps(payload)
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = json.loads(response.text)

return data