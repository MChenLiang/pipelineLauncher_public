#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
import sys
import tempfile
import importlib
import subprocess
import pathlib
from . import configuration

# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
conf = configuration.CONF()
PROJECT_CONFIG_PATH = conf.get('configuration', 'projectConfigurationPath')


# --+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
def launcher_project_software(project, software):
    """
    """
    # -
    path = pathlib.Path(PROJECT_CONFIG_PATH).joinpath('%s.py' % project)
    spec2 = importlib.util.spec_from_file_location(
        "project_config_value", path)
    project_config_value = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(project_config_value)
    # -
    soft_upper = software.upper()
    software_bat = project_config_value.__dict__.get(
        '{0}_BAT_PATH'.format(soft_upper), dict())
    software_location = project_config_value.__dict__.get(
        '{0}_LOCATION'.format(software.upper()), '')

    tmp_file = str(
        pathlib.Path(
            tempfile.mktemp()).parent.joinpath('start.bat'))

    with open(tmp_file, 'w') as f:
        f.write('@echo off\r\n')
        if software_bat.__len__():
            for (k, v) in software_bat.items():
                if isinstance(v, list):
                    f.write('set {0}={1};%{0}%\r\n'.format(k, ';'.join(v)))
                elif isinstance(v, int) or isinstance(v, str):
                    f.write('set {0}={1}\r\n'.format(k, v))
        f.write(software_location + '\r\n')

    #
    proc = subprocess.Popen('explorer.exe "{0}"'.format(tmp_file), stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE)
    proc.communicate()
    del proc
