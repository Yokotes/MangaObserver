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
import urllib

class XpathOptimizer():
    
    # Generate new short xpath
    def __shorten_path(self, tree, path, removed):
        r = removed
        elem = tree.xpath(path)[0]
        elem_class = elem.get('class')
        elem_id = elem.get('id')
        if elem_class is None and elem_id is None:
            removed_part = list(path.split('/')).pop(len(path.split('/'))-1)
            r.insert(0, removed_part)
            splited_path = path.split('/')
            splited_path.remove(removed_part)
            xpath = '/'.join(splited_path)
            return self.__shorten_path(tree, xpath, r)
        elif elem_class == None:
            return "//*[@id='" + elem_id + "']/" + "/".join(r)
        else:
            return "//*[@class='" + elem_class + "']/" + "/".join(r)

    # Optimize all manga site xpaths
    def optimize_xpaths(self, manga_site):
        page = self.__get_page(manga_site['test_link'])
        if page is None: return None

        try:
            tree = html.fromstring(page)
        except: 
            return None

        optimized_xpaths = []
        for xpath in manga_site['xpaths']:
            current_xpath = manga_site['xpaths'][xpath]
            
            # Delete useless parts
            if '/text()' in current_xpath:
                current_xpath = current_xpath.replace('/text()', '')
            if '/tbody' in current_xpath:
                current_xpath = current_xpath.replace('/tbody', '')
            if '/@src' in current_xpath:
                current_xpath = current_xpath.replace('/@src', '')
            
            # Getting all elems by xpath
            elems_list = tree.xpath(current_xpath)

            # Check elems count
            if elems_list == []:
                optimized_xpaths.append(current_xpath)
                continue

            # Getting elems data
            elem = elems_list[0]
            tag = elem.tag

            # Optimizing paths
            if ((tag == 'img' or 'h' in tag or tag == 'a' or 
                elem.get('class') == None) and len(current_xpath.split('/')) > 3):
                list_xpath = current_xpath.split('/')
                removed_part = list_xpath.pop(len(list_xpath)-1)
                path = '/'.join(list_xpath)
                shorten_xpath = self.__shorten_path(tree, path, [removed_part,])
            else:
                elem_class = elem.get('class')
                elem_id = elem.get('id')
                if elem_class == None:
                    shorten_xpath = "//*[@id='" + elem_id + "']"
                else:
                    shorten_xpath = "//*[@class='" + elem_class + "']"

            if tag == 'img': 
                    shorten_xpath += '/@src'

            optimized_xpaths.append(shorten_xpath)
        
        # Convert optimized xpaths to manga_site format
        data = {
            'name': manga_site['name'],
            'optimized': True,
            'test_link': manga_site['test_link'],
            'xpaths': {
                'title': optimized_xpaths[0],
                'descr': optimized_xpaths[1],
                'img': optimized_xpaths[2],
                'latest': optimized_xpaths[3]
            }
        }
        return data

    # Get HTML from test page's url
    def __get_page(self, url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        data = None
        try:
            req = urllib.request.Request(url, headers=hdr)
            with urllib.request.urlopen(req) as response:
                data = response.read()
            return data
        except: 
            return None