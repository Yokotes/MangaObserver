# =========================================================================
# Copyright 2020 Viktor Borzov

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#========================================================================== 

from lxml import html
import requests
from .file_builder import File_Builder

class MangaParser():
    def __init__(self):
        self.fb = File_Builder()

    # Parse manga by url
    def parseUrl(self, manga_site, url):
        page = self.get_page(url)
        if page is None: return ''
        data = ''
        try:
            tree = html.fromstring(page)

            data = {
                'title': (tree.xpath(manga_site.xpaths['title'])[0]).text if tree.xpath(manga_site.xpaths['title']) else url,
                'info': {
                    'latest': (tree.xpath(manga_site.xpaths['latest'])[0]).text if tree.xpath(manga_site.xpaths['latest']) else "Can't get a latest",
                    'img': tree.xpath(manga_site.xpaths['img']),
                    'descr': (tree.xpath(manga_site.xpaths['descr'])[0]).text if tree.xpath(manga_site.xpaths['descr']) else "Can't get a descr"
                }
            }
        except:
            pass
        finally:
            return data

    # Get HTML from url
    def get_page(self, url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        data = ''
        try:
            with requests.get(url, headers=hdr) as req:
                data = req.content
            return data
        except: 
            return None