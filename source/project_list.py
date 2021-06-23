#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from .gui_import import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class ProjectListView(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ProjectListView, self).__init__(parent)
        self.message_dict = dict()
        self.setFixedWidth(280)
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        layout.addWidget(self.scroll)
        temp_widget = QWidget(self.scroll)
        self.scroll.setWidget(temp_widget)
        v_lay = QVBoxLayout(temp_widget)
        v_lay.setSpacing(0)
        v_lay.setContentsMargins(0, 0, 0, 0)
        self.item_area = QWidget(temp_widget)
        self.item_area.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        v_lay.addWidget(self.item_area)
        self.item_lay = QVBoxLayout(self.item_area)
        self.item_lay.setSpacing(0)
        self.item_lay.setContentsMargins(0, 0, 0, 0)
        spacer_item = QSpacerItem(
            20, 173, QSizePolicy.Minimum, QSizePolicy.Expanding)
        v_lay.addItem(spacer_item)

    def clear(self):
        for each in self.message_dict.values():
            each.close()
        self.message_dict = dict()

    def remove_widget(self, project_name):
        wgt = self.message_dict.get(project_name, None)
        if wgt:
            self.message_dict.pop(project_name, wgt)
            wgt.close()

    def add_widget(self, projectName):
        wgt = self.message_dict.get(projectName, None)
        if wgt:
            return
        wgt = image_frame(self.item_area)
        wgt.PROJECT = projectName
        wgt.clicked.connect(self.on_image_frame_clicked)
        self.item_lay.addWidget(wgt)
        self.message_dict.setdefault(projectName, wgt)
        wgt.show()

    def add_widgets(self, *args):
        list(map(lambda proName: self.add_widget(proName), args))

    def on_image_frame_clicked(self, project_name):
        self.clicked.emit(project_name)
        self.hide()


class image_frame(QFrame):
    clicked = pyqtSignal(str)
    prevSelected = None
    clSelected = None
    selected = False
    is_height = 0
    _projectName = ''

    @property
    def PROJECT(self):
        return self._projectName

    @PROJECT.setter
    def PROJECT(self, name):
        self.set_title(name)
        self._projectName = name

    def __init__(self, *args):
        super(image_frame, self).__init__(*args)
        font = QFont()
        font.setFamily('Monospaced')
        font.setPixelSize(20)
        self.setFixedHeight(46)
        h_lay = QHBoxLayout(self)
        h_lay.setSpacing(0)
        h_lay.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self)
        self.label.setFixedSize(40, 40)
        self.label.setLineWidth(0)
        self.label.setScaledContents(True)
        h_lay.addWidget(self.label)
        self.line = QLabel(self)
        self.line.setStyleSheet('color: gray;')
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.line.setFont(font)
        h_lay.addWidget(self.line)

    def set_image(self, image):
        self.label.setPixmap(QPixmap(image))

    def set_title(self, title):
        self.line.setText(title)

    def set_selected(self, conf):
        if image_frame.prevSelected is not None:
            image_frame.prevSelected.selected = False
        self.selected = conf
        self.repaint()
        image_frame.prevSelected = self

    def set_select(self):
        if image_frame.clSelected == self:
            return
        if image_frame.clSelected is not None:
            image_frame.clSelected.is_height = False
        self.is_height = True
        self.repaint()
        image_frame.clSelected = self

    def mouseReleaseEvent(self, event):
        self.set_select()
        self.clicked.emit(self.PROJECT)

    def enterEvent(self, event):
        self.set_select()

    def paintEvent(self, event):
        if self.selected:
            if self.is_height:
                self.setStyleSheet(
                    "QFrame{background-color: rgb(0, 120, 215);}QLabel{border:0;}")
            else:
                self.setStyleSheet(
                    "QFrame{background-color: rgb(0, 120, 215);}QLabel{border:0;}")

        else:
            if self.is_height:
                self.setStyleSheet(
                    "QFrame{background-color: rgb(118,185,237); border:3px solid rgb(0, 120, 215);}"
                    "QLabel{border:0;}")

            else:
                self.setStyleSheet(
                    "QFrame{background-color: none;}QLabel{border:0;}")
