import requests
import json
import sys

try:
    r = requests.get('http://192.168.10.25:8088/ari/endpoints', auth=('hey', 'user'))
except requests.exceptions.ConnectionError as e:
    print '\nConnection error:', e
    sys.exit(13)
try:
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print '\nERROR:', e
    sys.exit(13)

# print r.status_code
# print r.text
if r.status_code != 200:
    print 'error in result code !! ->', r.status_code
    # raise Exception('warning 1')
    sys.exit(13)

event_json = json.loads(r.text)

# json.dump(r)
# json.dump(event_json, sys.stdout, indent=2, sort_keys=True, separators=(',', ': '))
# print event_json
# for peer in event_json:
#     print peer['resource'], peer['state']#['state']

print map(lambda peer: peer['resource'] + ' -> ' + peer['state'], event_json)
# peer = 0
# try:
#     while event_json[peer]:
#         print event_json[peer]['resource'] + ' -->', event_json[peer]['state']
#         peer += 1
# except IndexError:
#     pass
