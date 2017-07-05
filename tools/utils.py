#! /usr/bin/python
# encoding=utf-8

import os
import os.path
import re
import sys

project_root = sys.path[0]
settings_gradle = r"settings.gradle"
config_gradle = r"config.gradle"
build_gradle = "build.gradle"
android_rex = r"\s*android\s*=\s*\[.*?\]"
module_pattern = r"':(\w+-?\w+)'"
dependency_pattern = r"\s*(\w*compile) *\(?'((\w+\.)+\w+):([\w-]+):((\d+\.)+\d+)'\)?"
android_pattern = r"(compileSdkVersion|buildToolsVersion|applicationId|minSdkVersion|targetSdkVersion|versionCode|versionName)\s*([0-9a-zA-Z\.\"]+)"
application_pattern = r"\s*apply\s+plugin:\s+'com.android.application'\s*"

def listModule():
    settings = open(project_root + os.sep + settings_gradle, 'r')
    return parseModule(settings)


def parseModule(settings):
    if settings.closed:
        return []
    else:
        for line in settings.readlines():
            print line
            p = re.compile(pattern=module_pattern)
            # print p.findall(line)
            return p.findall(line)

def open_module(module_name, mode):
    module_path = sys.path[0] + os.sep + module_name + os.sep + build_gradle
    return open(module_path, mode)

def is_already_added():
    project_gradle = open(project_root + os.sep + "build.gradle", 'r')
    old_content = project_gradle.read()
    project_gradle.close()
    return old_content.find(r"'config.gradle'") != -1

def fill_space(raw, length=30):
    return length - len(raw)