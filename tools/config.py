#! /usr/bin/python
#encoding=utf-8

import config_add
import config_commit
import config_create

config_create.create_config()
config_add.apply()
config_commit.format()
