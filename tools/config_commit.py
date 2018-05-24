#! /usr/bin/python
# encoding=utf-8

import re

import utils
from constant import android_pattern
from constant import dependency_pattern
from constant import replace_android
from constant import replace_dependencies


def do_format(module):
    module = utils.open_module(module, 'r+')
    lines = module.readlines()
    lib_names=[]
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
                formated = am.group(0).replace(am.group('value'), replace_android % am.group('key')) + '\n'
                print formated
                module.write(formated)
        else:
            print dm.groups()
            lib_name = dm.group('lib')
            if lib_name in lib_names:
                compony = dm.group('compony')
                rdot = compony.rfind('.')
                rdot = 0 if rdot == -1 else rdot + 1
                lib_name = compony[rdot:] + '.' + lib_name
                formated = dm.group(0).replace(dm.group('right'), replace_dependencies % lib_name)
            else:
                formated = dm.group(0).replace(dm.group('right'), replace_dependencies % lib_name)
            lib_names.append(lib_name)
            print formated
            module.write(formated)
    module.close()


def format():
    modules = utils.list_module()
    for m in modules:
        do_format(m)
