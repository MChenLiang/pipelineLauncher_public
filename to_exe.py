#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
import sys

__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import pathlib
import pyfastcopy

import shutil


def copy_file(path_read, path_write):
    names = os.listdir(path_read)
    for name in names:
        path_read_new = path_read + "\\" + name
        path_write_new = path_write + "\\" + name
        if os.path.isdir(path_read_new):
            if not os.path.exists(path_write_new):
                os.mkdir(path_write_new)
            copy_file(path_read_new, path_write_new)
        else:
            shutil.copyfile(path_read_new, path_write_new)


if __name__ == '__main__':

    py_folder = pathlib.Path(sys.executable).parent
    nuitka = py_folder.joinpath("Scripts", "nuitka.bat")

    source_folder = pathlib.Path.cwd()
    follow_import = source_folder.joinpath("source")

    # 打包
    exe_path = source_folder.joinpath("launcher.py")

    cmd = ""
    cmd += "\n"
    cmd += str(nuitka) + " "
    cmd += "--standalone "
    cmd += "--windows-disable-console "
    cmd += "--mingw64 "
    cmd += "--show-memory "
    cmd += "--show-progress "
    cmd += "--plugin-enable=qt-plugins "
    cmd += "--follow-import-to=source "
    cmd += "--windows-icon-from-ico={} ".format(
        "source/icons/Launcher_exe_icon.ico")
    cmd += "--output-dir=out "
    cmd += "{exe}".format(exe=exe_path)

    os.system(cmd)

    # 拷贝图片
    icon_folder = source_folder.joinpath("source", "icons")
    to_icon_folder = source_folder.joinpath("out", "launcher.dist", "source")

    copy_file(str(icon_folder), str(to_icon_folder))

    # 拷贝配置文件
    for each in follow_import.glob("**/*.ini"):
        shutil.copy(str(each), str(to_icon_folder))
