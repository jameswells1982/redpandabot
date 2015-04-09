""""
Red Panda Scanning Bot

A Project by /u/NEWSBOT3 to find mentions of Red Pandas on reddit easily
see https://github.com/jameswells1982/redpandabot

"""

import time
import praw
import ConfigParser
import logging

logging.basicConfig(filename='/var/log/redpandabot.log', level=logging.DEBUG)
Config = ConfigParser.ConfigParser()
Config.read("./config.ini")
DBHost = Config.get('DB','Host')
DBUsername = Config.get('DB','Username')
DBPassword = Config.get('DB', 'Password')

print "Hello %s you are connecting to %s with password %s" % (DBUsername, DBHost,DBPassword)
logging.DEBUG('Hello %s you are connecting to %s with password %s', DBUsername, DBHost, DBPassword)
