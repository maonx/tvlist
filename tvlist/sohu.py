#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import json

def get_id(page):
    pattern = re.compile('playlist.*Id *= *"([0-9]*)"', re.I)
    playlist_id = pattern.search(page)
    if playlist_id is not None:
        return playlist_id.group(1)
    else :
        print("Can not find playlist ID !!")
        return 0

def get_json(page):
    playlist_id = get_id(page)
    if playlist_id:
        url = 'http://pl.hd.sohu.com/videolist?playlistid=' + playlist_id
        page = requests.get(url)
        if page.status_code == 200:
            json_str = page.json()
            return json_str
        else: 
            print("Can not open TV url !!")
            return 0

def playlist_url(page):
    json_list = get_json(page)
    if json_list:
        if 'showAlbumName' in json_list.keys():
            name = json_list['showAlbumName']
        else:
            name = json_list['albumName']
        update_info = json_list['updateNotification']
        videos = json_list['videos']
        free_videos = [ x for x in videos if not x['tvIsFee'] ]
        download_info = '可免费下载 %d 集' % len(free_videos)
        info = '\n'.join([name, update_info, download_info])
        playlist_urls = [ x['pageUrl'] for x in free_videos ] 
        playlist_urls.insert(0, info)
        return playlist_urls

        


    
