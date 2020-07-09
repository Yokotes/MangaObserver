from lxml import etree
import urllib

class XpathOptimizer():
    # TODO: 1. Fix spaces between img and @src
    
    # Generate new short xpath
    def __shorten_path(self, tree, path, removed):
        r = removed
        elem = tree.xpath(path)[0]
        elem_class = elem.get('class')
        elem_id = elem.get('id')
        if elem_class == None and elem_id == None:
            removed_part = list(path.split('/')).pop(len(path.split('/'))-1)
            r.append(removed_part)
            xpath = '/'.join(list(path.split('/')).remove(removed_part))
            return self.__shorten_path(tree, xpath, r)
        elif elem_class == None:
            return "//*[@id='" + elem_id + "']/" + "/".join(r)
        else:
            return "//*[@class='" + elem_class + "']/" + "/".join(r)

    # Optimize all manga site xpaths
    def optimize_xpaths(self, manga_site):
        page = self.__get_page(manga_site['test_link'])
        if page == '': return None
        html_parser = etree.HTMLParser()
        tree = etree.parse(page, html_parser)

        optimized_xpaths = []
        for xpath in manga_site['xpaths']:
            current_xpath = manga_site['xpaths'][xpath]
            if '/@src' in current_xpath:
                current_xpath = current_xpath.replace('/@src', '')
            elem = tree.xpath(current_xpath)[0]
            tag = elem.tag
            if tag == 'img' or 'h' in tag or tag == 'a' or elem.get('class') == None:
                list_xpath = current_xpath.split('/')
                removed_part = list_xpath.pop(len(list_xpath)-1)
                kek = '/'.join(list_xpath)
                shorten_xpath = self.__shorten_path(tree, kek, [removed_part,])
                if tag == 'img': 
                    shorten_xpath += '/@src'
            else:
                elem_class = elem.get('class')
                shorten_xpath = "//*[@class='" + elem_class + "']"
            optimized_xpaths.append(shorten_xpath)
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
        try:
            req = urllib.request.Request(url, headers=hdr)
            page = urllib.request.urlopen(req)
        except: return ''
        return page