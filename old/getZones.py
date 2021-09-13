import requests
import getpass
import json
AuthAPIToken = getpass.getpass(prompt="API-Token: ")
headers = {
 "Auth-API-Token":AuthAPIToken,
 "Content-Type": "application/json; charset=utf-8"
}
url="https://dns.hetzner.com/api/v1/zones"

response = requests.get(url=url, headers={"Auth-API-Token": AuthAPIToken})

print("Status:",response.status_code)
print("Content:",response.content)
