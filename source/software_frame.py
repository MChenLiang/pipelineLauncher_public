#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import math
from collections import defaultdict

from .gui_import import *

from . import software_button
from . import project_list

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
connect_path = icon_path('connected.png')
disconnect_path = icon_path('disconnected.png')


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class ProjectLabel(QLabel):
    clicked = pyqtSignal()
    allPro = []

    def __init__(self, *args):
        super(ProjectLabel, self).__init__(*args)
        self.setAlignment(Qt.AlignCenter)
        conf.set_configuration()
        self.pro_label = conf.get('configuration', 'pro_label')
        self.pro_label_hover = conf.get('configuration', 'pro_label_hover')
        self.setStyleSheet(self.pro_label)

    def mousePressEvent(self, event):
        self.clicked.emit()
        self.setStyleSheet(self.pro_label)

    def mouseReleaseEvent(self, event):
        self.setStyleSheet(self.pro_label_hover)

    def enterEvent(self, event):
        self.setStyleSheet(self.pro_label_hover)

    def leaveEvent(self, event):
        self.setStyleSheet(self.pro_label)


class ScrollArea(QScrollArea):
    THUMB_WIDTH = 128
    THUMB_HEIGHT = 128
    THUMB_MIN = 64
    THUMB_MAX = 256

    def __init__(self, slider, *args):
        super(ScrollArea, self).__init__(*args)
        self.slider = slider
        self.setFrameShape(QFrame.NoFrame)
        self.setContentsMargins(0, 0, 0, 0)
        self.image_widget_list = dict()
        self.main_widget = QWidget(self)
        self.main_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWidget(self.main_widget)
        self.setWidgetResizable(True)
        self.asset_space = 20
        self.auto_space = 0

    def clear_all(self):
        widgets = self.main_widget.children()
        if widgets:
            for widget in widgets:
                widget.setParent(None)
        self.image_widget_list.clear()

    def add_widget(self, widget):
        widget.setParent(self.main_widget)
        self.image_widget_list.setdefault(widget.ID, widget)
        self.set_size()
        widget.show()

    def add_widgets(self, widgets):
        for widget in widgets:
            self.add_widget(widget)

    def layout(self):
        w = self.width() - 20
        widgets = self.main_widget.children()
        # Can do -1
        num_x = max(math.ceil(w / (self.THUMB_WIDTH + self.asset_space)) - 1, 1)
        num_y = math.ceil(len(widgets) / num_x)
        self.main_widget.resize(
            w, num_y * (self.THUMB_HEIGHT + self.asset_space) + 50)

        main_w = self.main_widget.width()
        # Can do -1
        num_x = max(
            math.ceil(main_w / (self.THUMB_WIDTH + self.asset_space)) - 1, 1)

        x = 0
        y = 0
        for i in range(len(widgets)):
            space_x = 0
            if self.auto_space:
                space_x = (main_w - 30 - self.asset_space * 2 - num_x *
                           (self.THUMB_WIDTH + self.asset_space)) / num_x
            widgets[i].move(self.asset_space *
                            1 +
                            x *
                            (self.THUMB_WIDTH +
                             self.asset_space +
                             space_x), self.asset_space *
                            1 +
                            y *
                            (self.THUMB_HEIGHT +
                             self.asset_space))
            x += 1
            if x >= num_x:
                x = 0
                y += 1

    def change_item_size(self, mount):
        widgets = self.main_widget.children()
        self.THUMB_WIDTH += mount
        if self.THUMB_WIDTH > self.max_height:
            self.THUMB_WIDTH = self.max_height
        elif self.THUMB_WIDTH < self.min_width:
            self.THUMB_WIDTH = self.min_width

        self.THUMB_HEIGHT += mount
        if self.THUMB_HEIGHT > self.max_height:
            self.THUMB_HEIGHT = self.max_height
        elif self.THUMB_HEIGHT < self.min_width:
            self.THUMB_HEIGHT = self.min_width

        for a in widgets:
            a.resize(self.THUMB_WIDTH, self.THUMB_HEIGHT)

        self.layout()

    def set_size(self):
        size = self.slider.value()
        widgets = self.main_widget.children()

        self.THUMB_WIDTH = size
        self.THUMB_HEIGHT = size

        for a in widgets:
            a.resize(size, size)

        self.layout()

    def set_selected(self, enter_id):
        self.ImageWidgetList[str(enter_id)].set_selected()

    def resizeEvent(self, event):
        self.set_size()


