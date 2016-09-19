#!/usr/bin/env python

import requests
import argparse
import sohu

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
    page = requests.get(url)
    if page.status_code == 200:
        page_content = page.text
    else: 
        print("Can not open TV url !!")
    playlist_urls = sohu.playlist_url(page_content)
    start = args.start
    end = args.end + 1
    if not end: end = None 
    if args.info:
        print(playlist_urls[0])
    else :
        print(' '.join(playlist_urls[start:end]))

