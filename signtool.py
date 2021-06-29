#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import pathlib
import getpass
current_path = pathlib.Path.cwd()

cmd = "cd %s/signature" % current_path
cmd += "\n%s" % current_path.drive
cmd += "\nmakecert.exe -sv mykey.pvk -n \"CN=%sL\" mycert.cer" % getpass.getuser()
cmd += "\ncert2spc.exe mycert.cer mycert.spc"
cmd += "\npvk2pfx -pvk mykey.pvk -spc mycert.spc -pfx mycert.pfx"
cmd += "\nsignTool sign /v /f mycert.pfx /tr http://timestamp.digicert.com Z:/MCCCCL/launcher/launcher.exe"

os.system(cmd)
