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
import ast

# to disable the https warning
import urllib3
urllib3.disable_warnings()

logging.basicConfig(filename='/var/log/redpandabot.log', format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
Config = ConfigParser.ConfigParser()
Config.read("./config.ini")
BotUser = Config.get('Bot','Username')
BotPassword = Config.get('Bot','Password')
DBHost = Config.get('DB','Host')
DBUsername = Config.get('DB','Username')
DBPassword = Config.get('DB', 'Password')
IncludedSubreddits = ast.literal_eval(Config.get('Reddit','Included'))
ExcludedSubreddits = Config.get('Reddit','Excluded')
Words = ast.literal_eval(Config.get('Reddit','Terms'))

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
Scan.login(BotUser, BotPassword)

for subreddit in IncludedSubreddits:
    data = Scan.get_subreddit(subreddit)
    print "trying %s for submissions" % subreddit
    if data:
        for submission in data.get_new(limit=100):
            subject = submission.title.lower()
            has_pandas = any(string in subject for string in Words)
            if has_pandas:
                print 'Thread found in %s' % subreddit
                print ' %s' % submission.title
                print ' %s' % submission.short_link
    # now get comments
    comments = Scan.get_subreddit(subreddit).get_comments()
    print " trying comments in %s" % subreddit
    if comments:
        for comment in comments:
            has_pandas = any(string in comment.body for string in Words)
            if has_pandas:
                print 'Comment found in %s' % subreddit
                print ' %s ' % comment.permalink
        
