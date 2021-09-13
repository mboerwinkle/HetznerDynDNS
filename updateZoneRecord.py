#!/bin/python3
import requests
import getpass
import json
import time
import sys
AuthAPIToken=""
ZoneName=""
RecordType=""
RecordName=""
RecordValue=""
if len(sys.argv) == 3:
	with open(sys.argv[1], "r") as tokFP:
		with json.load(tokFP) as tokDat:
			AuthAPIToken = tokDat["apitoken"]
			ZoneName = tokDat["zonename"]
			RecordType = tokDat["recordtype"]
			RecordName = tokDat["recordname"]	
	RecordValue = sys.argv[2]
elif len(sys.argv) == 1:
	AuthAPIToken = getpass.getpass(prompt="API-Token: ")
	ZoneName = input("Zone Name: ")
	RecordType = input("Record Type: ")
	RecordName = input("Record Name: ")
	RecordValue = input("Record Value: ")
else:
	print("Invalid arguments")
	sys.exit()
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
recordsjson = json.loads(recordsresponse.text)
TargetRecord = None
for record in recordsjson["records"]:
	if record["type"] == RecordType and record["name"] == RecordName:
		TargetRecord = record
		break
assert not (TargetRecord is None)
print("Target Record: ", TargetRecord)
if TargetRecord["value"] == RecordValue:
	print("Target Record value is already", TargetRecord["value"])
else:
	NewRecordData = json.dumps({
		"value":RecordValue,
		"type":TargetRecord["type"],
		"name":TargetRecord["name"],
		"zone_id":TargetRecord["zone_id"]
	})
	time.sleep(1)
	updateresponse = requests.put(url=recordsurl+"/"+TargetRecord["id"], headers=headers, data=NewRecordData)
	assert updateresponse.status_code == 200
