# Starting client where things happen
from oscpy.client import OSCClient

address = "127.0.0.1"
port = 1221

### Initialize OSC Client
osc = OSCClient(address, port)

osc.send_message(u'/data', [u'helllooooo'])

