import json
import os.path
import asyncio

class File_Builder():
    '''
        This class allows to work with files
    '''

    # Async write and rewrite json files
    async def writeToFileAsync(self, file, data):
        sites = []
        count = 0
        if os.path.exists(file):
            sites = await self.readFromFileAsync(file)

        if 'manga_sites.json' in file:
            for index, site in enumerate(sites):
                if site['name'] == data['name']:
                    sites[index] = data
                else: count += 1
            if count == len(sites): sites.append(data) 
        elif 'manga.json' in file:
            # if type(data) is list: sites = self.fromMangaToDict(data)
            # else: sites.append(data)

            for index, site in enumerate(sites):
                if site['url'] == data['url']:
                    sites[index] = data
                else: count += 1

        if count == len(sites): sites.append(data)
        try:
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(sites, f, ensure_ascii=False)
        except:
            raise Exception('Failed to async write data to the file!')
    
    # Write and rewrite json files
    def writeToFile(self, file, data):
        sites = []
        count = 0
        if os.path.exists(file):
            sites = self.readFromFile(file)

        if 'manga_sites.json' in file:
            for index, site in enumerate(sites):
                if site['name'] == data['name']:
                    sites[index] = data
                else: count += 1
            if count == len(sites): sites.append(data) 
        elif 'manga.json' in file:
            for index, site in enumerate(sites):
                if site['url'] == data['url']:
                    sites[index] = data
                else: count += 1

        if count == len(sites): sites.append(data)
        try:
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(sites, f, ensure_ascii=False)
        except:
            raise Exception('Failed to write data to the file!')

    # Async read data from json file
    async def readFromFileAsync(self, file):
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data
            except:
                raise Exception('Failed to async load data!')
        else: return None

    # Read data from json file
    def readFromFile(self, file):
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data
            except:
                raise Exception('Failed to load data!')
        else: return None

    # Delete data from file
    def deleteFromFile(self, file, data):
        if 'manga_sites.json' in file:
            deleted_item = self.manga_site_to_dict(list([data]))
        elif 'manga.json' in file:
            deleted_item = self.manga_to_dict(list([data]))

        file_content = self.readFromFile(file)
        file_content.remove(deleted_item[0])

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(file_content, f, ensure_ascii=False)

    # Convert manga objects to dict
    def manga_to_dict(self, manga_list):
        list_of_dict = []
        for manga in manga_list:
            manga_dict = {
                'url': manga.data['url'],
                'name': manga.data['name'],
                'site': manga.site.name,
                'info': {
                    'descr': manga.data['info']['descr'],
                    'img': manga.data['info']['img'],
                    'latest': manga.data['info']['latest']
                }
            }
            list_of_dict.append(manga_dict)
        return list_of_dict

    # Convert manga objects to dict
    def manga_site_to_dict(self, site_list):
        list_of_dict = []
        for site in site_list:
            data = {
                'name': site.name,
                'optimized': site.optimized,
                'test_link': site.test_link,
                'xpaths': {
                    'title': site.xpaths['title'],
                    'descr': site.xpaths['descr'],
                    'img': site.xpaths['img'],
                    'latest': site.xpaths['latest']
                }
            }
            list_of_dict.append(data)
        return list_of_dict