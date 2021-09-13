import requests
import getpass
import json
import time

AuthAPIToken = getpass.getpass(prompt="API-Token: ")
ZoneName = input("Zone Name: ")
headers = {
 "Auth-API-Token":AuthAPIToken,
 "Content-Type": "application/json; charset=utf-8"
}
zonesurl = "https://dns.hetzner.com/api/v1/zones"

time.sleep(1)
zonesresponse = requests.get(url=zonesurl, headers=headers)
assert zonesresponse.status_code == 200
zonesjson = json.loads(zonesresponse.text)
ZoneID=""
for zone in zonesjson["zones"]:
	if zone["name"] == ZoneName:
		ZoneID = zone["id"]
		break
assert ZoneID != ""

recordsurl="https://dns.hetzner.com/api/v1/records"
print("Records URL:",recordsurl)
time.sleep(1)
recordsresponse = requests.get(url=recordsurl, headers=headers, params={"zone_id": ZoneID})
assert recordsresponse.status_code == 200
print(recordsresponse.text)

