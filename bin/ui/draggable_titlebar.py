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