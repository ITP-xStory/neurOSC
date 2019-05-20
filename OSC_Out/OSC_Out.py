from oscpy.client import OSCClient

osc = OSCClient("127.0.0.1", 5005)
for i in range(10):
    osc.send_message(b'/ping', [i])