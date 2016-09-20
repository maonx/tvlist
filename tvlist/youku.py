#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

def get_url(page):
    url = None
    if 'showid_en:' in page:
        pattern = re.search('showid_en:"(.*?)"', page)
    elif 'showid_z' in page:
        pattern = re.search('showid_z(.*?).html', page)
    else:
        pattern = None

    if  pattern is not None:
        id = pattern.group(1)
        url = 'http://www.youku.com/show_episode/id_z%s.html?dt=json' % id
    else:
        print("Error! can not find playlist ID !!!")
    return url

    
        
