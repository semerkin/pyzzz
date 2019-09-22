# -*- coding: utf-8 -*-

from pyajam import Pyajam
import json

ajam = Pyajam(server='192.168.10.8', username='manager', password='pa55', autoconnect=False)

ajam.login()

event_json = ajam.sippeers()

objson = json.dumps(event_json, encoding='utf-8')
# print objson   #print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))

for i in json.loads(objson):
    try:
        print ('{0:<14} {1:<15} {2:<8} {3:<8}'.format(i['objectname'], i['ipaddress'], i['status'], i['latency']))
    except:
        print ('{0:<14} {1:<15} {2:<8} {3:<8}'.format(i['objectname'], i['ipaddress'], i['status'], '-none-'))

