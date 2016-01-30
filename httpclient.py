#!/usr/bin/env python
# coding: utf-8
# Copyright 2016 Abram Hindle, https://github.com/tywtyw2002, and https://github.com/treedust
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

class HTTPResponse(object):
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    def connect(self, host, port):
        # use sockets! If port is None, set port as 80
        if not port:
            port = 80
        # connect it as what was shown in lab      
        outgoingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        outgoingSocket.connect((host, port))
        return outgoingSocket

    def get_code(self, data):
        # return the code
        return int(data.split()[1])

    def get_body(self, data):
        # return the whole html from "<!DOCTYPE html..." to "...</body>" 
        return data.split('\r\n\r\n')[1]

    # read everything from the socket
    def recvall(self, sock):
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
<<<<<<< HEAD
        # use urlparse to get ParseRequest
        parseResult    = urlparse(url)
        incomingSocket = self.connect(parseResult.hostname, parseResult.port)
        
        # made request and send it
        request = "GET   " + parseResult.path     + " HTTP/1.1\r\n" \
                + "Host: " + parseResult.hostname + "\r\n"          \
                + "Accept: */*\r\n"                                 \
                + "Connection: close\r\n\r\n"
        incomingSocket.send(request)
=======
        code = 500
        body = ""
        return HTTPResponse(code, body)
>>>>>>> abramhindle/master

        # get response of the sent request 
        response = self.recvall(incomingSocket)
        code     = self.get_code(response)
        body     = self.get_body(response)
        return HTTPRequest(code, body)
    
    def POST(self, url, args=None):
<<<<<<< HEAD
        # get or make a content for POST
        if (args != None):
            postContent = urllib.urlencode(args)
        else:
            postContent = ""

        # get parseRequest and Content-Length
        parseResult       = urlparse(url)
        postContentLength = len(postContent)
        incomingSocket    = self.connect(parseResult.hostname,parseResult.port)
        
        # made request and send it
        request = "POST  " + parseResult.path     + " HTTP/1.1\r\n"        \
                + "Host: " + parseResult.hostname + "\r\n"                 \
                + "Accept: */*\r\n"                                        \
                + "Content-Type: application/x-www-form-urlencoded\r\n"    \
                + "Content-Length: " + str(postContentLength) + "\r\n\r\n" \
                + postContent + "\r\n"
        incomingSocket.send(request)

        # get response of the sent request 
        response = self.recvall(incomingSocket)
        code     = self.get_code(response)
        body     = self.get_body(response)
        return HTTPRequest(code, body)
=======
        code = 500
        body = ""
        return HTTPResponse(code, body)
>>>>>>> abramhindle/master

    # I changed the initial order of input argv because GET is before URL
    def command(self, command, url, args=None):
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
        print client.command( sys.argv[2], sys.argv[1] )
    else:
<<<<<<< HEAD
        print ( command, sys.argv[1] )   
=======
        print client.command( sys.argv[1] )   
>>>>>>> abramhindle/master
