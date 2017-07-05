#! /usr/bin/python
# encoding=utf-8

import os
import sys

import utils

project_root = sys.path[0]
apply_from_config = "apply from: 'config.gradle'"


def apply():
    if utils.is_already_added():
        return

    project_gradle = open(project_root + os.sep + "build.gradle", 'a')
    project_gradle.write(apply_from_config)
    project_gradle.close()


