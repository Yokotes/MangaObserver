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

from PyQt5 import QtCore, QtGui, QtWidgets
from ..ui.main_window import Ui_MainWindow
from ..ui.manga_site_form import Ui_MangaSiteForm
import sys
import webbrowser
from ..utilities.file_builder import File_Builder
from ..utilities.xpath_optimizer import XpathOptimizer
import time
import requests

class UIManager():
    def __init__(self, update_manager):
        # Initialize update manager
        self.update_manager = update_manager

        # Initialize all windows and forms
        self.__init_main_window()
        self.__init_manga_site_form()

        # Create variables that will contains all watcher's changes
        self.manga_changes = []
        self.manga_list = []
        self.manga_sites = []
        self.latests = []
        self.manga_sites_dict = {}

        # Base variables from main window
        self.stackedWidget = self.main_window.stackedWidget
        self.file_builder = File_Builder()
        self.optimizer = XpathOptimizer()

        # Hook logic for main window
        self.__set_main_window_behavior()
        self.__set_manga_site_behavior()

        self.__start_update_loop()

    # Start update loop
    def __start_update_loop(self):
        self.updateThread = UpdateThread(func=self.__update_loop)
        self.updateThread.start()

    # Update loop
    def __update_loop(self):
        while True:
            # Check sites changes
            if len(self.manga_sites) > 0:

                # Fill sites list
                if self.main_window.listWidget.count() < len(self.manga_sites):
                    for i in range(self.main_window.listWidget.count(),
                                    len(self.manga_sites)):
                        self.main_window.listWidget.insertItem(i, self.manga_sites[i].name)
                
                # Fill sites combobox
                if self.main_window.comboBox.count() < len(self.manga_sites):
                    for i in range(self.main_window.comboBox.count(),
                                    len(self.manga_sites)):
                        self.main_window.comboBox.insertItem(i, self.manga_sites[i].name)
            
            # Check manga's changes
            if len(self.manga_changes) > 0:
                self.manga_list.clear()
                self.manga_list.extend(self.manga_changes)
                if self.main_window.mangaList.count() < len(self.manga_list):

                    # Fill manga list widget
                    for i in range(self.main_window.mangaList.count(),
                                    len(self.manga_list)):
                        manga = self.manga_list[i]
                        manga_site = manga.site

                        # Fill manga sites dict
                        if manga_site.name in self.manga_sites_dict:
                            self.manga_sites_dict[manga_site.name] += 1
                        else:
                            self.manga_sites_dict[manga_site.name] = 1

                        # Fill manga list
                        if manga.data['name'] == 'New item': continue
                        item = QtWidgets.QListWidgetItem()
                        item.setText(manga.data['name'] +'\n('+ manga_site.name+')')
                        pixmap = QtGui.QPixmap()
                        try:
                            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                                    'Accept-Encoding': 'none',
                                    'Accept-Language': 'en-US,en;q=0.8',
                                    'Connection': 'keep-alive'}

                            img_url = manga.data['info']['img'][0]
                            if img_url[0] == '/':
                                help_url = manga.data['url'].split('/')[2]
                                img_url = 'https://' + help_url + img_url

                            with requests.get(img_url, headers=hdr) as req:
                                image = req.content
                                
                            pixmap.loadFromData(image)
                        except:
                            pixmap.load('./img/image_placeholder.jpg')

                        item.setIcon(QtGui.QIcon(pixmap))
                        self.main_window.mangaList.insertItem(i, item)
                        time.sleep(0.01)
                    
            # Check lastests
            if len(self.latests) > 0 and self.main_window.mangaList.count() > 0:
                for name in self.latests:
                    items = self.main_window.mangaList.findItems(
                        name, QtCore.Qt.MatchContains)
                    if type(items) is list and items != []: item = items[0]
                    if item != None: 
                        item.setBackground(QtGui.QColor.fromRgbF(0, 0.8, 0, 0.3))
                    time.sleep(1)
                    self.trayIcon.showMessage('Вышла новая глава!', name, 
                        QtGui.QIcon(QtGui.QPixmap('./img/logo.png')))
                    self.latests.remove(name)
            time.sleep(1.5)

    # ==================================
    #   Windows and forms behavior
    # ==================================

    # Setting main window's elements behavior
    def __set_main_window_behavior(self):
        # ===============================
        #   Window header
        # ===============================

        # Close button behavior
        self.main_window.closeBtn.clicked.connect(
            lambda: self.__hide_main_window())
        
        # Minimize button behavior
        self.main_window.minBtn.clicked.connect(
            lambda: self.MainWindow.showMinimized())

        # ===============================
        #   Start page
        # ===============================

        # Go to add manga site page
        self.main_window.goToAddMangaSite.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(4))
        
        # Go to add manga page
        self.main_window.goToAddMangaBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2))
        
        # Link to the github
        self.main_window.authorLink.clicked.connect(
            lambda: webbrowser.open('https://github.com/Yokotes'))

        # ===============================
        #   Add manga page
        # ===============================

        # Go to add manga site page
        self.main_window.goToMangaSitePageBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(4))
        
        # Add manga to the manga.json file
        self.main_window.addMangaBtn.clicked.connect(self.__add_manga)

        # Back button
        self.main_window.manga_backBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))

        # ===============================   
        #   Manga sites page
        # ===============================

        # Open add manga site form
        self.main_window.addMangaSite.clicked.connect(
            lambda: self.__add_new_site())
        
        # Open manga site settings
        self.main_window.changeMangaSite.clicked.connect(
            lambda: self.__fill_manga_site_form())
        
        # Delete selected manga site
        
        self.main_window.deleteMangaSite.clicked.connect(
            lambda: self.__delete_manga_site())

        # Back button
        self.main_window.sites_backBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))

        # ===============================   
        #   Manga info page
        # ===============================

        # Open info by clicking on manga list item
        self.main_window.mangaList.itemClicked.connect(self.__show_manga_info)
        
        # Go to the start page
        self.main_window.info_backBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        
        # Delete selected manga
        self.main_window.deleteMangaBtn.clicked.connect(self.__delete_manga)

        # Go to the manga site
        self.main_window.latestBtn.clicked.connect(
            lambda: webbrowser.open(self.currentManga.data['url']))

        # ===============================   
        #   Manga list
        # ===============================
        self.main_window.addMangaBtn_3.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2))

    # Setting manga site's form behavior
    def __set_manga_site_behavior(self):

        # Add manga site
        self.manga_site_form.addMangaSiteBtn.clicked.connect(
            lambda: self.__add_manga_site())
        
        # TitleBar close button
        self.manga_site_form.closeBtn.clicked.connect(
            lambda: self.MangaSiteForm.close())

        # TitleBar minimize button
        self.manga_site_form.minBtn.clicked.connect(
            lambda: self.MangaSiteForm.showMinimized())

    # ==================================    
    #   Other functions
    # ==================================
    # Add manga site to the file
    def __add_manga_site(self):
        site_name = self.manga_site_form.siteNameEdit.toPlainText()
        title_xpath = self.manga_site_form.titleMangaEdit.toPlainText()
        descr_xpath = self.manga_site_form.descrMangaEdit.toPlainText()
        img_xpath = self.manga_site_form.imgMangaEdit.toPlainText()
        latest_xpath = self.manga_site_form.latestMangaEdit.toPlainText()
        test_link = self.manga_site_form.testLinkEdit.toPlainText()
        # Check all text edits
        if (title_xpath != '' and descr_xpath != '' and 
            img_xpath != '' and latest_xpath != ''):
            data = {
                'name': site_name,
                'optimized': False,
                'test_link': test_link,
                'xpaths': {
                    'title': title_xpath,
                    'descr': descr_xpath,
                    'img': img_xpath,
                    'latest': latest_xpath
                }
            }
            # Optimize xpaths
            optimized_site = self.optimizer.optimize_xpaths(data)

            # Write new manga site to the file
            if optimized_site is not None:
                self.file_builder.writeToFile(
                    file='./data/manga_sites.json', data=optimized_site)
            
            # Close window
            self.MangaSiteForm.close()

    # Delete manga
    def __delete_manga(self):
        index = self.main_window.mangaList.currentIndex().row()
        manga = self.manga_list[index]
        self.file_builder.deleteFromFile('./data/manga.json', manga)
        self.main_window.mangaList.takeItem(
            self.main_window.mangaList.currentIndex().row())
        self.manga_list.remove(manga)
        self.stackedWidget.setCurrentIndex(0)
        self.manga_sites_dict[manga.site.name] -= 1
        print(manga.site.name)

    # Show manga info
    def __show_manga_info(self, item):
        item.setBackground(QtGui.QColor.fromRgbF(1, 1, 1))
        self.main_window.stackedWidget.setCurrentIndex(1)
        self.main_window.imageLabel.setPixmap(item.icon().pixmap(
            self.main_window.imageLabel.width(), 
            self.main_window.imageLabel.height()))
        self.main_window.titleLabel.setText(item.text())
        index = self.main_window.mangaList.currentIndex().row()
        self.currentManga = self.manga_list[index]
        self.main_window.descrLabel.setText('\t'+self.currentManga.data['info']['descr'])
        latest = self.currentManga.data['info']['latest'].split('\n')
        for index, part in enumerate(latest):
            latest[index] = str(part).replace(' ', '')
        self.main_window.latestBtn.setText('Прочитать:  '+' '.join(latest))

    # Delete manga site
    def __delete_manga_site(self):
        index = self.main_window.listWidget.currentIndex().row()
        site = self.manga_sites.pop(index)
        self.main_window.comboBox.removeItem(index)

        # Create messagebox
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle('Оповещение')
        
        # Check if manga exist in manga site
        if site.name not in self.manga_sites_dict or self.manga_sites_dict[site.name] == 0:
            self.file_builder.deleteFromFile('./data/manga_sites.json', site)
            self.main_window.listWidget.takeItem(index)
            message_box.setText('Сайт удален из списка!')
        else:
            message_box.setText('Перед удалением сайта необходимо удалить мангу!')

        message_box.exec()
        
    # Open manga site form for adding new manga site
    def __add_new_site(self):
        self.manga_site_form.siteNameEdit.setText('')
        self.manga_site_form.titleMangaEdit.setText('')
        self.manga_site_form.descrMangaEdit.setText('')
        self.manga_site_form.imgMangaEdit.setText('')
        self.manga_site_form.latestMangaEdit.setText('')
        self.manga_site_form.testLinkEdit.setText('')

        self.MangaSiteForm.show()

    # Fill manga site form
    def __fill_manga_site_form(self):
        index = self.main_window.listWidget.currentIndex().row()
        if index != -1:
            self.MangaSiteForm.show()
            manga_site = self.manga_sites[index]

            self.manga_site_form.siteNameEdit.setText(
                manga_site.name)
            self.manga_site_form.titleMangaEdit.setText(
                manga_site.xpaths['title'])
            self.manga_site_form.descrMangaEdit.setText(
                manga_site.xpaths['descr'])
            self.manga_site_form.imgMangaEdit.setText(
                manga_site.xpaths['img'])
            self.manga_site_form.latestMangaEdit.setText(
                manga_site.xpaths['latest'])
            self.manga_site_form.testLinkEdit.setText(
                manga_site.test_link)

    # Add manga to the mang.json file
    def __add_manga(self):
        manga_url = self.main_window.mangaUrlEdit.toPlainText()
        manga_site = self.main_window.comboBox.currentText()
        if manga_url != '' and manga_site != '':
            # Create dict with user input data
            data = {
                'url': manga_url,
                'name': 'New item',
                'site': manga_site,
                'info': {
                    'descr': '',
                    'img': '',
                    'latest': ''
                }
            }
            # Write to the file
            self.file_builder.writeToFile('./data/manga.json', data)
            
            # Clear all textEdits and comboBoxes
            self.main_window.mangaUrlEdit.clear()
            self.main_window.comboBox.setCurrentIndex(0)

            # Show complete message
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle('Оповещение')
            message_box.setText('Манга добавлена в список!')
            message_box.exec()

    # Hide main window
    def __hide_main_window(self):
        self.MainWindow.hide()
        self.trayIcon.showMessage('Приложение MangaObserver работает в свернутом режиме',
                                    '↓', QtGui.QIcon(QtGui.QPixmap('./img/logo.png')))

    # Closing app and check version
    def close_app(self):
        self.MainWindow.close()
        self.MangaSiteForm.close()
        self.update_manager.watch_version()

    # Initialize main window
    def __init_main_window(self):
        # Create main app
        self.app = QtWidgets.QApplication(sys.argv)

        # Create UI for main app
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.main_window.mangaList.setIconSize(QtCore.QSize(50, 50))
        self.main_window.label_16.setText('ver.' + self.update_manager.current_version)
        self.trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(QtGui.QPixmap('./img/logo.png')))
        self.trayIcon.setParent(self.app)
        self.trayIcon.show()
        self.trayIcon.setToolTip('MangaObserver работает...')
        context_menu = QtWidgets.QMenu('Menu')
        open_action = context_menu.addAction('Открыть MangaObserver')
        exit_action = context_menu.addAction('Закрыть')
        self.trayIcon.setContextMenu(context_menu)
        open_action.triggered.connect(
            self.MainWindow.show)
        exit_action.triggered.connect(
            lambda: self.close_app())

    # Initialize manga site settings form
    def __init_manga_site_form(self):
        self.MangaSiteForm = QtWidgets.QDialog()
        self.manga_site_form = Ui_MangaSiteForm()
        self.manga_site_form.setupUi(self.MangaSiteForm)

    # Start frontend side of application
    def start(self):
        # Start main app
        sys.exit(self.app.exec_())
    
# Update thread
class UpdateThread(QtCore.QThread):
    def __init__(self, parent=None, func=None):
        super(UpdateThread, self).__init__(parent)
        self.value = 0
        self.func = func

    def run(self):
        while self.value < 100:
            self.value += 1
            if self.func != None: self.func()
            time.sleep(0.03)