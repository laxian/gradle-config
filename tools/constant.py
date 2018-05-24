#! /usr/bin/python
# encoding=utf-8

import sys

project_root = sys.path[0]

if len(sys.argv) > 1:
    project_root = sys.argv[1]
else:
    print '----------------------'
    print '请指定Android project root path'
    print '----------------------'
    exit(-1)

config_gradle = r"config.gradle"
build_gradle = r"build.gradle"
android_rex = r"\s*android\s*=\s*\[.*?\]"

dependency_pattern = r"\s*((?:(?:\w+C)|c)ompile)" \
                     r" *(?P<right>\(?'(?P<compony>(?:\w+\.)*[\w-]+):" \
                     r"(?P<lib>[\w-]+):" \
                     r"(?P<ver>(?:\w+\.)*[\w@+]+)'\)?\s*)\n"

android_pattern = r"\s*" \
                  r"(?P<key>compileSdkVersion|buildToolsVersion|applicationId|minSdkVersion|" \
                  r"targetSdkVersion|versionCode|versionName)\s+(?P<value>[0-9a-zA-Z\.\"']+)"

replace_android = r"rootProject.ext.android.%s"
replace_dependencies = r"rootProject.ext.dependencies['%s']"

apply_from_config = r"apply from: 'config.gradle'"

settings_gradle = r"settings.gradle"
module_pattern = r"':([\w-]+)'"


# used for migration from as2 -> As3
compile_rex=r'\s*\w*(?P<key>(?:C|\bc)ompile\b)\s*.*'
# compile_rex=r'\s*\w+(?P<key>(?:C|\bc)ompile)(?: |\().+'

r_map={
    'compile':'implementation',
    'Compile':'Implementation'
}
# end
