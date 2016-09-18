#!/usr/bin/env python

import requests
import re

def get_id(page):
    rr = re.compile('playlistId')
    r = rr.search(rr)
    return r.group(1)


