#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import time
import psutil
import pathlib
import sys

from source.gui_import import *
import source.script_tool as script_tool
import source.ctrl_label as ctrl_label
import source.configuration as configuration

import source.base_commands as base_commands
import source.startup_interface as startup_interface

import source.mcl_launcher as mcl_launcher

import source.start_software as start_software

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
global qt_app
qt_app: QApplication

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


class MainFunc(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainFunc, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAutoFillBackground(True)
        self.setMouseTracking(True)
        self.setStyleSheet("""QMainWindow{border: 1px solid gray;}""")

        self.main_widget = mcl_launcher.Widget(self)
        self.setFixedSize(960, 540)
        self.setCentralWidget(self.main_widget)
        self.main_widget.softwareClicked[str].connect(self.start_software)

        self._init_ui_()

        self.is_enter = False
        self.m_pressed = False
        self.pixmap = QPixmap()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start)
        self.duration = 800.0
        self.opacity = 0.3
        self.setWindowOpacity(0)

    def _init_ui_(self):
        self.init_message()
        self.init_pro_conf()
        self.add_tray()
        self.add_ctrl_bt()
        self.init_current_project()

    def init_current_project(self):
        conf.set_software()
        current_project = conf.get("configuration", "current_project")
        if current_project and current_project in self.project_list:
            self.main_widget.set_project(current_project)

    def init_message(self):
        account = base_commands.get_current_user_name()
        system = base_commands.get_system()
        ip = base_commands.get_ip4()
        computer = base_commands.get_computer()
        self.main_widget.set_user(account)
        self.main_widget.set_group("")
        self.main_widget.set_system(system)
        self.main_widget.set_ip(ip)
        self.main_widget.set_host(computer)

    def init_pro_conf(self):
        conf.set_project()
        self.project_list = eval(conf.get('configuration', 'projectList'))
        self._pro_dict = {
            pro: sorted(
                eval(
                    conf.get(
                        pro,
                        'softWare'))) for pro in self.project_list}
        self.main_widget.init_project(self._pro_dict)

    @pyqtSlot(str)
    def start_software(self, software):
        project = str(self.main_widget.get_project())
        if not project:
            return

        return start_software.launcher_project_software(project, software)

    # 添加系统托盘-+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
    def add_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icon_path('window_icon.png')))
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.tray_click)
        self.tray_menu()

    def tray_click(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.setWindowOpacity(self.opacity)
            self.activateWindow()
            self.showNormal()

        elif reason == QSystemTrayIcon.MiddleClick:
            self.tray_show_message()
        else:
            pass

    def tray_show_message(self):
        icon = QSystemTrayIcon.Information
        in_text = 'soft :{}\r\n'.format(conf.get_name())
        in_text += 'version : {}\r\n'.format(conf.get_version())
        in_text += 'author : {}\r\n'.format(
            configuration.decode(conf.__getAuthor__()))
        self.tray_icon.showMessage('introduce : ', in_text, icon)

    def tray_menu(self):

        img_main = QIcon(icon_path('window_icon.png'))
        img_min = QIcon(icon_path('min_in.png'))
        img_exit = QIcon(icon_path('del_in.png'))

        self.tray_icon.setToolTip(
            '{0} {1}'.format(
                conf.get_name(),
                conf.get_version()))

        self.action_restore = QAction(img_main, conf.get_name(), self)
        self.action_min = QAction(img_min, "Minimize", self)
        self.action_quit = QAction(img_exit, "Exit", self)

        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(self.action_restore)
        self.tray_icon_menu.addAction(self.action_min)
        self.tray_icon_menu.addSeparator()
        self.tray_icon_menu.addAction(self.action_quit)
        self.tray_icon.setContextMenu(self.tray_icon_menu)

        self.action_restore.triggered.connect(self.max_action)
        self.action_min.triggered.connect(self.min_action)
        self.action_quit.triggered.connect(self.exit_action)

        self.menu = QMenu()
        self.action = QAction("Exit")
        self.menu.addAction(self.action)

    def min_action(self):
        self.hide()

    def max_action(self):
        self.setWindowOpacity(self.opacity)
        self.showNormal()

    def exit_action(self):
        self.close()
        global qt_app
        qt_app.quit()

    # 自定义控制按钮+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
    def add_ctrl_bt(self):
        self.btn_min = ctrl_label.CtrlLabel(2, icon_path('min_out.png'))
        self.btn_min.setParent(self)
        self.btn_min.setGeometry(self.width() - 60, 5, 20, 20)
        self.btn_min.setToolTip('min')

        self.btn_close = ctrl_label.CtrlLabel(3, icon_path('del_out.png'))
        self.btn_close.setParent(self)
        self.btn_close.setGeometry(self.width() - 30, 5, 20, 20)
        self.btn_close.setToolTip('close')

    def btn_click(self, ID):
        if ID == 2:
            self.btn_min.setPixmap(QPixmap(icon_path("min_out.png")))
        elif ID == 3:
            self.btn_close.setPixmap(QPixmap(icon_path("del_out.png")))

    def btn_handle(self, ID):

        if ID == 2:
            self.min_action()

        elif ID == 3:
            self.exit_action()

    def btn_enter(self, ID):
        if ID == 2:
            self.btn_min.setPixmap(QPixmap(icon_path("min_in.png")))

        elif ID == 3:
            self.btn_close.setPixmap(QPixmap(icon_path("del_in.png")))

    def btn_leave(self, ID):
        if ID == 2:
            self.btn_min.setPixmap(QPixmap(icon_path("min_out.png")))
        elif ID == 3:
            self.btn_close.setPixmap(QPixmap(icon_path("del_out.png")))

    # 设置窗口可被拖动+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.c_pos = event.globalPos() - self.pos()
            self.m_pressed = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.m_pressed:
                self.move(event.globalPos() - self.c_pos)
                event.accept()

    def mouseReleaseEvent(self, event):
        self.m_pressed = False

    def hide(self):
        t = 0
        while t <= 20:
            newOpacity = self.windowOpacity() - 0.1  # 设置淡出
            if newOpacity < 0:
                break

            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.02)
        super(MainFunc, self).hide()

    def showNormal(self):
        super(MainFunc, self).showNormal()
        t = 0
        while t <= 20:
            newOpacity = self.windowOpacity() + 0.1  # 设置淡入
            if newOpacity > 1:
                break
            self.setWindowOpacity(newOpacity)
            t -= 1
            time.sleep(0.02)

    def close(self):
        conf.set_software()
        current_project = self.main_widget.get_project()
        conf.set("configuration", "current_project", current_project)

        t = 0
        while t <= 20:
            newOpacity = self.windowOpacity() - 0.05  # 设置淡出
            if newOpacity < 0:
                break

            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.02)

        super(MainFunc, self).close()
        sip.delete(self.tray_icon)
        sip.delete(self)
        sys.exit()

    def start(self):
        self.opacity += self.timer.interval() / self.duration
        self.setWindowOpacity(self.opacity)
        if self.opacity > 1:
            self.timer.stop()
        else:
            self.show()


if __name__ == '__main__':

    exe_name = pathlib.Path(script_tool.get_script_file()).stem
    base_commands.create_lnk_and_start(pathlib.Path.cwd().joinpath(exe_name))

    current_proc = psutil.Process()
    if current_proc.name() == 'python.exe':
        pass

    else:
        # if '192.168' in current_proc.exe():
        #     current_proc.kill()
        for proc in psutil.process_iter():
            if proc.name() != current_proc.name():
                continue
            if proc.pid != current_proc.pid:
                base_commands.delete_ui(
                    '{}.exe'.format(
                        str(exe_name)),
                    str(exe_name))

    global qt_app
    qt_app = QApplication(sys.argv)
    ui = MainFunc()
    anim_path = icon_path('waiting.gif')
    splash = startup_interface.SplashScreen(
        anim_path, Qt.WindowStaysOnTopHint, ui)
    splash.showMessage(
        'author : %s' %
        __author__,
        Qt.AlignLeft | Qt.AlignBottom,
        Qt.yellow)
    splash.show()
    sys.exit(qt_app.exec_())
