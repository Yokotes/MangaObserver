# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets, Qt
# from ui.main_window import Ui_MainWindow
from main.ui_manager import UIManager
from main.watcher import Watcher

if __name__ == "__main__":
    watcher = Watcher()
    ui_manager = UIManager()

    watcher.add_manga_observer(ui_manager.manga_changes)
    watcher.add_sites_observer(ui_manager.manga_sites)
    watcher.add_latest_observer(ui_manager.latests)

    watcher.watch()
    ui_manager.start()