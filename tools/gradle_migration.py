#! /usr/bin/python
# encoding=utf-8

import re
import utils
from constant import r_map, compile_rex


def format_module(fmodule):
    global m
    p=re.compile(compile_rex)
    lines = fmodule.readlines()
    fmodule.truncate()
    fmodule.seek(0)
    for l in lines:
        if l.find("ompile"):
            m=p.match(l)
        if m is not None:
            fmodule.write(l.replace(m.group('key'), r_map[m.group('key')]))
            print l.replace(m.group('key'), r_map[m.group('key')])
        else:
            fmodule.write(l)


def travel_module(modules):
    for d in modules:
        format_module(utils.open_module(d, 'r+'))


travel_module(utils.list_module())