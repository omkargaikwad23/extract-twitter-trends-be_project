# to run: python3 TrendingHashtags.py > hashtags.txt

import tweepy
import time, sys 

import warnings
warnings.filterwarnings("ignore")

ACCESS_TOKEN = '1395621591468306433-yB2Xj0dUtCl60iYDspEjq2eBuGubwW'
ACCESS_TOKEN_SECRET = 'ssfp9kpkDkxNlyHjlVZL0uSIqxVrJ1hKnURwbKyOBpUEu'
CONSUMER_KEY = 'FIKIk9765mOgxYV86tBhRviu1'
CONSUMER_SECRET = "gVSiUWUOVCyCm5HBu0YY1Q7vr7Us8mRgeBh5ixZ3kB1TqkCtVG"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

trending = api.get_place_trends(id = 44418)

#Trending topics
topics = [x['name'] for x in trending[0]['trends']]
for topic in topics:
	# print(topic.encode('utf-8').strip())
	print(topic)
	
# Trending hash tags
#hashtags = [x['name'] for x in trending[0]['trends'] if x['name'].startswith('#')]
#print hashtags
