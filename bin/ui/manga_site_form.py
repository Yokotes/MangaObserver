# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/manga_site_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
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

from .draggable_titlebar import DraggableTitleBar

class Ui_MangaSiteForm(object):
    def setupUi(self, MangaSiteForm):
        MangaSiteForm.setObjectName("MangaSiteForm")
        MangaSiteForm.resize(500, 639)
        MangaSiteForm.setMinimumSize(QtCore.QSize(500, 639))
        MangaSiteForm.setMaximumSize(QtCore.QSize(500, 639))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/logo80x80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MangaSiteForm.setWindowIcon(icon)
        MangaSiteForm.setStyleSheet("QDialog {\n"
"    background-color: white;\n"
"    border: 1px solid #9b9b9b\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-bottom: 2px solid #eb3131;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #eb3131;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c52828;\n"
"}")
        self.label_9 = QtWidgets.QLabel(MangaSiteForm)
        self.label_9.setGeometry(QtCore.QRect(150, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.addMangaSiteBtn = QtWidgets.QPushButton(MangaSiteForm)
        self.addMangaSiteBtn.setGeometry(QtCore.QRect(160, 590, 151, 31))
        self.addMangaSiteBtn.setObjectName("addMangaSiteBtn")
        self.label_8 = QtWidgets.QLabel(MangaSiteForm)
        self.label_8.setGeometry(QtCore.QRect(160, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.latestMangaEdit = QtWidgets.QTextEdit(MangaSiteForm)
        self.latestMangaEdit.setGeometry(QtCore.QRect(50, 430, 391, 31))
        self.latestMangaEdit.setObjectName("latestMangaEdit")
        self.label_5 = QtWidgets.QLabel(MangaSiteForm)
        self.label_5.setGeometry(QtCore.QRect(180, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.descrMangaEdit = QtWidgets.QTextEdit(MangaSiteForm)
        self.descrMangaEdit.setGeometry(QtCore.QRect(50, 250, 391, 31))
        self.descrMangaEdit.setObjectName("descrMangaEdit")
        self.label_6 = QtWidgets.QLabel(MangaSiteForm)
        self.label_6.setGeometry(QtCore.QRect(160, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MangaSiteForm)
        self.label_7.setGeometry(QtCore.QRect(180, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.siteNameEdit = QtWidgets.QTextEdit(MangaSiteForm)
        self.siteNameEdit.setGeometry(QtCore.QRect(50, 70, 391, 31))
        self.siteNameEdit.setObjectName("siteNameEdit")
        self.titleMangaEdit = QtWidgets.QTextEdit(MangaSiteForm)
        self.titleMangaEdit.setGeometry(QtCore.QRect(50, 160, 391, 31))
        self.titleMangaEdit.setObjectName("titleMangaEdit")
        self.imgMangaEdit = QtWidgets.QTextEdit(MangaSiteForm)
        self.imgMangaEdit.setGeometry(QtCore.QRect(50, 340, 391, 31))
        self.imgMangaEdit.setObjectName("imgMangaEdit")
        self.testLinkEdit = QtWidgets.QTextEdit(MangaSiteForm)
        self.testLinkEdit.setGeometry(QtCore.QRect(50, 520, 391, 31))
        self.testLinkEdit.setObjectName("testLinkEdit")
        self.label_10 = QtWidgets.QLabel(MangaSiteForm)
        self.label_10.setGeometry(QtCore.QRect(180, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.windowHeader = DraggableTitleBar(MangaSiteForm, MangaSiteForm)
        self.windowHeader.setGeometry(QtCore.QRect(0, 0, 501, 30))
        self.windowHeader.setStyleSheet("QGroupBox {\n"
"    border: none;\n"
"    background-color: #eb3131\n"
"}")
        self.windowHeader.setTitle("")
        self.windowHeader.setObjectName("windowHeader")
        self.closeBtn = QtWidgets.QPushButton(self.windowHeader)
        self.closeBtn.setGeometry(QtCore.QRect(450, 0, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")
        self.minBtn = QtWidgets.QPushButton(self.windowHeader)
        self.minBtn.setGeometry(QtCore.QRect(410, 0, 30, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.minBtn.setFont(font)
        self.minBtn.setObjectName("minBtn")
        self.label_15 = QtWidgets.QLabel(self.windowHeader)
        self.label_15.setGeometry(QtCore.QRect(30, 0, 47, 30))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("./img/header_logo.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")

        self.retranslateUi(MangaSiteForm)
        QtCore.QMetaObject.connectSlotsByName(MangaSiteForm)
        MangaSiteForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def retranslateUi(self, MangaSiteForm):
        _translate = QtCore.QCoreApplication.translate
        MangaSiteForm.setWindowTitle(_translate("MangaSiteForm", "Manga site settings"))
        self.label_9.setText(_translate("MangaSiteForm", "Xpath последней главы"))
        self.addMangaSiteBtn.setText(_translate("MangaSiteForm", "Добавить новый сайт"))
        self.label_8.setText(_translate("MangaSiteForm", "Xpath картинки манги"))
        self.label_5.setText(_translate("MangaSiteForm", "Название сайта"))
        self.label_6.setText(_translate("MangaSiteForm", "Xpath названия манги"))
        self.label_7.setText(_translate("MangaSiteForm", "Xpath описания"))
        self.label_10.setText(_translate("MangaSiteForm", "Тестовая ссылка"))
        self.closeBtn.setText(_translate("MangaSiteForm", "🞪"))
        self.minBtn.setText(_translate("MangaSiteForm", "−"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MangaSiteForm = QtWidgets.QDialog()
    ui = Ui_MangaSiteForm()
    ui.setupUi(MangaSiteForm)
    MangaSiteForm.show()
    sys.exit(app.exec_())

