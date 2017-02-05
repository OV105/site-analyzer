#!/usr/bin/env python3
#
####################################################################
#
# Copyright (c) Timothy H. Lee
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the Apache License 2.0 License.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED. See the Apache License 2.0 License for 
# more details.
#
####################################################################


import unittest
from analyze_site import Crawler, Page, Analytics
from tempfile import TemporaryFile


class TestCrawler(unittest.TestCase):
    def testInit(self):
        url = "http://httpbin.org/"
        crawler = Crawler(url, 1, ".")
        self.assertEqual(crawler.base_url, url)

    def testUpdateWordcount(self):
        url = "http://httpbin.org/"
        crawler = Crawler(url, 1, ".")
        crawler.wordcount = dict()
        dict1 = {"one":1, "two": 2}
        crawler.updateWordcount(dict1)
        self.assertEqual(2, len(crawler.wordcount))
        self.assertEqual(1, crawler.wordcount["one"])
        self.assertEqual(2, crawler.wordcount["two"])
        crawler.updateWordcount(dict1)
        self.assertEqual(2, len(crawler.wordcount))
        self.assertEqual(2, crawler.wordcount["one"])
        self.assertEqual(4, crawler.wordcount["two"])

    def testStart(self):
        url = "http://httpbin.org/"
        crawler = Crawler(url, 0, ".")
        crawler.start()
        self.assertEqual(7, crawler.wordcount["containing"])


class TestPage(unittest.TestCase):
    def testInit(self):
        url = "http://httpbin.org/"
        page = Page(url)
        self.assertEqual(page.base_url, url)

    def testWordcount(self):
        url = "http://base.com/"
        page = Page(url)
        html = "<!doctype html><html><body>aaa  aaa bbb<body><html>"
        page.feed(html)
        self.assertEqual(2, len(page.wordcount))
        self.assertEqual(2, page.wordcount['aaa'])
        self.assertEqual(1, page.wordcount['bbb'])

    def testLinks(self):
        url = "http://base.com/"
        page = Page(url)
        absUrl = "http://foo.com/bar"
        relUrl = "relative.html"
        html = "<!doctype html><html><body><a href='{}'>bar</a><a href='{}'>rel</a><body><html>".format(absUrl, relUrl)
        page.feed(html)
        self.assertEqual(2,len(page.links))
        self.assertTrue(absUrl in page.links)
        fullRelUrl = url + relUrl
        self.assertTrue(fullRelUrl in page.links)

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.keyfile = TemporaryFile('w')
        keywords = ["foo", "bar", "faz"]
        for keyword in keywords:
            self.keyfile.write("{}\n".format(keyword))

        self.keyfile.flush()


    def testInit(self):
        analytics = Analytics(self.keyfile.name)
        self.assertIsInstance(analytics, Analytics)


    def testKeywords(self):
        analytics = Analytics(self.keyfile.name)
        self.assertEqual(self.keyfile.name, analytics.keyword_file)
        for keyword in analytics.keywords:
            self.assertTrue(keyword in analytics.keywords)

if __name__ == "__main__":
    unittest.main()
