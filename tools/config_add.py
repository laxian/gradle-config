#! /usr/bin/python
# encoding=utf-8

import os

import utils
from constant import apply_from_config
from constant import project_root


def apply():
    if utils.is_already_added():
        return

    project_gradle = open(project_root + os.sep + "build.gradle", 'a')
    project_gradle.write(apply_from_config)
    project_gradle.close()

