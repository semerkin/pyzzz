# -*- coding: utf-8 -*-

import sys
from time import strftime, sleep
import requests

from asterisk.ami import AMIClient


def event_notification(source, event):
    try:
        strevent = str(event)
        r = requests.post('http://IP/DEST', auth=('USER', 'PASS'),
                          headers={'content-type': 'application/json'},
                          data={'evtime': strftime("%Y-%m-%d %H:%M:%S"),
                                'event': strevent})
        print r.status_code     # это in production закоментить
    except Exception:
        print '\n problem !!!!'
        sys.exit(13)
    print event.name + ' -------> ' + strevent + '\n'    # это in production закоментить

host = '127.0.0.1'
user = 'hey'
password = 'user'

client = AMIClient(host)
future = client.login(user, password)
if future.response.is_error():
    raise Exception(str(future.response))

client.add_event_listener(event_notification)

try:
    while True:
        sleep(10)
except (KeyboardInterrupt, SystemExit):
    client.logoff()


