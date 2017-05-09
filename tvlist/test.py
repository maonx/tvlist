#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from common import *
from sohu import *

class SohuExtractor(unittest.TestCase):

    """Docstring for CommonFuntions. """

    url = ['http://tv.sohu.com/20170508/n492237339.shtml']

    def test_download_url_content(self):
        for i in self.url:
            url_content = download_url_content(i)
            self.assertTrue(url_content)

    def test_get_playlist_id(self):
        url = 'http://tv.sohu.com/20170508/n492237339.shtml'
        url_content = download_url_content(url)
        self.assertEqual(get_playlist_id(url_content), '9331535')



if __name__ == '__main__':
    unittest.main()

