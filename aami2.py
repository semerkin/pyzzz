import socket

username = 'se'
password = '1121'
""" Initialize the dictionary in the global space """


def make_dict(lst):
    ret = {}
    for i in lst:
        i = i.strip()
        if i and i[0] is not "#" and i[-1] is not "=":
            var, val = i.rsplit(":", 1)
            ret[var.strip()] = val.strip()
    return ret


class acli:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverip = '192.168.10.9'
        self.serverport = 5038
        self.username = ''
        self.password = ''

    def sendCmd(self, action, **args):
        self.sock.send("Action: %s\r\n" % action)
        for key, value in args.items():
            self.sock.send("%s: %s\r\n" % (key, value))
        self.sock.send("\r\n")
        data = []
        while '\r\n\r\n' not in ''.join(data)[-4:]:
            buf = self.sock.recv(1)
            data.append(buf)
        l = ''.join(data).split('\r\n')
        return l

    def conn(self):
        self.sock.connect((self.serverip, self.serverport))
        # need Events OFF with the login else event text pollutes our command response
        ret = self.sendCmd("login", Username=self.username, Secret=self.password, Events="OFF")
        # print "Connect response: ", ret
        if 'Response: Success' in ret:
            print 'Connected.'
            return True
        else:
            # print "Connect failed!"
            callCavalry(value['Message'], 'api call')
            return False


def callCavalry(mesg, doing):
    # put your action here
    print 'Ouch!', mesg, doing
    return True


def main():
    ast = acli()
    ast.username = username
    ast.password = password
    if ast.conn():
        dev = ast.sendCmd('SIPShowPeer', Peer='157')
        # print "Command response: ", dev
        value = make_dict(dev)
        if value['Response'] == 'Success':
            # print value
            print "Address-IP", value['Address-IP']
            print "Status    ", value['Status']
            # don't test only for "OK" here, some return longer strings with ping time etc
            if 'OK' in value['Status']:
                print 'OK:        trunk is up.'
                # pass
            else:
                callCavalry(value['Status'], 'peer myvoiptrunkname')
        else:
            callCavalry(value['Message'], 'api call')

        dev = ast.sendCmd('SIPShowPeer', Peer='177')
        # print "Command response: ", dev
        value = make_dict(dev)
        if value['Response'] == 'Success':
            # print value
            print "Address-IP", value['Address-IP']
            print "Status    ", value['Status']
            # don't test only for "OK" here, some return longer strings with ping time etc
            if 'OK' in value['Status']:
                print 'OK:        trunk is up.'
                # pass
            else:
                callCavalry(value['Status'], 'peer myvoiptrunkname')
        else:
            callCavalry(value['Message'], 'api call')

    return 0


def main2():
    ast = acli()
    ast.username = username
    ast.password = password
    if ast.conn():
        dev = ast.sendCmd('SIPpeers')
        print "Command response: ", dev
        value = make_dict(dev)
        if value['Response'] == 'Success':
            print value

    return 0


if __name__ == '__main__':
    main()
