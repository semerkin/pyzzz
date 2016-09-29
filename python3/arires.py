import json
import sys
import requests

try:
    r = requests.get('http://192.168.10.25:8088/ari/endpoints', auth=('hey', 'user'))
except requests.exceptions.ConnectionError as conerr:
    print('\nConnection error ! ', conerr)
    sys.exit(13)
try:
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print('ERROR: %s' % e)
    sys.exit(13)

# print(dir(r))
# print(r.json()[0])
# print r.status_code
# print r.text
if r.status_code != 200:
    print('\nerror in result code !!')
    sys.exit(13)

event_json = json.loads(r.text)

# json.dump(r)
# json.dump(event_json, sys.stdout, indent=2, sort_keys=True, separators=(',', ': '))
# print event_json
# for peer in 0, 1, 2:
#    print event_json[peer]['resource'], event_json[peer]['state']#['state']
#
# print(type(event_json))
# print(map(lambda x: x['state'], event_json))
for peer in event_json:
    print(peer['resource'] + ' -> ' + peer['state'])

print('===')

print('\n'.join(list(map(lambda peer: peer['resource'] + ' -> ' + peer['state'], event_json))))

print('===')

print('\n'.join([peer['resource'] + ' -> ' + peer['state'] for peer in event_json]))

