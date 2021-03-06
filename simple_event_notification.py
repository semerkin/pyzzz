# pip install asterisk-ami


import os
import time

from asterisk.ami import AMIClient


def event_notification(source, event):
    print event.name + ' ---> ' + str(event) + '\n'



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
