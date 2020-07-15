from PyQt5 import QtCore, QtGui, QtWidgets
from .draggable_titlebar import DraggableTitleBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 630)
        MainWindow.setMinimumSize(QtCore.QSize(900, 630))
        MainWindow.setMaximumSize(QtCore.QSize(900, 630))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/logo80x80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: white;\n"
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
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 580, 290, 50))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid #9d9d9d;\n"
"    background-color: #e5e3e3;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.addMangaBtn_3 = QtWidgets.QPushButton(self.groupBox)
        self.addMangaBtn_3.setGeometry(QtCore.QRect(81, 10, 127, 30))
        self.addMangaBtn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addMangaBtn_3.setObjectName("addMangaBtn_3")
        self.mangaList = QtWidgets.QListWidget(self.centralwidget)
        self.mangaList.setGeometry(QtCore.QRect(0, 30, 290, 551))
        self.mangaList.setStyleSheet("QListWidget {\n"
"    border: 1px solid #9d9d9d \n"
"}")
        self.mangaList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mangaList.setAutoScroll(False)
        self.mangaList.setMovement(QtWidgets.QListView.Static)
        self.mangaList.setProperty("isWrapping", False)
        self.mangaList.setResizeMode(QtWidgets.QListView.Fixed)
        self.mangaList.setViewMode(QtWidgets.QListView.ListMode)
        self.mangaList.setWordWrap(True)
        self.mangaList.setObjectName("mangaList")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(289, 30, 611, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    border: 1px solid #9d9d9d;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #9d9d9d;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.startPage = QtWidgets.QWidget()
        self.startPage.setObjectName("startPage")
        self.label = QtWidgets.QLabel(self.startPage)
        self.label.setGeometry(QtCore.QRect(180, 120, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #eb3131")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.authorLink = QtWidgets.QCommandLinkButton(self.startPage)
        self.authorLink.setGeometry(QtCore.QRect(490, 560, 111, 61))
        self.authorLink.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.authorLink.setStyleSheet("QCommandLinkButton {\n"
"    background-color: transparent;\n"
"    color: #eb3131;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"    color: #c52828;\n"
"}")
        icon = QtGui.QIcon.fromTheme("none")
        self.authorLink.setIcon(icon)
        self.authorLink.setObjectName("authorLink")
        self.label_10 = QtWidgets.QLabel(self.startPage)
        self.label_10.setGeometry(QtCore.QRect(250, 30, 75, 75))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./img/logo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.siteGroupBox = QtWidgets.QGroupBox(self.startPage)
        self.siteGroupBox.setGeometry(QtCore.QRect(40, 200, 531, 141))
        self.siteGroupBox.setStyleSheet("")
        self.siteGroupBox.setTitle("")
        self.siteGroupBox.setObjectName("siteGroupBox")
        self.goToAddMangaSite = QtWidgets.QPushButton(self.siteGroupBox)
        self.goToAddMangaSite.setGeometry(QtCore.QRect(380, 60, 131, 31))
        self.goToAddMangaSite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goToAddMangaSite.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"}")
        self.goToAddMangaSite.setObjectName("goToAddMangaSite")
        self.label_11 = QtWidgets.QLabel(self.siteGroupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 5, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #4e4e4e")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.siteGroupBox)
        self.label_12.setGeometry(QtCore.QRect(20, 60, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #535353")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.siteGroupBox_2 = QtWidgets.QGroupBox(self.startPage)
        self.siteGroupBox_2.setGeometry(QtCore.QRect(40, 360, 531, 141))
        self.siteGroupBox_2.setStyleSheet("")
        self.siteGroupBox_2.setTitle("")
        self.siteGroupBox_2.setObjectName("siteGroupBox_2")
        self.goToAddMangaBtn = QtWidgets.QPushButton(self.siteGroupBox_2)
        self.goToAddMangaBtn.setGeometry(QtCore.QRect(380, 60, 131, 31))
        self.goToAddMangaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goToAddMangaBtn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"}")
        self.goToAddMangaBtn.setObjectName("goToAddMangaBtn")
        self.label_13 = QtWidgets.QLabel(self.siteGroupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 5, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #4e4e4e")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.siteGroupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 60, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #535353")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.startPage)
        self.label_16.setGeometry(QtCore.QRect(10, 570, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #8a8a8a")
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.startPage)
        self.showMangaInfo = QtWidgets.QWidget()
        self.showMangaInfo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.showMangaInfo.setObjectName("showMangaInfo")
        self.imageLabel = QtWidgets.QLabel(self.showMangaInfo)
        self.imageLabel.setGeometry(QtCore.QRect(20, 20, 181, 241))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet("")
        self.imageLabel.setText("")
        self.imageLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.imageLabel.setObjectName("imageLabel")
        
        self.titleLabel = QtWidgets.QLabel(self.showMangaInfo)
        self.titleLabel.setGeometry(QtCore.QRect(220, 20, 361, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.titleLabel.setStyleSheet("color: #eb3131;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.titleLabel.setObjectName("titleLabel")
        self.info_backBtn = QtWidgets.QPushButton(self.showMangaInfo)
        self.info_backBtn.setGeometry(QtCore.QRect(20, 559, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_backBtn.setFont(font)
        self.info_backBtn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: #eb3131;\n"
"}")
        self.info_backBtn.setObjectName("info_backBtn")
        self.descrLabel = QtWidgets.QLabel(self.showMangaInfo)
        self.descrLabel.setGeometry(QtCore.QRect(20, 280, 571, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descrLabel.setFont(font)
        self.descrLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.descrLabel.setTextFormat(QtCore.Qt.RichText)
        self.descrLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descrLabel.setWordWrap(True)
        self.descrLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.descrLabel.setObjectName("descrLabel")
        self.deleteMangaBtn = QtWidgets.QPushButton(self.showMangaInfo)
        self.deleteMangaBtn.setGeometry(QtCore.QRect(484, 559, 111, 31))
        self.deleteMangaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteMangaBtn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"}")
        self.deleteMangaBtn.setObjectName("deleteMangaBtn")
        self.latestBtn = QtWidgets.QPushButton(self.showMangaInfo)
        self.latestBtn.setGeometry(QtCore.QRect(220, 226, 361, 35))
        self.latestBtn.setObjectName("latestBtn")
        self.latestBtn.setStyleSheet("font-size: 10pt")
        self.latestBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stackedWidget.addWidget(self.showMangaInfo)
        self.addMangaPage = QtWidgets.QWidget()
        self.addMangaPage.setObjectName("addMangaPage")
        self.mangaUrlEdit = QtWidgets.QTextEdit(self.addMangaPage)
        self.mangaUrlEdit.setGeometry(QtCore.QRect(90, 170, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mangaUrlEdit.setFont(font)
        self.mangaUrlEdit.setStyleSheet("QTextEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-bottom: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}")
        self.mangaUrlEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mangaUrlEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mangaUrlEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.mangaUrlEdit.setAcceptRichText(True)
        self.mangaUrlEdit.setObjectName("mangaUrlEdit")
        self.label_2 = QtWidgets.QLabel(self.addMangaPage)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #eb3131;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.addMangaPage)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #eb3131;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.addMangaPage)
        self.label_4.setGeometry(QtCore.QRect(90, 250, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #eb3131;")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.addMangaPage)
        self.comboBox.setGeometry(QtCore.QRect(90, 290, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.addMangaBtn = QtWidgets.QPushButton(self.addMangaPage)
        self.addMangaBtn.setGeometry(QtCore.QRect(90, 400, 171, 41))
        self.addMangaBtn.setObjectName("addMangaBtn")
        self.goToMangaSitePageBtn = QtWidgets.QPushButton(self.addMangaPage)
        self.goToMangaSitePageBtn.setGeometry(QtCore.QRect(320, 400, 141, 41))
        self.goToMangaSitePageBtn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"}")
        self.goToMangaSitePageBtn.setObjectName("goToMangaSitePageBtn")
        self.manga_backBtn = QtWidgets.QPushButton(self.addMangaPage)
        self.manga_backBtn.setGeometry(QtCore.QRect(10, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manga_backBtn.setFont(font)
        self.manga_backBtn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: #eb3131;\n"
"}")
        self.manga_backBtn.setObjectName("manga_backBtn")
        self.stackedWidget.addWidget(self.addMangaPage)
        self.addMangaSitePage = QtWidgets.QWidget()
        self.addMangaSitePage.setObjectName("addMangaSitePage")
        self.siteNameEdit = QtWidgets.QTextEdit(self.addMangaSitePage)
        self.siteNameEdit.setGeometry(QtCore.QRect(110, 60, 321, 31))
        self.siteNameEdit.setObjectName("siteNameEdit")
        self.titleMangaEdit = QtWidgets.QTextEdit(self.addMangaSitePage)
        self.titleMangaEdit.setGeometry(QtCore.QRect(110, 120, 321, 31))
        self.titleMangaEdit.setObjectName("titleMangaEdit")
        self.descrMangaEdit = QtWidgets.QTextEdit(self.addMangaSitePage)
        self.descrMangaEdit.setGeometry(QtCore.QRect(110, 180, 321, 31))
        self.descrMangaEdit.setObjectName("descrMangaEdit")
        self.imgMangaEdit = QtWidgets.QTextEdit(self.addMangaSitePage)
        self.imgMangaEdit.setGeometry(QtCore.QRect(110, 240, 321, 31))
        self.imgMangaEdit.setObjectName("imgMangaEdit")
        self.label_5 = QtWidgets.QLabel(self.addMangaSitePage)
        self.label_5.setGeometry(QtCore.QRect(20, 65, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.addMangaSitePage)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.addMangaSitePage)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.addMangaSitePage)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.addMangaSiteBtn = QtWidgets.QPushButton(self.addMangaSitePage)
        self.addMangaSiteBtn.setGeometry(QtCore.QRect(220, 380, 111, 31))
        self.addMangaSiteBtn.setObjectName("addMangaSiteBtn")
        self.latestMangaEdit = QtWidgets.QTextEdit(self.addMangaSitePage)
        self.latestMangaEdit.setGeometry(QtCore.QRect(110, 300, 321, 31))
        self.latestMangaEdit.setObjectName("latestMangaEdit")
        self.label_9 = QtWidgets.QLabel(self.addMangaSitePage)
        self.label_9.setGeometry(QtCore.QRect(20, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.addMangaSitePage)
        self.mangaSitesPage = QtWidgets.QWidget()
        self.mangaSitesPage.setObjectName("mangaSitesPage")
        self.listWidget = QtWidgets.QListWidget(self.mangaSitesPage)
        self.listWidget.setGeometry(QtCore.QRect(60, 100, 491, 381))
        self.listWidget.setObjectName("listWidget")
        self.mangaSitesGroupBox = QtWidgets.QGroupBox(self.mangaSitesPage)
        self.mangaSitesGroupBox.setGeometry(QtCore.QRect(60, 480, 491, 71))
        self.mangaSitesGroupBox.setTitle("")
        self.mangaSitesGroupBox.setObjectName("mangaSitesGroupBox")
        self.addMangaSite = QtWidgets.QPushButton(self.mangaSitesGroupBox)
        self.addMangaSite.setGeometry(QtCore.QRect(40, 20, 111, 31))
        self.addMangaSite.setObjectName("addMangaSite")
        self.changeMangaSite = QtWidgets.QPushButton(self.mangaSitesGroupBox)
        self.changeMangaSite.setGeometry(QtCore.QRect(180, 20, 121, 31))
        self.changeMangaSite.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"}")
        self.changeMangaSite.setObjectName("changeMangaSite")
        self.deleteMangaSite = QtWidgets.QPushButton(self.mangaSitesGroupBox)
        self.deleteMangaSite.setGeometry(QtCore.QRect(330, 20, 121, 31))
        self.deleteMangaSite.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #eb3131;\n"
"    color: #eb3131;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eb3131;\n"
"    color: white;\n"
"}")
        self.deleteMangaSite.setObjectName("deleteMangaSite")
        self.label_17 = QtWidgets.QLabel(self.mangaSitesPage)
        self.label_17.setGeometry(QtCore.QRect(210, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: #eb3131;")
        self.label_17.setObjectName("label_17")
        self.sites_backBtn = QtWidgets.QPushButton(self.mangaSitesPage)
        self.sites_backBtn.setGeometry(QtCore.QRect(10, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sites_backBtn.setFont(font)
        self.sites_backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sites_backBtn.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: #eb3131;\n"
"}")
        self.sites_backBtn.setObjectName("sites_backBtn")
        self.stackedWidget.addWidget(self.mangaSitesPage)
        self.windowHeader = DraggableTitleBar(self.centralwidget, MainWindow)
        self.windowHeader.setGeometry(QtCore.QRect(0, 0, 900, 30))
        self.windowHeader.setStyleSheet("QGroupBox {\n"
"    border: none;\n"
"    background-color: #eb3131\n"
"}")
        self.windowHeader.setTitle("")
        self.windowHeader.setObjectName("windowHeader")
        self.closeBtn = QtWidgets.QPushButton(self.windowHeader)
        self.closeBtn.setGeometry(QtCore.QRect(850, 0, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")
        self.minBtn = QtWidgets.QPushButton(self.windowHeader)
        self.minBtn.setGeometry(QtCore.QRect(810, 0, 30, 30))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MangaWatcher"))
        self.addMangaBtn_3.setText(_translate("MainWindow", "Добавить мангу"))
        self.label.setText(_translate("MainWindow", "Manga Watcher"))
        self.authorLink.setText(_translate("MainWindow", "@Viktor Borzov"))
        self.goToAddMangaSite.setText(_translate("MainWindow", "Добавить сайт  🡢"))
        self.label_11.setText(_translate("MainWindow", "Добавьте сайт манги"))
        self.label_12.setText(_translate("MainWindow", "Добавьте сайт манги, с которого программа будет брать информацию. Заполните xpaths названия манги, картинки, описания и последней главы."))
        self.goToAddMangaBtn.setText(_translate("MainWindow", "Добавить мангу  🡢"))
        self.label_13.setText(_translate("MainWindow", "Добавьте мангу в список"))
        self.label_14.setText(_translate("MainWindow", "Добавьте мангу в ваш список. Если выйдет новая глава, то вы получите уведомление, а манга в списке подсветиться зеленым."))
        self.label_16.setText(_translate("MainWindow", "ver: 1.0 beta"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.info_backBtn.setText(_translate("MainWindow", "«"))
        self.descrLabel.setText(_translate("MainWindow", "Title"))
        self.deleteMangaBtn.setText(_translate("MainWindow", "Удалить мангу"))
        self.latestBtn.setText(_translate("MainWindow", "Прочитать"))
        self.label_2.setText(_translate("MainWindow", "Добавить мангу"))
        self.label_3.setText(_translate("MainWindow", "URL"))
        self.label_4.setText(_translate("MainWindow", "САЙТ"))
        self.addMangaBtn.setText(_translate("MainWindow", "Добавить мангу в список"))
        self.goToMangaSitePageBtn.setText(_translate("MainWindow", "Добавить сайт манги"))
        self.manga_backBtn.setText(_translate("MainWindow", "«"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.label_6.setText(_translate("MainWindow", "Title xpath:"))
        self.label_7.setText(_translate("MainWindow", "Descr xpath:"))
        self.label_8.setText(_translate("MainWindow", "Img xpath:"))
        self.addMangaSiteBtn.setText(_translate("MainWindow", "Add manga site"))
        self.label_9.setText(_translate("MainWindow", "Latest xpath:"))
        self.addMangaSite.setText(_translate("MainWindow", "Добавить сайт"))
        self.changeMangaSite.setText(_translate("MainWindow", "Изменить"))
        self.deleteMangaSite.setText(_translate("MainWindow", "Удалить"))
        self.label_17.setText(_translate("MainWindow", "Список сайтов"))
        self.sites_backBtn.setText(_translate("MainWindow", "«"))
        self.closeBtn.setText(_translate("MainWindow", "🞪"))
        self.minBtn.setText(_translate("MainWindow", "−"))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

