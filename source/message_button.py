#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from .gui_import import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class MessageCtrlLabel(QLabel):
    _stopTime = 600.00

    @property
    def StopTime(self):
        return self._stopTime

    @StopTime.setter
    def StopTime(self, stopTime):
        self._stopTime = stopTime

    def __init__(self, *args):
        super(MessageCtrlLabel, self).__init__(*args)
        self.message_widget = None
        self.font = QFont()
        self.font.setFamily('Monospaced')
        self.font.setPixelSize(20)
        self.setFont(self.font)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(60, 60)

    def set_key(self, key, txt):
        qss = conf.get('configuration', key)
        self.setStyleSheet(qss)
        self.setText(txt)

    def set_ctrl_label(self, widget):
        self.message_widget = widget
        self.message_widget.hide()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.set_ctrl_hide)

    def set_ctrl_hide(self):
        self.message_widget.hide()
        self.timer.stop()

    def set_ctrl_show(self):
        self.timer.stop()
        ctrl_pos = self.pos() + QPoint(75, 55)  # + self.parent().pos()
        self.message_widget.move(ctrl_pos)
        self.message_widget.show()

    def leaveEvent(self, *args, **kwargs):
        if not self.message_widget:
            return
        self.timer.start(self._stopTime)

    def enterEvent(self, *args, **kwargs):
        if not self.message_widget:
            return
        self.set_ctrl_show()


class MessageLabels(QLabel):
    def __init__(self, *args):
        super(MessageLabels, self).__init__(*args)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.raise_()
        self.font = QFont()
        self.font.setFamily('Monospaced')
        self.font.setPixelSize(20)
        self.setFont(self.font)
        self.setFixedSize(240, 30)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

    def set_key(self, key, txt):
        qss = configuration.CONF().get('configuration', key)
        self.setStyleSheet(qss)
        self.setText(txt)
