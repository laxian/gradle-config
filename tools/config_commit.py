#! /usr/bin/python
#encoding=utf-8

import re
import sys

import utils

project_root = sys.path[0]
settings_gradle = r"settings.gradle"
config_gradle = r"config.gradle"
build_gradle = "build.gradle"
android_rex = r"\s*android\s*=\s*\[.*?\]"
module_pattern = r"':(\w+-?\w+)'"
dependency_pattern = r"\s*(\w*compile) *\(?'((\w+\.)+\w+):([\w-]+):((\d+\.)+\d+)'\)?"
android_pattern = r"\s*(compileSdkVersion|buildToolsVersion|applicationId|minSdkVersion|targetSdkVersion|versionCode|versionName)\s*([0-9a-zA-Z\.\"]+)"
application_pattern = r"\s*apply\s+plugin:\s+'com.android.application'\s*"

replace_android = "rootProject.ext.android.%s"
replace_dependencies = "rootProject.ext.dependencies['%s']"

def do_format(module):
    module = utils.open_module(module, 'r+')
    lines = module.readlines()
    module.truncate()
    module.seek(0)
    for l in lines:
        dependency_p = re.compile(dependency_pattern)
        dm = dependency_p.match(l)
        if dm is None:
            android_p = re.compile(android_pattern)
            am = android_p.match(l)
            if am is None:
                module.write(l)
                continue
            else:
                # print am.group(0)
                # print am.group(1)
                # print am.group(2)
                # print am.groups()
                formated = am.group(0).replace(am.group(2), replace_android % am.group(1))+'\n'
                print formated
                module.write(formated)
        else:
            print dm.groups()
            formated = dm.group(1) + ' ' + replace_dependencies % dm.group(4)+'\n'
            print formated
            module.write(formated)
    module.close()


def format():
    modules = utils.listModule()
    for m in modules:
        do_format(m)

format()