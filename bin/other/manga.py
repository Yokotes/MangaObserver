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

from ..utilities.manga_parser import MangaParser
from ..utilities.file_builder import File_Builder
import asyncio

class Manga():
    def __init__(self, manga_site, data=None):
        self.site = manga_site
        self.data = data
        self.parser = MangaParser()
        self.fb = File_Builder()

    # Async update function
    async def update(self, latests_list):
        old_data = self.data['info']['latest']
        result = ''
        # Get data from parser
        result = await self.parser.parseUrl(self.site, self.data['url'])
        if result != '':
            self.data['name'] = result['title']
            if old_data != result['info']['latest']:
                latests_list.append(self.data['name'])
            self.data['info']['latest'] = result['info']['latest']
            self.data['info']['descr'] = result['info']['descr']
            self.data['info']['img'] = result['info']['img']

            # Convert data to a dict
            file_data = {
                'url': self.data['url'],
                'name': self.data['name'],
                'site': self.site.name,
                'info': {
                    'descr': self.data['info']['descr'],
                    'img': self.data['info']['img'],
                    'latest': self.data['info']['latest'] 
                }
            }
            # Write data to the manga.json file
            if old_data != result['info']['latest'] or self.data['name'] == 'New item': await self.fb.writeToFileAsync('./data/manga.json', file_data)