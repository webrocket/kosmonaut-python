import socket
import uuid
import json
from urlparse import urlparse

debug = False

def log(msg):
    if debug:
        print("DEBUG: %s" % msg)


class Client(object):

    def __init__(self, url):
        self.__uri = urlparse(url)
        self.__generate_identity()

    def socket_type(self):
        return "req"

    def broadcast(self, channel, event, data):
        payload = ["BC", channel, event, json.dumps(data)]
        return self.__perform_request(payload)

    def open_channel(self, name):
        payload = ["OC", name]
        return self.__perform_request(payload)

    def close_channel(self, name):
        payload = ["CC", name]
        return self.__perform_request(payload)

    def request_single_access_token(self, uid, permission):
        payload = ["AT", uid, permission]
        return self.__perform_request(payload)

    def __connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.__uri.hostname, self.__uri.port))
        return sock

    def __generate_identity(self):
        parts = []
        parts.append(self.socket_type())
        parts.append(self.__uri.path)
        parts.append(self.__uri.username)
        parts.append(str(uuid.uuid4()))
        self.__identity = ":".join(parts)

    def __pack(self, payload, with_identity = True):
        if with_identity:
            payload.insert(0, "")
            payload.insert(0, self.__identity)
        return "\n".join(payload) + "\n\r\n\r\n"

    def __recv(self, sock):
        pass


    def __perform_request(self, payload):
        response = []
        sock = self.__connect()
        packet = self.__pack(payload)
        log("Client/REQ : %s" % packet)
        sock.send(packet)
        response = self.__recv(sock)
        sock.close()
        print(response)

