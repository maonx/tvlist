#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def download_url_content(url):
    url_content = False
    response = requests.get(url)
    if response.status_code == 200:
        url_content = response.text
    return url_content
