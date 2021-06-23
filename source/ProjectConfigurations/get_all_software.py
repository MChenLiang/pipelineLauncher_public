#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import re
import platform

py_version = platform.python_version()[0]

if int(py_version) < 3:
    import _winreg as winreg
else:
    import winreg as winreg


def get_all_software():
    def order_dict(dict_list, num_key, display_name, display_icon):
        dict_list[num_key] = {
            'DisplayName': display_name,
            'DisplayIcon': display_icon}
        exe_icon = re.compile('.*exe')
        match = exe_icon.match(display_icon)
        if match:  # 匹配到exe， 可直接打开
            dict_list[num_key]['exe'] = match.group()
        else:  # 没有exe，Icon可为ico 文件
            dict_list[num_key]['icon'] = display_icon

    dict_list = {}
    sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
               ]

    for k in sub_key:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             k, 0, winreg.KEY_ALL_ACCESS)
        for i in range(0, winreg.QueryInfoKey(key)[0] - 1):
            try:
                key_name_list = winreg.EnumKey(key, i)
                each_key_path = k + '\\' + key_name_list
                each_key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    each_key_path,
                    0,
                    winreg.KEY_ALL_ACCESS)
                display_name, reg_sz = winreg.QueryValueEx(
                    each_key, "DisplayName")
                try:
                    install_location = winreg.QueryValueEx(
                        each_key, "InstallLocation")[0]
                except BaseException:
                    install_location = "undefined"
                try:
                    display_icon = winreg.QueryValueEx(
                        each_key, "DisplayIcon")[0]
                except BaseException:
                    display_icon = "undefined"

                if install_location == "undefined":
                    continue

                order_dict(dict_list, str(i), display_name, display_icon)
            except WindowsError:
                pass

    return dict_list


def search_exe_path(keyworld):
    software = get_all_software()
    for (i, exe_mess) in software.items():
        display_name = exe_mess["DisplayName"]
        exe_file = exe_mess["icon"] if not exe_mess.get(
            "exe") else exe_mess.get("exe")
        keyworld = re.compile(keyworld)
        match = keyworld.match(display_name)
        if match:
            return exe_file
