#! /usr/bin/python
# encoding=utf-8

import os
import os.path
import re

import utils
from constant import android_pattern
from constant import android_rex
from constant import build_gradle
from constant import config_gradle
from constant import dependency_pattern
from constant import project_root


def read_file(path):
    dependency_map = {}
    android_map = {}
    is_application = False
    file = open(path, 'r')

    for l in file.readlines():
        if l.find("//") != -1 or l.find("fileTree") != -1 or l.find("files(") != -1 or l.find(
                "project(") != -1 or l.find("rootProject") != -1:
            continue
        if l.find("com.android.application") != -1:
            is_application = True

        if l.find(r"compile ") != -1 or l.find(r"compile(") != -1 or l.find(
                r"Compile ") != -1 or l.find(r"Compile(") != -1:
            p = re.compile(dependency_pattern)
            m = p.match(l)
            if m is None:
                continue
            print '\n-----------'
            print m.groups()
            formated = m.group('compony') + ':' + \
                m.group('lib') + ':' + m.group('ver')
            print formated
            print '-----------\n'
            if dependency_map.get(m.group('lib')) is None:
                dependency_map[m.group('lib')] = formated
            else:
                compony = m.group('compony')
                rdot = compony.rfind('.')
                rdot = 0 if rdot == -1 else rdot+1
                dependency_map[compony[rdot:] + '.' + m.group('lib')] = formated
        else:
            if not is_application:
                continue
            else:
                m = re.search(android_pattern, l)
                if m is None:
                    continue
                else:
                    print m
                    print m.groups()
                    print m.group(0)
                    android_map[m.group('key')] = m.group('value')

    file.close()
    return dependency_map, android_map


def readAndroidConfig():
    android_config = ""
    config = open(project_root + os.sep + config_gradle, 'r')
    config_content = config.read()
    p = re.compile(android_rex, re.S)
    m = p.search(config_content)
    if m is None:
        android_config = "android=[]"
    else:
        android_config = m.group(0)
    config.close()
    return android_config


def create_config_map():
    dependency_map, android_map = travel_module(utils.list_module())
    dependency_config = "\tdependencies = [\n"

    kvlist = [(k, dependency_map[k]) for k in dependency_map.keys()]
    kvlist = sorted(kvlist, cmp=lambda x,y: cmp(len(x[1]), len(y[1])))
    for k, v in kvlist:
        print "'%s'%s:\t'%s'," % (k, ' ' * utils.fill_space(k), v)
        dependency_config += "            '%s'%s:\t'%s',\n" % (
            k, ' ' * utils.fill_space(k), v)
    dependency_config += "\t]\n"

    android_config = "\tandroid = [\n"
    amlist = [(k, android_map[k]) for k in android_map.keys()]
    amlist = sorted(amlist, cmp=lambda x,y:cmp(x[0],y[0]))
    for k, v in amlist:
        android_config += "            %s%s:\t%s,\n" % (
            k, ' ' * utils.fill_space(k, 28), v)
    android_config += "\t]\n"

    return dependency_config, android_config


def create_config():
    '''
    打开（创建）config.gradle
    ext{
        android=[]
        dependencies=[]
    }
    :return:
    '''
    config = open(project_root + os.sep + config_gradle, 'w+')
    dependencies_config, android_config = create_config_map()
    config.write("// auto generated by zwx\n")
    config.write("ext {\n")
    config.write(android_config)
    config.write("\n")
    config.write(dependencies_config)
    config.write("}")
    config.close()


def travel_module(modules):
    dependency_map = {}
    android_map = {}
    for d in modules:
        print "module %s----> " % d
        d_map, a_map = read_file(
            project_root + os.sep + d + os.sep + build_gradle)
        dependency_map.update(d_map)
        android_map.update(a_map)
    return dependency_map, android_map
