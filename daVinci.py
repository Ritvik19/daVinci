import sys, os
sys.path.append(os.path.join(sys.path[0], 'modules'))

import webscraping

def make_reply(msg):
    print(msg)
    reply = None
    mode = None
    if msg is not None:
        msg = msg.split()
        if msg[0] == '/woof':
            reply = webscraping.woof()
            mode = 1
        elif msg[0] == '/wiki':
            reply = webscraping.wiki(' '.join(msg[1:]))
            mode = 0
        elif msg[0] == '/dict':
            reply = webscraping.cambridge(' '.join(msg[1:]))
            mode = 0
        elif msg[0] == '/hastebin':
            reply = webscraping.haste(' '.join(msg[1:]))
            mode = 0
        else:
            reply = webscraping.search(' '.join(msg))
            mode = 0
    return reply, mode
