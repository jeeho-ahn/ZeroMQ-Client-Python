"""
An example package for ZeroMQ client

Written: Ahn, Jeeho
Apr 30th, 2023
"""

import zmq_tools as zt

client = zt.zmqClient(7878)
if(client):
    print("Connected")

res = client.request_msg("Test client here")
print(res)
