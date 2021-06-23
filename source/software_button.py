#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from .gui_import import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class SETATTR(QLabel):
    clicked = pyqtSignal(str)
    _soft_name_ = ""
    _in_image_path_ = ""
    _out_image_path_ = ""
    _id_ = ""

    def __init__(self, *args, **kwargs):
        super(SETATTR, self).__init__(*args, **kwargs)

    @property
    def SOFT_NAME(self):
        return self._soft_name_

    @SOFT_NAME.setter
    def SOFT_NAME(self, soft_name):
        self._soft_name_ = soft_name

    @property
    def IN_IMAGE(self):
        return self._in_image_path_

    @IN_IMAGE.setter
    def IN_IMAGE(self, image_path):
        self._in_image_path_ = str(image_path)

    @property
    def OUT_IMAGE(self):
        return self._out_image_path_

    @OUT_IMAGE.setter
    def OUT_IMAGE(self, out_image):
        self._out_image_path_ = str(out_image)

    @property
    def ID(self):
        return self._id_

    @ID.setter
    def ID(self, enter_id):
        self._id_ = enter_id


class SoftwareButton(SETATTR):
    def __init__(self, soft_name, image_folder, *args, **kwargs):
        super(SoftwareButton, self).__init__(*args, **kwargs)
        self.SOFT_NAME = soft_name

        self.image_path = icon_path(
            '{0}/{1}_logo.png'.format(image_folder, self.SOFT_NAME))
        self.setPixmap(QPixmap(self.image_path))

        self.setToolTip(self.SOFT_NAME)

        self.setObjectName(self.SOFT_NAME)
        self.setScaledContents(True)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.resize(QSize(60, 60))

    def mouseReleaseEvent(self, *args, **kwargs):
        self.setPixmap(QPixmap(self.OUT_IMAGE))
        self.clicked.emit(self.SOFT_NAME)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setPixmap(QPixmap(self.IN_IMAGE))

    def leaveEvent(self, *args, **kwargs):
        self.setPixmap(QPixmap(str(self.image_path)))

    def enterEvent(self, *args, **kwargs):
        self.setPixmap(QPixmap(self.OUT_IMAGE))