class PicturePrev(QFrame):
    _proDict = defaultdict()
    _introDict = defaultdict()
    softwareClicked = pyqtSignal(str)

    @property
    def PROJECT(self):
        return self._proDict

    @PROJECT.setter
    def PROJECT(self, val):
        self._proDict = val
        self.set_project(list(val.keys())[0])
        self.set_pro_widget()

    @property
    def INTRO(self):
        return self._introDict

    @INTRO.setter
    def INTRO(self, val):
        self._introDict = val

    def __init__(self, *args):
        super(PicturePrev, self).__init__(*args)
        self.palette = QPalette()
        brush = QBrush(QColor(40, 40, 40))
        brush.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.setPalette(self.palette)

        self.font = QFont()

        self.font.setFamily('Monospaced')
        self.font.setPixelSize(20)

        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        pro_widget = QWidget(self)
        pro_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(pro_widget)
        temp_lay = QHBoxLayout(pro_widget)
        temp_lay.setContentsMargins(10, 10, 10, 10)

        label = QLabel('Project : ', pro_widget)
        label.setFont(self.font)
        label.setStyleSheet('color: #ff7950')
        self.pro_label = ProjectLabel(pro_widget)
        self.pro_label.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        self.pro_label.setFont(self.font)
        temp_lay.addWidget(label)
        temp_lay.addWidget(self.pro_label)

        self.slider = QSlider(pro_widget)
        self.slider.hide()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(60)
        self.slider.setMaximum(200)
        self.slider.setValue(64)
        self.slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        conf.set_configuration()
        H_slider = conf.get('configuration', 'H_slider')
        self.slider.setStyleSheet(H_slider)
        temp_lay.addWidget(self.slider)

        spacerItem = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Preferred)
        temp_lay.addItem(spacerItem)

        line = QFrame(self)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.softMessage = QWidget()
        self.softMessage.setSizePolicy(
            QSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Expanding))

        self.lay = QHBoxLayout(self.softMessage)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.setSpacing(9)
        layout.addWidget(self.softMessage)

        self.software_scroll = ScrollArea(self.slider, self.softMessage)
        self.project_list_view = project_list.ProjectListView(self.softMessage)
        self.project_list_view.setHidden(True)

        self.lay.addWidget(self.software_scroll)
        self.lay.addWidget(self.project_list_view)

        self.asset_space = 20
        self.auto_space = 0

        self.setWindowOpacity(0.0)

        self._connect_()

    def get_project(self):
        return str(self.pro_label.text())

    def set_project(self, project_name):
        self.pro_label.setText(project_name)
        self.set_software_widget()

    def _connect_(self):
        self.project_list_view.clicked.connect(self.set_project)
        self.slider.valueChanged.connect(self.on_slider_connect)
        self.pro_label.clicked.connect(self.on_pro_label_connect)

    def on_slider_connect(self):
        self.software_scroll.set_size()

    def on_pro_label_connect(self):
        self.project_list_view.setHidden(not self.project_list_view.isHidden())

    def set_pro_widget(self):
        self.project_list_view.clear()
        self.project_list_view.add_widgets(*sorted(self.PROJECT.keys()))

    def set_software_widget(self):
        pro = self.get_project()
        soft_ware = self.PROJECT.get(pro)
        self.software_scroll.clear_all()
        for each in soft_ware:
            widget = software_button.SoftwareButton(each, 'soft')
            widget.OUT_IMAGE = icon_path('disconnected.png')
            widget.IN_IMAGE = icon_path('connected.png')
            widget.clicked[str].connect(self.on_software_connect)
            self.software_scroll.add_widget(widget)

    @pyqtSlot(str)
    def on_software_connect(self, software):
        self.softwareClicked.emit(software)
