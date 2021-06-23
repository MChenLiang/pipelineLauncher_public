#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from .gui_import import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class CtrlLabel(QLabel):
    def __init__(self, *args):
        super(CtrlLabel, self).__init__()
        self.setMouseTracking(True)
        self.setScaledContents(True)
        if args:
            self.ID = args[0]
            self.setPixmap(QPixmap(args[1]))

    def mouseReleaseEvent(self, event):
        self.parent().btn_handle(self.ID)

    def enterEvent(self, event):
        self.parent().btn_enter(self.ID)

    def leaveEvent(self, event):
        self.parent().btn_leave(self.ID)

    def mousePressEvent(self, event):
        self.parent().btn_click(self.ID)
