#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'miaochenliang'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import os
import pathlib

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
command_tool = pathlib.Path("C:/Program Files/ImageMagick-7.0.6-Q16")
command_tool = command_tool.joinpath("magick.exe")

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


def FindExamAllFiles():
    current_folder = pathlib.Path.cwd().joinpath("source", "icons")
    yield from current_folder.glob("**/*.png")


if __name__ == '__main__':
    for f in FindExamAllFiles():
        command = '"{0}" {1} {2}'.format(command_tool, f, f)
        print(command)
        os.system(command)
