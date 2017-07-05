#! /usr/bin/python
#encoding=utf-8

import os
import sys

import utils

project_root = sys.path[0]
settings_gradle = r"settings.gradle"
config_gradle = r"config.gradle"
build_gradle = "build.gradle"
android_rex = r"\s*android\s*=\s*\[.*?\]"
module_pattern = r"':(\w+-?\w+)'"
dependency_pattern = r"\s*(\w*compile) *\(?'((\w+\.)+\w+):([\w-]+):((\d+\.)+\d+)'\)?"
android_pattern = r"(compileSdkVersion|buildToolsVersion|applicationId|minSdkVersion|targetSdkVersion|versionCode|versionName)\s*([0-9a-zA-Z\.\"]+)"
application_pattern = r"\s*apply\s+plugin:\s+'com.android.application'\s*"

apply_from_config = "apply from: 'config.gradle'"



def apply():
    if utils.is_already_added():
        return

    project_gradle = open(project_root + os.sep + "build.gradle", 'a')
    project_gradle.write(apply_from_config)
    project_gradle.close()

apply()