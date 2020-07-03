from utilities.file_builder import File_Builder
from other.manga_site import MangaSite
from utilities.manga_parser import MangaParser
from other.manga import Manga
from PyQt5 import QtCore, QtWidgets
import asyncio
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
        self.loop = asyncio.new_event_loop()
        self.loop.create_task(self.__getData())
        self.loop.create_task(self.__updateManga())
        self.loop.run_forever()

    # Async update mangas in file
    async def __updateManga(self):
        while True:
            tasks = []
            for manga in self.manga_list:
                tasks.append(manga.update(self.latests))
            
            if len(tasks) > 0: await asyncio.wait(tasks)
            await asyncio.sleep(1)

    # Async get data from files and fill variables
    async def __getData(self):
        while True:
            # Read raw data from files
            raw_manga = await self.fb.readFromFileAsync('./data/manga.json')
            raw_manga_sites = await self.fb.readFromFileAsync('./data/manga_sites.json')

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
            if raw_manga != None:
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
                
            await asyncio.sleep(1)

    # Start backend thread
    def watch(self):
        self.backendThread.start()

    # Get inner observator's variable
    def add_manga_observer(self, observer):
        if not observer in self.manga_observers:
            self.manga_observers.append(observer)

    # Get inner observator's variable
    def add_sites_observer(self, observer):
        if not observer in self.sites_observers:
            self.sites_observers.append(observer)
    
    # Get inner observator's variable
    def add_latest_observer(self, observer):
        if not observer in self.latest_observers:
            self.latest_observers.append(observer)

# BackendThread
class BackendThread(QtCore.QThread):
    def __init__(self, parent=None, func=None):
        super(BackendThread, self).__init__(parent)
        self.value = 0
        self.func = func

    def run(self):
        while self.value < 100:
            self.value += 1
            if self.func != None: self.func()
            time.sleep(0.03)