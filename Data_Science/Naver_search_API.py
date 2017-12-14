import os
import sys
import urllib.request
import datetime
import time
import json
# import config

def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",app_id)
