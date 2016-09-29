# pip install asterisk-ami

import sys
import os
import time
import requests

from asterisk.ami import AMIClient


def event_notification(source, event):
    try:
        strevent = str(event)
        r = requests.post('http://IP/DEST', auth=('USER', 'PASS'), data=strevent)
        print r.status_code # это потом закоментить
    except:
        print '\nConnection problem !'
        sys.exit(13)
    print event.name + ' ---> ' + strevent + '\n' # это потом закоментить



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
        time.sleep(10)
except (KeyboardInterrupt, SystemExit):
client.logoff()
