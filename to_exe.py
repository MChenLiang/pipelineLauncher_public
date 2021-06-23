#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
import sys
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import pathlib


py_folder = pathlib.Path(sys.executable).parent
nuitka = py_folder.joinpath("Scripts", "nuitka.bat")

source_folder = pathlib.Path.cwd()
follow_import = source_folder.joinpath("source")

exe_path = source_folder.joinpath("launcher.py")

icon_path = source_folder.joinpath("source", "icons", "Launcher_exe_icon.ico")

print(icon_path)

cmd = str(nuitka) + " "
cmd += "--standalone "
cmd += "--windows-disable-console "
cmd += "--mingw64 "
cmd += "--show-memory "
cmd += "--show-progress "
cmd += "--plugin-enable=qt-plugins "
cmd += "--follow-import-to=source "
cmd += "--windows-icon-from-ico={} ".format(icon_path)
cmd += "--output-dir=out "
cmd +=  "{exe}".format(exe=exe_path)

print(cmd)

os.system(cmd)
