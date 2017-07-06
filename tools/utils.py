#! /usr/bin/python
# encoding=utf-8

import os
import os.path
import re

from constant import build_gradle
from constant import module_pattern
from constant import project_root
from constant import settings_gradle


def list_module():
    settings = open(project_root + os.sep + settings_gradle, 'r')
    for line in settings.readlines():
        print line
        p = re.compile(pattern=module_pattern)
        return p.findall(line)


def open_module(module_name, mode):
    module_path = project_root + os.sep + module_name + os.sep + build_gradle
    return open(module_path, mode)


def is_already_added():
    project_gradle = open(project_root + os.sep + "build.gradle", 'r')
    old_content = project_gradle.read()
    project_gradle.close()
    return old_content.find(r"'config.gradle'") != -1


def fill_space(raw, length=30):
    return length - len(raw)
