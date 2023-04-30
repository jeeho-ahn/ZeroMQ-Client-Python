"""
An example package for ZeroMQ client

Written: Ahn, Jeeho
Apr 30th, 2023
"""

import zmq

class zmqClient:
    """
    Client object for requesting robot states
    """
    def __init__(self, port:int) -> None:
        self.socket = self.connect_to_server(port)
        self.header_delim="&"
        self.type_delim=";"
        self.elem_delim=","
        

    def connect_to_server(self,port:int):
        """
        connect to robot states server
        :returns: connected socket
        """
        context = zmq.Context()
        port_str = str(port)

        #  Socket to talk to server
        print("Connecting to hello world server…")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:"+port_str)

        return socket


    def request_msg(self,msg_out:str,decode=True)->str:
        """
        byte-wise states communication
        """
        self.socket.send(bytes(msg_out, 'utf-8'))
        message = self.socket.recv()
        #print("Received reply %s" % (message))
        #print(message.decode('utf-8'))
        if(decode):
            return message.decode('utf-8')
        else:
            return message
    