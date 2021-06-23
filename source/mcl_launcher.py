#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from .message_button import MessageCtrlLabel, MessageLabels
from .software_frame import PicturePrev

from .gui_import import *

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


class Widget(QWidget):
    softwareClicked = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(6, 6, 6, 6)
        self.main_layout.setSpacing(6)

        self.resize(960, 540)

        self.font = QFont()
        self.font.setFamily('Monospaced')
        self.font.setPixelSize(20)

        self.palette = QPalette()

        self.title_ui()
        self.main_ui()
        self.init_ui()

        self._connect_()

    def init_ui(self):
        self.set_name('{0} {1}'.format(conf.get_name(), conf.get_version()))
        self.set_log(icon_path('window_icon.png'))

    def title_ui(self):
        self.title_widget = QWidget(self)
        self.main_layout.addWidget(self.title_widget)
        self.title_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

        lay = QHBoxLayout(self.title_widget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        self.log_label = QLabel(self.title_widget)
        self.log_label.setFixedSize(20, 20)
        self.log_label.setScaledContents(True)
        lay.addWidget(self.log_label)

        self.name_label = QLabel(self.title_widget)
        self.name_label.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.name_label.setFont(self.font)
        self.name_label.setStyleSheet('QLabel{color : red;}')
        self.name_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        lay.addWidget(self.name_label)

        spacer_item = QSpacerItem(
            456, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        lay.addItem(spacer_item)

        line = QFrame(self)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        brush = QBrush(QColor(40, 40, 40))
        brush.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        line.setPalette(self.palette)
        self.main_layout.addWidget(line)

    def main_ui(self):
        self.message_widget = QWidget(self)
        self.message_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.message_widget)

        lay = QHBoxLayout(self.message_widget)
        lay.setContentsMargins(0, 0, 0, 0)

        # author group ……~……~……~……~……~……~……~……~……
        self.message_frame = QFrame(self.message_widget)
        self.message_frame.setSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Expanding)
        lay.addWidget(self.message_frame)
        self._init_message_()

        line = QFrame(self.message_widget)
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        lay.addWidget(line)

        self.soft_frame = PicturePrev(self.message_widget)
        lay.addWidget(self.soft_frame)

    def _init_message_(self):
        lay_message = QVBoxLayout(self.message_frame)
        lay_message.setContentsMargins(0, 0, 0, 0)

        spacer_item = QSpacerItem(
            0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding)
        lay_message.addItem(spacer_item)

        # author
        self.user_ctrl_label = MessageCtrlLabel(self.message_frame)
        self.user_label = MessageLabels(self)
        self.user_ctrl_label.set_ctrl_label(self.user_label)
        self.user_ctrl_label.set_key('qss_user', '用户')
        self.user_label.set_key('qss_user_widget', 'ChenLiang.Miao')
        lay_message.addWidget(self.user_ctrl_label)
        # group
        self.group_ctrl_label = MessageCtrlLabel(self.message_frame)
        self.group_label = MessageLabels(self)
        self.group_ctrl_label.set_ctrl_label(self.group_label)
        self.group_ctrl_label.set_key('qss_group', '组别')
        self.group_label.set_key('qss_group_widget', 'ChenLiang.Miao')
        lay_message.addWidget(self.group_ctrl_label)
        # system
        self.system_ctrl_label = MessageCtrlLabel(self.message_frame)
        self.system_label = MessageLabels(self)
        self.system_ctrl_label.set_ctrl_label(self.system_label)
        self.system_ctrl_label.set_key('qss_system', '系统')
        self.system_label.set_key('qss_system_widget', 'ChenLiang.Miao')
        lay_message.addWidget(self.system_ctrl_label)
        # IP
        self.ip_ctrl_label = MessageCtrlLabel(self.message_frame)
        self.ip_label = MessageLabels(self)
        self.ip_ctrl_label.set_ctrl_label(self.ip_label)
        self.ip_ctrl_label.set_key('qss_ip', '地址')
        self.ip_label.set_key('qss_ip_widget', 'ChenLiang.Miao')
        lay_message.addWidget(self.ip_ctrl_label)
        # host
        self.host_ctrl_label = MessageCtrlLabel(self.message_frame)
        self.host_label = MessageLabels(self)
        self.host_ctrl_label.set_ctrl_label(self.host_label)
        self.host_ctrl_label.set_key('qss_host', '主机')
        self.host_label.set_key('qss_host_widget', 'ChenLiang.Miao')
        lay_message.addWidget(self.host_ctrl_label)

        spacer_item = QSpacerItem(
            0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding)
        lay_message.addItem(spacer_item)

    def set_log(self, inPath):
        self.log_label.setPixmap(QPixmap(inPath))

    def set_name(self, name):
        self.name_label.setText(name)

    def set_user(self, user):
        self.user_label.setText(user)

    def set_group(self, grp):
        self.group_label.setText(grp)

    def set_system(self, sysName):
        self.system_label.setText(sysName)

    def set_ip(self, ip):
        self.ip_label.setText(ip)

    def set_host(self, host):
        self.host_label.setText(host)

    def init_project(self, pro_dict):
        self.soft_frame.PROJECT = pro_dict

    def get_project(self):
        return self.soft_frame.get_project()

    def set_project(self, project_name):
        self.soft_frame.set_project(project_name)

    def init_pro_intro(self, intro_dict):
        self.soft_frame.INTRO = intro_dict

    @pyqtSlot(str)
    def start_software(self, software):
        self.softwareClicked.emit(software)

    def _connect_(self):
        self.soft_frame.softwareClicked[str].connect(self.start_software)
