#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import argparse
from common import *
from sohu import *

def get_args():
    parser = argparse.ArgumentParser(description='Get video urls in a TV playlist url')
    parser.add_argument('url', help='TV list url')
    parser.add_argument('-s', '--start', type=int, help='Input a number "N" to start', metavar='N', default=1)
    parser.add_argument('-e', '--end', type=int, help='Input a number "N" to end', metavar='N', default=-1)
    parser.add_argument('-i', '--info', action='store_true', help='Display TV playlist infomation')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    url = args.url
    playlist_id = get_playlist_id(url) 
    playlist_json = get_playlist_json(playlist_id)
    playlist_urls = get_playlist_url(playlist_json)
    start = args.start
    end = args.end + 1
    if not end: end = None 
    if args.info:
        playlist_info(playlist_json)
    else :
        print(' '.join(playlist_urls[start:end]))

