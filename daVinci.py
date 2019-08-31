import sys, os
sys.path.append(os.path.join(sys.path[0], 'modules'))

import woof

def make_reply(msg):
    print(msg)
    reply = None
    if msg == '/woof':
        reply = woof.get_image_url()
        mode = 1
    elif msg is not None:
        reply = 'Okay'
        mode = 0
    return reply, mode
