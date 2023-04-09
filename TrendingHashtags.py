# to run: python3 TrendingHashtags.py > hashtags.txt

import os
import tweepy
import time, sys 
import json

import warnings
warnings.filterwarnings("ignore")

keyFile = open('secret.json')
apiKeys = json.load(keyFile);

# Variables that containsw the user credentials to access Twitter API 
ACCESS_TOKEN = apiKeys['access_token']
ACCESS_TOKEN_SECRET =  apiKeys['access_token_secret']
CONSUMER_KEY = apiKeys['consumer_key']
CONSUMER_SECRET = apiKeys['consumer_secret']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

trending = api.get_place_trends(id = 44418)

CWD = os.getcwd()
filename = os.path.join(CWD, "hashtags.txt")
DATA_WRITER = open(filename, "w")

#Trending topics
topics = [x['name'] for x in trending[0]['trends']]
for topic in topics:
	DATA_WRITER.write(topic + '\n')