#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def download_url_content(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print('\nFailed!!', e)
        return False
    return response.text
