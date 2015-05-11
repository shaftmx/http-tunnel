#!/usr/bin/env python
import socket, time
import httplib, urllib
from uuid import uuid4
import threading
import argparse
import sys


conn_dest = { # proxy
'host': 'localhost',
'port': 3128
}

target_addr = remote_addr = {
'host': 'google.fr',
'port': 80
}

url = "http://{host}:{port}{url}".format(host=remote_addr['host'], port=remote_addr['port'], url='/')

http_conn = httplib.HTTPConnection(conn_dest['host'], conn_dest['port'])


params = urllib.urlencode({"host": target_addr['host'], "port": target_addr['port']})
headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

http_conn.request("GET", url, params, headers)
#http_conn.request("POST", self._url("/" + self.id), params, headers)

response = http_conn.getresponse()
data = response.read()

print 'STATUS : %s' % response.status
print 'DATA : %s' % data
