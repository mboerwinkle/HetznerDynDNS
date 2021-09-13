import requests
import json
import getpass
AuthAPIToken = getpass.getpass(prompt="API-Token: ")
zone = input("Zone Name: ")
url="https://dns.hetzner.com/api/v1/zones"
data = json.dumps({
 "name":zone,
 "ttl":86400
})
response = requests.post(url=url, headers={"Auth-API-Token": AuthAPIToken, "Content-Type": "application/json"}, data = data)
print("Status:",response.status_code)
print("Content:",response.content)
