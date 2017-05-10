#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from common import *
from sohu import *

class SohuExtractor(unittest.TestCase):

    """Docstring for CommonFuntions. """

    url = (('http://tv.sohu.com/20170508/n492237339.shtml', '9331535'),
           ('http://tv.sohu.com/20170509/n492390412.shtml', '9182663'),
           ('http://tv.sohu.com/20170510/n492391375.shtml', '9337016'),
           ('http://tv.sohu.com/20170509/n492346595.shtml', '8373574'),
           )

    def test_download_url_content(self):
        for url, playlist_id in self.url:
            url_content = download_url_content(url)
            self.assertTrue(url_content)

    def test_get_playlist_id(self):
        for url, playlist_id in self.url:
            self.assertEqual(get_playlist_id(url), playlist_id)

    def test_get_playlist_json(self):
        for url, playlist_id in self.url:
            self.assertTrue(get_playlist_json(playlist_id))

    def test_get_playlist_url(self):
        for url, playlist_id in self.url:
            playlist_json = get_playlist_json(playlist_id)
            self.assertTrue(get_playlist_url(playlist_json))


        



if __name__ == '__main__':
    unittest.main()

