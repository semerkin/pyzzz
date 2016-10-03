# -*- coding: utf-8 -*-

import sys
from time import strftime, sleep
import requests

from asterisk.ami import AMIClient

evlist = ['Newstate',
          'Newchannel',
          'SoftHangupRequest',
          'DeviceStateChange',
          'DialBegin',
          'DialEnd',
          'HangupRequest',
          'Hangup']


def event_notification(source, event):
    if event.name in evlist:
        try:
            r = requests.post('http://IP/DEST', auth=('USER', 'PASS'),
                              headers={'content-type': 'application/json'},
                              data={'evtime': strftime("%Y-%m-%d %H:%M:%S"),
                                    'event': str(event)})
        except requests.exceptions.ConnectionError as e:
            print '\nConnection error:', e
            sys.exit(13)
        if r.status_code != 200:
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print '\nERROR:', e
                sys.exit(13)
        # тут уже однозначно r.status_code == 200
        print r.status_code


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


