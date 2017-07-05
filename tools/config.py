#! /usr/bin/python
#encoding=utf-8

import config_add
import config_commit
import config_create

config_create.createConfig()
config_add.apply()
config_commit.format()
