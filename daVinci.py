import sys, os
sys.path.append(os.path.join(sys.path[0], 'modules'))

import woof, webscraping

def make_reply(msg):
    print(msg)
    reply = None
    msg = msg.split()
    if msg[0] == '/woof':
        reply = woof.get_image_url()
        mode = 1
    elif msg[0] == '/wiki':
        reply = webscraping.wiki(' '.join(msg[1:]))
        mode = 0
    elif msg[0] is not None:
        reply = 'Okay'
        mode = 0
    return reply, mode
