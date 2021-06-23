#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# import
# --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
# #
from .gui_import import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class SplashScreen(QSplashScreen):
    def __init__(self, animation, flag, widget):
        super(SplashScreen, self).__init__(QPixmap(), flag)
        self.movie = QMovie(animation)
        self.movie.setParent(self)
        self.movie.frameChanged.connect(self.on_next_frame)
        self.count = self.movie.frameCount()
        self.step = 0
        self.widget = widget

    def on_next_frame(self):
        if self.step < self.count:
            pixmap = self.movie.currentPixmap()
            self.setPixmap(pixmap)
            self.setMask(pixmap.mask())
            self.step += 1

        else:
            self.finish(self.widget)

    def showEvent(self, *args):
        self.movie.start()

    def finish(self, widget):
        self.movie.setParent(None)
        # sip.delete(self.movie)
        widget.showNormal()
        super(SplashScreen, self).finish(widget)
