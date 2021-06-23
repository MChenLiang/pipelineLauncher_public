#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFrame,
    QLabel,
    QComboBox,
    QAction,
    QMenu,
    QTextEdit,
    QSystemTrayIcon,
    QSizePolicy,
    QSpacerItem,
    QGridLayout,
    QSlider,
    QSplashScreen,
    QCommandLinkButton,
    QStackedWidget,
    QTextBrowser,
    QTableWidget,
    QPushButton,
    QListView,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QDialog,
    QAbstractItemView,
    QStackedLayout)
from PyQt5.QtCore import Qt, QSize, QTimer, QPoint, QElapsedTimer, QCoreApplication
from PyQt5.QtGui import QPixmap, QMovie, QFont, QIcon, QBrush, QPalette, QCursor, QPainter, QResizeEvent, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot
try:
    from PyQt5 import sip
except BaseException:
    import sip
from . import script_tool
from . import configuration

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
script_path = script_tool.get_script_path()
conf = configuration.CONF()

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


def icon_path(icon):
    return str(script_path.joinpath("icons", icon))
