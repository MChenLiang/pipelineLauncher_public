#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

import os

from source import script_tool
folder = script_tool.get_script_path()
for each in folder.glob("**\\*.py"):
    print(each)
    os.system(
        r"C:\ProgramData\Anaconda3\envs\py37\Scripts\autopep8.exe --in-place --aggressive --aggressive %s" %
        each)
