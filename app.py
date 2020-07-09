# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets, Qt
# from ui.main_window import Ui_MainWindow
from bin.main.ui_manager import UIManager
from bin.main.watcher import Watcher
from bin.utilities.update_manager import UpdateManager

if __name__ == "__main__":
    watcher = Watcher()
    um = UpdateManager()
    ui_manager = UIManager(um)

    watcher.add_manga_observer(ui_manager.manga_changes)
    watcher.add_sites_observer(ui_manager.manga_sites)
    watcher.add_latest_observer(ui_manager.latests)

    watcher.watch()
    ui_manager.start()