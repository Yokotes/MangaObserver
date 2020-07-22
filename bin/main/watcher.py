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
from ..other.manga import Manga
from ..other.manga_site import MangaSite
from PyQt5 import QtCore, QtWidgets
import time

class Watcher():
    def __init__(self):
        self.backendThread = BackendThread(func=self.__backendLoop)
        self.fb = File_Builder()
        self.manga_list = []
        self.manga_sites_list = []
        self.latests = []
        self.manga_observers = []
        self.sites_observers = []
        self.latest_observers = []

    # Main backend loop
    def __backendLoop(self):
        while True:
            self.__getData()
            self.__updateManga()
            time.sleep(0.1)

    # Update mangas in file
    def __updateManga(self):
        for manga in self.manga_list:
            manga.update(self.latests)

    # Get data from files and fill variables
    def __getData(self):
        # Read raw data from files
        raw_manga = self.fb.readFromFile('./data/manga.json')
        raw_manga_sites = self.fb.readFromFile('./data/manga_sites.json')

        sites_len = len(self.manga_sites_list)

        # Clear all lists
        self.manga_sites_list.clear()
        self.manga_list.clear()

        # Convert raw sites data
        if raw_manga_sites != None:
            for manga_site in raw_manga_sites:
                ms = MangaSite(manga_site['name'], manga_site['xpaths'], manga_site['test_link'])
                ms.optimized = manga_site['optimized']
                self.manga_sites_list.append(ms)

        # Convert raw mangas data
        if raw_manga is not None:
            for manga in raw_manga:
                site = list(filter(lambda x: x if x.name == manga['site'] else None, list(self.manga_sites_list)))
                new_manga = Manga(site[0], manga)
                self.manga_list.append(new_manga)

        # Notice all manga's observers
        for observer in self.manga_observers:
            observer.clear()
            observer.extend(self.manga_list)

        # Notice all site's observers
        if sites_len != len(self.manga_sites_list):
            for observer in self.sites_observers:
                observer.clear()
                observer.extend(self.manga_sites_list)

        # Notice all latest's observers
        if len(self.latests) > 0:
            for observer in self.latest_observers:
                observer.extend(self.latests)
            self.latests.clear()

    # Start backend thread
    def watch(self):
        self.backendThread.start()

    # Get inner observator's variable
    def add_manga_observer(self, observer):
        if observer not in self.manga_observers:
            self.manga_observers.append(observer)

    # Get inner observator's variable
    def add_sites_observer(self, observer):
        if observer not in self.sites_observers:
            self.sites_observers.append(observer)
    
    # Get inner observator's variable
    def add_latest_observer(self, observer):
        if observer not in self.latest_observers:
            self.latest_observers.append(observer)

# BackendThread
class BackendThread(QtCore.QThread):
    def __init__(self, parent=None, func=None):
        super(BackendThread, self).__init__(parent)
        self.func = func

    def run(self):
        while True:
            if self.func is not None: 
                self.func()
            time.sleep(1)