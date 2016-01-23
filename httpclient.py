#!/usr/bin/env python
# coding: utf-8
# Copyright 2013 Abram Hindle
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it

# using for testing and debugging:
# python httpclient.py GET "https://www.google.ca/"

import sys
import socket
import re
# you may use urllib to encode data appropriately
import urllib

# get help from https://docs.python.org/2/library/urlparse.html
from urlparse import urlparse

def help():
    print "httpclient.py [GET/POST] [URL]\n"

class HTTPRequest(object):
    print("in HTTPRequest but this class we do not need to change.")
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    #def get_host_port(self,url):
	
    def connect(self, host, port):
        print("in def 1")
        # use sockets!
        if not port:
            print("port == None")
            port = 80

        outgoingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        outgoingSocket.connect((host, port))

        return outgoingSocket

    def get_code(self, data):
        print("in def 2")
        print"data is ------------> ", data

        return None

    def get_headers(self,data):
        print("in def 3")
        print("The data is printed like this2:")
        #print(data.split('\r\n\r\n'))
        return None

    def get_body(self, data):
        print("in def 4")
        print("The data is printed like this3:")
        return None

    # read everything from the socket
    def recvall(self, sock):
        print("in def 5")
        buffer = bytearray()
        done = False
        while not done:
            part = sock.recv(1024)
            if (part):
                buffer.extend(part)
            else:
                done = not part
        return str(buffer)

    def GET(self, url, args=None):
        print("in def 6")
        print("URL ->", url)

        parseResult = urlparse(url)
        print(parseResult)
        print

        incomingSocket = self.connect(parseResult.hostname, parseResult.port)

        print("\nBack to def 6")
        request = "GET %s HTTP/1.1\r\n\
                   Host: %s\r\n\
                   Accept: */*\r\n\
                   Connection: close\r\n\r\n"\
                   % (parseResult.path, parseResult.hostname)
        print(request)
        incomingSocket.send(request)

        response = self.recvall(incomingSocket)
        code = self.get_code(response)
        body = self.get_body(response)

        print(code, body)
        print("------------------------------")

        return HTTPRequest(code, body)

    def POST(self, url, args=None):
        print("in def 7")
        code = 500
        body = ""
        return HTTPRequest(code, body)

    def command(self, command, url, args=None):
        print "\nCommand in client.command is:", command, '\n'
        if (command == "POST"):
            return self.POST( url, args )
        else:
            return self.GET( url, args )
    
if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        print client.command( sys.argv[1], sys.argv[2] )
    else:
        print client.command( command, sys.argv[1] )    
