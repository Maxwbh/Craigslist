# -*- encoding: utf-8 -*-

__author__ = 'Maxwell'

import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
config.add_section('DataBase')
config.set('DataBase', 'conn', 'mysql')
config.set('DataBase', 'user', 'root')
config.set('DataBase', 'pwd', 'a')
config.set('DataBase', 'iphost', '127.0.0.1')
config.set('DataBase', 'port', '3306')
config.set('DataBase', 'base', 'db_email')


# Writing our configuration file to 'emailtool.cfg'
with open('emailtool.cfg', 'wb') as configfile:
    config.write(configfile)
