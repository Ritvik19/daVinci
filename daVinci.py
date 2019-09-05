import sys, os
sys.path.append(os.path.join(sys.path[0], 'modules'))

import webscraping, help, chat

def make_reply(msg):
    reply = None
    mode = None
    if msg is not None:
        msg = msg.split()
        print(msg)
        if msg[0] == '/help':
            reply = help.help()
            mode = 0
        elif msg[0] == '/woof':
            reply = webscraping.woof()
            mode = 2
        elif msg[0] == '/cric':
            reply = webscraping.cricbuzz()
            mode = 0
        elif msg[0] == '/wiki':
            reply = webscraping.wiki(' '.join(msg[1:]))
            mode = 0
        elif msg[0] == '/dict':
            reply = webscraping.cambridge(' '.join(msg[1:]))
            mode = 0
        elif msg[0] == '/hastebin':
            reply = webscraping.haste(' '.join(msg[1:]))
            mode = 0
        elif msg[0] == '/code':
            reply = webscraping.stackoverflow(' '.join(msg[1:]))
            mode = 0
        elif msg[0] == '/apod':
            reply = webscraping.apod()
            mode = 3 if len(reply) == 2 else 0
        elif msg[0] == '/pic':
            reply = webscraping.upsplash(' '.join(msg[1:]))
            mode = 2
        else:
            reply = chat.reply(' '.join(msg))
            mode = 0
    return reply, mode
