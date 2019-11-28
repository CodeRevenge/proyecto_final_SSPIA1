# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\Interface_AGB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1288, 715)
        MainWindow.setMinimumSize(QtCore.QSize(1271, 657))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/inteligencia-artificial.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:images/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QDoubleSpinBox, QSpinBox\n"
"{\n"
"    border: 1px solid #b1b1b1;\n"
"    background-color: #323232;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus , QSpinBox:focus\n"
"{\n"
"    border: 2px solid #ffaa00;\n"
"    background-color: #4d4d4d;\n"
"}\n"
"\n"
"QDoubleSpinBox:!focus:hover , QSpinBox:!focus:hover\n"
"{\n"
"    border: 1px solid #7e7e7e;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    color:rgb(98, 98, 98);\n"
"    border-radius:5px;\n"
"    border: 1px solid rgb(65, 65, 65);\n"
"    background-color: rgb(66, 66, 66);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_box = QtWidgets.QGroupBox(self.tab)
        self.input_box.setMinimumSize(QtCore.QSize(800, 400))
        self.input_box.setObjectName("input_box")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.input_box)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tbl_resultados = QtWidgets.QTableWidget(self.input_box)
        self.tbl_resultados.setEnabled(True)
        self.tbl_resultados.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tbl_resultados.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbl_resultados.setAutoFillBackground(False)
        self.tbl_resultados.setStyleSheet("color: rgb(255, 255, 255);")
        self.tbl_resultados.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.tbl_resultados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_resultados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tbl_resultados.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tbl_resultados.setAutoScroll(False)
        self.tbl_resultados.setAutoScrollMargin(16)
        self.tbl_resultados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_resultados.setTabKeyNavigation(True)
        self.tbl_resultados.setProperty("showDropIndicator", False)
        self.tbl_resultados.setDragEnabled(False)
        self.tbl_resultados.setAlternatingRowColors(False)
        self.tbl_resultados.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tbl_resultados.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_resultados.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_resultados.setGridStyle(QtCore.Qt.DotLine)
        self.tbl_resultados.setWordWrap(True)
        self.tbl_resultados.setCornerButtonEnabled(False)
        self.tbl_resultados.setObjectName("tbl_resultados")
        self.tbl_resultados.setColumnCount(6)
        self.tbl_resultados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(5, item)
        self.tbl_resultados.horizontalHeader().setVisible(False)
        self.tbl_resultados.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_resultados.horizontalHeader().setDefaultSectionSize(130)
        self.tbl_resultados.horizontalHeader().setHighlightSections(True)
        self.tbl_resultados.horizontalHeader().setStretchLastSection(True)
        self.tbl_resultados.verticalHeader().setVisible(False)
        self.tbl_resultados.verticalHeader().setCascadingSectionResizes(True)
        self.tbl_resultados.verticalHeader().setDefaultSectionSize(35)
        self.tbl_resultados.verticalHeader().setHighlightSections(True)
        self.tbl_resultados.verticalHeader().setSortIndicatorShown(False)
        self.tbl_resultados.verticalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.tbl_resultados, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.input_box, 0, 0, 2, 2)
        self.control_box = QtWidgets.QGroupBox(self.tab)
        self.control_box.setMinimumSize(QtCore.QSize(0, 400))
        self.control_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.control_box.setObjectName("control_box")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.control_box)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.inp_hierro = QtWidgets.QDoubleSpinBox(self.control_box)
        self.inp_hierro.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_hierro.setFont(font)
        self.inp_hierro.setFrame(True)
        self.inp_hierro.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_hierro.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_hierro.setKeyboardTracking(True)
        self.inp_hierro.setDecimals(4)
        self.inp_hierro.setMinimum(-1.0)
        self.inp_hierro.setMaximum(999999.0)
        self.inp_hierro.setProperty("value", 0.008)
        self.inp_hierro.setObjectName("inp_hierro")
        self.gridLayout_5.addWidget(self.inp_hierro, 8, 1, 1, 2)
        self.inp_fibra = QtWidgets.QDoubleSpinBox(self.control_box)
        self.inp_fibra.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_fibra.setFont(font)
        self.inp_fibra.setFrame(True)
        self.inp_fibra.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_fibra.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_fibra.setKeyboardTracking(True)
        self.inp_fibra.setDecimals(2)
        self.inp_fibra.setMinimum(-1.0)
        self.inp_fibra.setMaximum(999999.0)
        self.inp_fibra.setProperty("value", 27.0)
        self.inp_fibra.setObjectName("inp_fibra")
        self.gridLayout_5.addWidget(self.inp_fibra, 6, 1, 1, 2)
        self.rb_ning = QtWidgets.QRadioButton(self.control_box)
        self.rb_ning.setEnabled(False)
        self.rb_ning.setObjectName("rb_ning")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_ning)
        self.gridLayout_5.addWidget(self.rb_ning, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 6, 0, 1, 1)
        self.cbx_sexo = QtWidgets.QComboBox(self.control_box)
        self.cbx_sexo.setObjectName("cbx_sexo")
        self.cbx_sexo.addItem("")
        self.cbx_sexo.addItem("")
        self.gridLayout_5.addWidget(self.cbx_sexo, 1, 1, 1, 2)
        self.rb_emb = QtWidgets.QRadioButton(self.control_box)
        self.rb_emb.setEnabled(False)
        self.rb_emb.setObjectName("rb_emb")
        self.buttonGroup.addButton(self.rb_emb)
        self.gridLayout_5.addWidget(self.rb_emb, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 8, 0, 1, 1)
        self.rb_lac = QtWidgets.QRadioButton(self.control_box)
        self.rb_lac.setEnabled(False)
        self.rb_lac.setObjectName("rb_lac")
        self.buttonGroup.addButton(self.rb_lac)
        self.gridLayout_5.addWidget(self.rb_lac, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.inp_calcio = QtWidgets.QDoubleSpinBox(self.control_box)
        self.inp_calcio.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_calcio.setFont(font)
        self.inp_calcio.setFrame(True)
        self.inp_calcio.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_calcio.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_calcio.setKeyboardTracking(True)
        self.inp_calcio.setDecimals(2)
        self.inp_calcio.setMinimum(-1.0)
        self.inp_calcio.setMaximum(999999.0)
        self.inp_calcio.setProperty("value", 1.0)
        self.inp_calcio.setObjectName("inp_calcio")
        self.gridLayout_5.addWidget(self.inp_calcio, 7, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 5, 0, 1, 1)
        self.inp_kcal = QtWidgets.QDoubleSpinBox(self.control_box)
        self.inp_kcal.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_kcal.setFont(font)
        self.inp_kcal.setFrame(True)
        self.inp_kcal.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_kcal.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_kcal.setKeyboardTracking(True)
        self.inp_kcal.setDecimals(2)
        self.inp_kcal.setMinimum(-1.0)
        self.inp_kcal.setMaximum(999999.0)
        self.inp_kcal.setProperty("value", 2900.0)
        self.inp_kcal.setObjectName("inp_kcal")
        self.gridLayout_5.addWidget(self.inp_kcal, 4, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.control_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 7, 0, 1, 1)
        self.btn_train = QtWidgets.QPushButton(self.control_box)
        self.btn_train.setEnabled(True)
        self.btn_train.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_train.setFont(font)
        self.btn_train.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_train.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.btn_train.setObjectName("btn_train")
        self.gridLayout_5.addWidget(self.btn_train, 9, 0, 1, 3)
        self.inp_edad = QtWidgets.QDoubleSpinBox(self.control_box)
        self.inp_edad.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_edad.setFont(font)
        self.inp_edad.setFrame(True)
        self.inp_edad.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_edad.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_edad.setKeyboardTracking(True)
        self.inp_edad.setDecimals(1)
        self.inp_edad.setMaximum(150.0)
        self.inp_edad.setSingleStep(1.0)
        self.inp_edad.setProperty("value", 22.0)
        self.inp_edad.setObjectName("inp_edad")
        self.gridLayout_5.addWidget(self.inp_edad, 0, 1, 1, 2)
        self.inp_vit_a = QtWidgets.QDoubleSpinBox(self.control_box)
        self.inp_vit_a.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_vit_a.setFont(font)
        self.inp_vit_a.setFrame(True)
        self.inp_vit_a.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_vit_a.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_vit_a.setKeyboardTracking(True)
        self.inp_vit_a.setDecimals(4)
        self.inp_vit_a.setMinimum(-1.0)
        self.inp_vit_a.setMaximum(999999.0)
        self.inp_vit_a.setProperty("value", 0.01)
        self.inp_vit_a.setObjectName("inp_vit_a")
        self.gridLayout_5.addWidget(self.inp_vit_a, 5, 1, 1, 2)
        self.line = QtWidgets.QFrame(self.control_box)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.control_box, 0, 2, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.error_graph = Error_Graph(self.tab_3)
        self.error_graph.setObjectName("error_graph")
        self.gridLayout_6.addWidget(self.error_graph, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 4, 0, 1, 1)
        self.inp_individuos = QtWidgets.QSpinBox(self.groupBox)
        self.inp_individuos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_individuos.setFont(font)
        self.inp_individuos.setFrame(True)
        self.inp_individuos.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_individuos.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_individuos.setKeyboardTracking(True)
        self.inp_individuos.setMinimum(1)
        self.inp_individuos.setMaximum(200)
        self.inp_individuos.setProperty("value", 8)
        self.inp_individuos.setObjectName("inp_individuos")
        self.gridLayout_7.addWidget(self.inp_individuos, 1, 2, 1, 2)
        self.inp_p_mutacion = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.inp_p_mutacion.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_p_mutacion.setFont(font)
        self.inp_p_mutacion.setFrame(True)
        self.inp_p_mutacion.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_p_mutacion.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_p_mutacion.setKeyboardTracking(True)
        self.inp_p_mutacion.setObjectName("inp_p_mutacion")
        self.gridLayout_7.addWidget(self.inp_p_mutacion, 4, 2, 1, 2)
        self.inp_generaciones = QtWidgets.QSpinBox(self.groupBox)
        self.inp_generaciones.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_generaciones.setFont(font)
        self.inp_generaciones.setFrame(True)
        self.inp_generaciones.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_generaciones.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.inp_generaciones.setKeyboardTracking(True)
        self.inp_generaciones.setMinimum(1)
        self.inp_generaciones.setMaximum(99999)
        self.inp_generaciones.setProperty("value", 2000)
        self.inp_generaciones.setObjectName("inp_generaciones")
        self.gridLayout_7.addWidget(self.inp_generaciones, 0, 2, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tbl_alimentos = QtWidgets.QTableWidget(self.tab_2)
        self.tbl_alimentos.setEnabled(True)
        self.tbl_alimentos.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tbl_alimentos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbl_alimentos.setAutoFillBackground(False)
        self.tbl_alimentos.setStyleSheet("color: rgb(255, 255, 255);")
        self.tbl_alimentos.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.tbl_alimentos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_alimentos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tbl_alimentos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tbl_alimentos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbl_alimentos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tbl_alimentos.setAutoScroll(False)
        self.tbl_alimentos.setAutoScrollMargin(16)
        self.tbl_alimentos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_alimentos.setTabKeyNavigation(True)
        self.tbl_alimentos.setProperty("showDropIndicator", False)
        self.tbl_alimentos.setDragEnabled(False)
        self.tbl_alimentos.setAlternatingRowColors(False)
        self.tbl_alimentos.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tbl_alimentos.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_alimentos.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_alimentos.setGridStyle(QtCore.Qt.DotLine)
        self.tbl_alimentos.setWordWrap(True)
        self.tbl_alimentos.setCornerButtonEnabled(False)
        self.tbl_alimentos.setObjectName("tbl_alimentos")
        self.tbl_alimentos.setColumnCount(6)
        self.tbl_alimentos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_alimentos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_alimentos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_alimentos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_alimentos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_alimentos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_alimentos.setHorizontalHeaderItem(5, item)
        self.tbl_alimentos.horizontalHeader().setVisible(False)
        self.tbl_alimentos.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_alimentos.horizontalHeader().setDefaultSectionSize(130)
        self.tbl_alimentos.horizontalHeader().setHighlightSections(True)
        self.tbl_alimentos.horizontalHeader().setStretchLastSection(True)
        self.tbl_alimentos.verticalHeader().setVisible(False)
        self.tbl_alimentos.verticalHeader().setCascadingSectionResizes(True)
        self.tbl_alimentos.verticalHeader().setDefaultSectionSize(35)
        self.tbl_alimentos.verticalHeader().setHighlightSections(True)
        self.tbl_alimentos.verticalHeader().setSortIndicatorShown(False)
        self.tbl_alimentos.verticalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tbl_alimentos, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tbl_informacion = QtWidgets.QTableWidget(self.tab_4)
        self.tbl_informacion.setEnabled(True)
        self.tbl_informacion.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tbl_informacion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbl_informacion.setAutoFillBackground(False)
        self.tbl_informacion.setStyleSheet("color: rgb(255, 255, 255);")
        self.tbl_informacion.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.tbl_informacion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_informacion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tbl_informacion.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tbl_informacion.setAutoScroll(False)
        self.tbl_informacion.setAutoScrollMargin(16)
        self.tbl_informacion.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_informacion.setTabKeyNavigation(True)
        self.tbl_informacion.setProperty("showDropIndicator", False)
        self.tbl_informacion.setDragEnabled(False)
        self.tbl_informacion.setAlternatingRowColors(False)
        self.tbl_informacion.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tbl_informacion.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_informacion.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_informacion.setGridStyle(QtCore.Qt.DotLine)
        self.tbl_informacion.setWordWrap(True)
        self.tbl_informacion.setCornerButtonEnabled(False)
        self.tbl_informacion.setObjectName("tbl_informacion")
        self.tbl_informacion.setColumnCount(6)
        self.tbl_informacion.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_informacion.setHorizontalHeaderItem(5, item)
        self.tbl_informacion.horizontalHeader().setVisible(False)
        self.tbl_informacion.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_informacion.horizontalHeader().setDefaultSectionSize(130)
        self.tbl_informacion.horizontalHeader().setHighlightSections(True)
        self.tbl_informacion.horizontalHeader().setStretchLastSection(True)
        self.tbl_informacion.verticalHeader().setVisible(False)
        self.tbl_informacion.verticalHeader().setCascadingSectionResizes(True)
        self.tbl_informacion.verticalHeader().setDefaultSectionSize(35)
        self.tbl_informacion.verticalHeader().setHighlightSections(True)
        self.tbl_informacion.verticalHeader().setSortIndicatorShown(False)
        self.tbl_informacion.verticalHeader().setStretchLastSection(True)
        self.gridLayout_8.addWidget(self.tbl_informacion, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generador de dietas"))
        self.input_box.setTitle(_translate("MainWindow", "Resultados"))
        self.tbl_resultados.setSortingEnabled(False)
        item = self.tbl_resultados.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Alimento"))
        item = self.tbl_resultados.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ración media Kcal/día"))
        item = self.tbl_resultados.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vitamina A g/día"))
        item = self.tbl_resultados.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fibra g/día"))
        item = self.tbl_resultados.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Calcio g/día"))
        item = self.tbl_resultados.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Hierro g/día"))
        self.control_box.setTitle(_translate("MainWindow", "Controles"))
        self.inp_hierro.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.inp_fibra.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.rb_ning.setText(_translate("MainWindow", "Ninguna"))
        self.label_9.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Especifique el número de épocas máximas.</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Fibra (g)"))
        self.cbx_sexo.setItemText(0, _translate("MainWindow", "Hombre"))
        self.cbx_sexo.setItemText(1, _translate("MainWindow", "Mujer"))
        self.rb_emb.setText(_translate("MainWindow", "Embarazada"))
        self.label_11.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Especifique el número de épocas máximas.</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Hierro (g)"))
        self.rb_lac.setText(_translate("MainWindow", "Lactancia"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Sexo"))
        self.inp_calcio.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "KiloCalorias (KCal)"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Especifique el número de épocas máximas.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Vitamina A (g)"))
        self.inp_kcal.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Edad"))
        self.label_10.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Especifique el número de épocas máximas.</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Calcio (g)"))
        self.btn_train.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_train.setText(_translate("MainWindow", "Crear dieta"))
        self.inp_edad.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.inp_vit_a.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dieta"))
        self.groupBox.setTitle(_translate("MainWindow", "Configuración"))
        self.label_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Generaciones"))
        self.label_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Individuos"))
        self.label_12.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Probabilidad de mutación"))
        self.inp_individuos.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.inp_p_mutacion.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.inp_generaciones.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Información algoritmo"))
        self.tbl_alimentos.setSortingEnabled(False)
        item = self.tbl_alimentos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Alimentos"))
        item = self.tbl_alimentos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ración media Kcal"))
        item = self.tbl_alimentos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vitamina A gramos"))
        item = self.tbl_alimentos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fibra gramos"))
        item = self.tbl_alimentos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Calcio gramos"))
        item = self.tbl_alimentos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Hierro gramos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Alimentos"))
        self.tbl_informacion.setSortingEnabled(False)
        item = self.tbl_informacion.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lactantes menores"))
        item = self.tbl_informacion.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lactantes mayores"))
        item = self.tbl_informacion.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Niños pequeños"))
        item = self.tbl_informacion.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Niños medianos"))
        item = self.tbl_informacion.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Niños grandes"))
        item = self.tbl_informacion.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Adultos A"))
        item = self.tbl_informacion.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Adultos B"))
        item = self.tbl_informacion.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Adultos C"))
        item = self.tbl_informacion.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Adultos D"))
        item = self.tbl_informacion.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Adultos E"))
        item = self.tbl_informacion.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Mujeres A"))
        item = self.tbl_informacion.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Mujeres B"))
        item = self.tbl_informacion.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Mujeres C"))
        item = self.tbl_informacion.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Mujeres D"))
        item = self.tbl_informacion.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "Mujeres E"))
        item = self.tbl_informacion.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "Embarazo"))
        item = self.tbl_informacion.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "Lactancia"))
        item = self.tbl_informacion.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Edad"))
        item = self.tbl_informacion.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ración media Kcal/día"))
        item = self.tbl_informacion.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vitamina A g/día"))
        item = self.tbl_informacion.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fibra g/día"))
        item = self.tbl_informacion.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Calcio g/día"))
        item = self.tbl_informacion.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Hierro g/día"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Información nutricional recomendada"))

from UI.external_widgets.error_graph import Error_Graph
from UI.resources import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

