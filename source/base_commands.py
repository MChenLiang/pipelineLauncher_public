#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import sys
import getpass
import platform
import socket

import pathlib
import win32api
import win32con
import win32gui
from win32com.shell import shell

import pythoncom
import winreg

import psutil

import re

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
__all_ui__ = set()
__find_ui__ = str()

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


def get_py_version():
    # 当前py版本
    return sys.int_info[0]


def get_current_user_name():
    # 计算机当前用户
    return getpass.getuser()


def get_system():
    # 系统版本号
    uname = platform.uname()
    return uname[0] + uname[2] + ' ' + platform.architecture()[0]


def get_ip4():
    return socket.gethostbyname(socket.gethostname())


def get_computer():
    return platform.node()


def get_desktop():
    """
    获取桌面路径
    :return:
    """
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]


def create_lnk(in_path, lnk_path):
    """
    创建快捷方式
    :param in_path:
    :param lnk_path:
    :return:
    """
    in_path = in_path  # type: pathlib.Path
    lnk_path = lnk_path  # type: pathlib.Path
    _base = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink)

    _base.SetPath(str(in_path))
    folder = in_path.parent
    _base.SetWorkingDirectory(str(folder))

    flag = lnk_path.suffix
    if flag != '.lnk':
        lnk_path += '.lnk'

    _base.QueryInterface(pythoncom.IID_IPersistFile).Save(str(lnk_path), 0)
    return lnk_path


def create_lnk_and_start(exe_file):
    """
    创建快捷方式，并添加开始启动
    :param exe_file:
    :return:
    """
    desk_path = pathlib.Path(get_desktop())
    exe_path = pathlib.Path(exe_file)
    pattern = "**/*{}*".format(exe_path.stem)
    lnks = list(desk_path.glob(pattern))

    start_path = desk_path.joinpath("{}.lnk".format(exe_path.stem))
    if not lnks:
        start_path = create_lnk(exe_file, start_path)

    # 添加开机启动
    key_name = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    name = str(exe_path.stem)  # 要添加的项值名称
    try:
        key = win32api.RegOpenKey(
            win32con.HKEY_CURRENT_USER,
            key_name,
            0,
            win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, str(start_path))
        win32api.RegCloseKey(key)
    except Exception as e:
        pass


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def foo(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(
            hwnd) and win32gui.IsWindowVisible(hwnd):
        __all_ui__.add(hwnd)


def find_window(cla_name, win_t):
    win32gui.EnumWindows(foo, 0)
    for hwnd in __all_ui__:
        if cla_name == win32gui.GetClassName(
                hwnd) and win_t == win32gui.GetWindowText(hwnd).decode('GB2312'):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            break


def delete_ui(cla_name, win_t):
    find_window(cla_name, win_t)


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def get_all_process():
    return {each.name(): each.pid for each in psutil.process_iter()}


def exists_exe(proc, name):
    all_process = get_all_process()
    if proc not in all_process.keys():
        return 0
    #
    win = win32gui.FindWindow(None, name)
    if not win:
        return 0
    return 1


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def get_all_software():
    def order_dict(dict_list, num_key, display_name, display_icon):
        dict_list[num_key] = {
            'DisplayName': display_name,
            'DisplayIcon': display_icon}
        exeIcon = re.compile('.*exe')
        match = exeIcon.match(display_icon)
        if match:  # 匹配到exe， 可直接打开
            dict_list[num_key]['exe'] = match.group()
        else:  # 没有exe，Icon可为ico 文件
            dict_list[num_key]['icon'] = display_icon

    dict_list = {}
    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        0,
        winreg.KEY_ALL_ACCESS)
    for i in range(0, winreg.QueryInfoKey(key)[0] - 1):
        try:
            key_name_list = winreg.EnumKey(key, i)
            each_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" + \
                '\\' + key_name_list
            each_key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                each_key_path,
                0,
                winreg.KEY_ALL_ACCESS)
            display_name, reg_sz = winreg.QueryValueEx(each_key, "DisplayName")
            try:
                display_icon, reg_sz = winreg.QueryValueEx(
                    each_key, "DisplayIcon")
            except WindowsError:
                pass
            # 注册表中同时满足DisplayName 和 DisplayIcon
            if display_name and display_icon:
                order_dict(dict_list, str(i), display_name, display_icon)
        except WindowsError:
            pass

    return dict_list
