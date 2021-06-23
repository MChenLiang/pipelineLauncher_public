#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import sys
from . import scriptTool

dirname = str(scriptTool.get_script_path())
sys.path.insert(0, dirname)

os.environ['PATH'] += os.pathsep + dirname
