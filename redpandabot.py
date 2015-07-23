""""
Red Panda Scanning Bot

A Project by /u/NEWSBOT3 to find mentions of Red Pandas on reddit easily
see https://github.com/jameswells1982/redpandabot

"""

import time
import praw
import ConfigParser
import logging
import pprint

logging.basicConfig(filename='/var/log/redpandabot.log', format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
Config = ConfigParser.ConfigParser()
Config.read("./config.ini")
DBHost = Config.get('DB','Host')
DBUsername = Config.get('DB','Username')
DBPassword = Config.get('DB', 'Password')
IncludedSubreddits = Config.get('Reddit','Included')
ExcludedSubreddits = Config.get('Reddit','Excluded')

print "Hello %s you are connecting to %s with password %s" % (DBUsername, DBHost,DBPassword)

logging.debug('Hello %s you are connecting to %s with password %s', DBUsername, DBHost, DBPassword)
logging.debug('Including %s Excluding %s', IncludedSubreddits, ExcludedSubreddits)


Scan = praw.Reddit('RedPandaBot scanning for Red Panda cuteness. https://github.com/jameswells1982/redpandabot/ ')


# Suggested workflow
# This bot only scans and adds NEW data to the DB. Storing all reddit data would be silly. Therefore we should only store a comment id, link in a each subreddit table
# So first check if a table exists, if not create from template
# then if it does exist
# There should be able a table for thread titles and comments
# It also neeeds to scan submission titles and texts

print "Checking %s for comments" % (IncludedSubreddits)
Scan.login('RedPandaBot','DuckCult3%')
temp = Scan.get_subreddit('aww')
temp_commments = temp.get_comments()
#flat_comments = praw.helpers.flatten_tree(temp_commments)
#print "T"
flat_comments = praw.helpers.flatten_tree(temp_comments)
print flat_comments


