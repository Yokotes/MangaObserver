from PyQt5 import QtCore, QtGui, QtWidgets

class DraggableTitleBar(QtWidgets.QGroupBox):
    def __init__(self, parent, window):
        super().__init__(parent)
        self.offset = None
        self.window = window
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.window.move(self.window.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)
            
    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)