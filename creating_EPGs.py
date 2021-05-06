from acitoolkit import*
import json

url="https://apic1.dcloud.cisco.com"
usr="admin"
passw="C1sco12345"

session = Session(url,usr,passw)
session.login()

tenants = Tenant.get(session)
print('List of all Tenents:')
for x in tenants:
    print (x.name)
    if x.name=='mgmt':
        tenant=x
#print(type(tenant))

print('\nList of all Appication profiles:')
aps = AppProfile.get(session,tenant)
for x in aps:
    print(x.name)
    if x.name=='Profile':
        ap=x
#print(type(ap))

print('\nList of all ABridge Domains:')
bds = BridgeDomain.get(session,tenant)
for x in bds:
    print(x.name)
    if x.name=='BD1':
        bd=x
#print(type(bd))

with open ('epgs.json','r') as file:
    data = json.loads(file.read())
	
for x in data:
    epg = EPG(x['name'], ap)
    epg.descr='created_by_acitoolkit'
    epg.attach(bd)
    resp = tenant.push_to_apic(session)
	