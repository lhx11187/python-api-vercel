from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import random
import uuid
import time

""" The HTTP request handler """
class handler(BaseHTTPRequestHandler):

  def _send_cors_headers(self):
    """ Sets headers required for CORS """
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

  def send_dict_response(self, d):
    """ Sends a dictionary (JSON) back to the client """
    self.wfile.write(bytes(dumps(d), "utf8"))

  def do_OPTIONS(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()

  def do_GET(self):
    path = str(self.path)
    try:
        domain = path[path.rindex("/")+1:]
        print(domain)
        ip = socket.gethostbyname(domain)   
    except:
        text = 'path is: %s, \n Error happens\n'%(path)
    else:
        text = 'domain is: %s \n ip is: %s\n'%(domain, ip)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode())
    return
