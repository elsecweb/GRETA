# python 3

# G.R.E.T.A. by ksebarnes - @barnfeline

# General Research Event Twitter Algorithm

############################

# greta collects tweets based on a keyword search

# twitter only allows you to collect all tweets posted within the last two weeks

# '-filter:retweets' clears the data of retweets so there are no repeats in your data

############################

# before running code: 'pip install tweepy' and 'pip install pandas'

import tweepy
import csv
import pandas as pd

############################

# input your credentials here from twitter's api for authorization

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

############################

# open/create a file to append data

csvFile = open('XXX.csv', 'a')

############################

# use csv writer to write collected data

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="'KEYWORD', 'KEYWORD' -filter:retweets",count=200,  # both keywords must show up in the tweet for it to be collected
                           lang="en",
                           since="2019-11-20").items(): # make sure to change the date!
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
