#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json
from common import *

def get_playlist_id(url):
    try:
        url_content = download_url_content(url)
        pattern = re.compile('playlist.*Id *= *"([0-9]*)"', re.I)
        playlist_id = pattern.search(url_content)
    except Exception as e:
        print('\nGet playlist ID failed!!', e)
        return False
    return playlist_id.group(1)

def get_playlist_json(playlist_id):
    try:
        url = 'http://pl.hd.sohu.com/videolist?playlistid=' + playlist_id
        playlist_json = json.loads(download_url_content(url))
    except Exception as e:
        print('\nGet playlist json failed!!', e)
        return False
    return playlist_json

def playlist_info(playlist_json):
    try:
        if 'showAlbumName' in playlist_json.keys():
            playlist_name = playlist_json['showAlbumName']
        else:
            playlist_name = playlist_json['albumName']
        update_info = playlist_json['updateNotification']
        videos = playlist_json['videos']
        free_videos = [ x for x in videos if not x['tvIsFee'] ]
        download_info = '可免费下载 %d 集' % len(free_videos)
    except Exception as e:
        print('\nGet playlist infomation failed!!', e)

    print('\n\t剧集名称:\t', playlist_name)
    print('\n\t剧集更新:\t', update_info)
    print('\n\t剧集下载:\t', download_info)

def get_playlist_url(playlist_json):
    try:
        videos = playlist_json['videos']
        free_videos = [ x for x in videos if not x['tvIsFee'] ]
        playlist_urls = [ x['pageUrl'] for x in free_videos ] 
    except Exception as e:
        print('\nGet playlist url failed!!', e)
        return False
    return playlist_urls

        


    
