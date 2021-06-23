#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import pathlib
import configparser
from . import script_tool

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
script_path = script_tool.get_script_path()

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


def encode(s):
    return " ".join([bin(ord(c)).replace("0b", "") for c in s])


def decode(s):
    return "".join([chr(i) for i in [int(b, 2) for b in s.split(" ")]])


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class CONF(object):
    _in_path = ""

    def set_path(self, in_path):
        self._in_path = in_path

    def set_configuration(self):
        # 设置当前配置表路径
        self._in_path = script_path.joinpath("configuration.ini")

    def set_project(self):
        cf = CONF()
        # 得到配置表路径中的软件软件配置表
        project_folder = cf.get("configuration", "projectConfigurationPath")
        # 设置路径
        path = pathlib.Path(project_folder)
        pro_path = path.joinpath("projectConfiguration.ini")
        if pro_path.exists():
            self._in_path = pro_path
        else:
            self._in_path = script_path.joinpath(
                "projectConfigurations", "projectConfiguration.ini")

    def set_software(self):
        self._in_path = script_path.joinpath("software_message.ini")

    def __init__(self):
        self.set_configuration()
        self.cf = None

    def get(self, field, key):
        try:
            self._read()
            result = self.cf.get(field, key)
        except Exception as e:
            result = ""

        return result

    def set(self, field, key, val):
        self._read()
        if self.find(field, key):
            self.cf.remove_option(field, key)

        self.cf[field][key] = val
        self.write()

    def has_op(self, section):
        self._read()
        return self.cf.has_section(section)

    def find(self, field, key):
        self._read()
        return self.cf.has_option(field, key)

    def write(self):
        with open(self._in_path, "w") as f:
            self.cf.write(f)

    def _read(self):
        self.cf = None
        del self.cf
        self.cf = configparser.ConfigParser()
        self.cf.read(str(self._in_path))

    @classmethod
    def get_name(cls):
        return cls().get("configuration", "name")

    @classmethod
    def get_version(cls):
        return cls().get("configuration", "version")

    def __getAuthor__(self):
        return self.get(
            "@Copyright",
            "1011111 1011111 1100001 1110101 1110100 1101000 1101111 1110010 1011111 1011111")

    def __getEmail__(self):
        return self.get(
            "@Copyright",
            "1011111 1011111 1000101 1101101 1100001 1101001 1101100 1011111 1011111")
