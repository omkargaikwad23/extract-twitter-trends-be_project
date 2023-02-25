# tcrawl.py Crawls Twitter for the trends in hashtags.txt 
# To run: python crawl.py hashtags.txt path_to_store_tweets 
# Output: will create a file for tweets crawled for each trending topic/hasht

# Import the necessary methods from tweepy library
import sys

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy import TweepyException

import warnings
warnings.filterwarnings("ignore")

# Variables that contains the user credentials to access Twitter API 
# # keys from  "Twitter Tweet Summarization" app
access_token = '1395621591468306433-yB2Xj0dUtCl60iYDspEjq2eBuGubwW'
access_token_secret = "ssfp9kpkDkxNlyHjlVZL0uSIqxVrJ1hKnURwbKyOBpUEu"
consumer_key = "FIKIk9765mOgxYV86tBhRviu1"
consumer_secret = "gVSiUWUOVCyCm5HBu0YY1Q7vr7Us8mRgeBh5ixZ3kB1TqkCtVG"

import os.path
current_path = os.path.dirname(__file__)

RELATIVE_DIR = "\data\\"
DATA_FOLDER = sys.argv[2]
print(DATA_FOLDER)

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(Stream):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print (status)

def query_through_stream(topic):
    stream = Stream(auth, l)
    stream.filter(track=[topic])

def query_through_search(query):
	# print(type(DATA_FOLDER), print(type(query)))
	# print(DATA_FOLDER)
	print(query)
	TOPIC_DATA_HANDLER = open(DATA_FOLDER+ query, 'w')
	api = API(auth)
	
	tweets = dict()
	# # Initialization ## 
	max_tweets = 500
	tweet_count = 0
	max_id = -1
	since_id = None
	tweet_per_query = 100
	
	# print("Downloading tweets for query : "+query)
	while tweet_count < max_tweets:
		try:
			if (max_id <= 0):
				if (not since_id):
					new_tweets = api.search_tweets(q=query, count=tweet_per_query, lang="en", result_type="mixed", locale="en")
				else:
					new_tweets = api.search_tweets(q=query, count=tweet_per_query, since_id=since_id, lang="en", result_type="mixed", locale="en")
			else:
				if (not since_id):
					new_tweets = api.search_tweets(q=query, count=tweet_per_query, max_id=str(max_id - 1), lang="en", result_type="mixed", locale="en")
				else:
					new_tweets = api.search_tweets(q=query, count=tweet_per_query, max_id=str(max_id - 1), since_id=since_id, lang="en", result_type="mixed", locale="en")
			if not new_tweets:
				print("No more tweets found")
				break
			tweet_id_iter = None
			for tweet in new_tweets:
				# json_tweet = jsonpickle.encode(tweet._json, unpicklable=False)
				if(tweet.user.followers_count > 200 and tweet.text not in tweets):
					# tweet_text = (tweet.text).encode('utf-8').strip()
					tweet_text = (tweet.text)

					tweet_text = tweet_text.replace('\n', " ")
					
					tweets[tweet.text] = 1  # # for duplicate identification
					
					TOPIC_DATA_HANDLER.write(tweet_text + '\n\n')
					tweet_count += 1
					if(tweet_id_iter):
						tweet_id_iter = min(tweet_id_iter, tweet.id)
					else:
						tweet_id_iter = tweet.id
					if(tweet_count == max_tweets):
						break					
			# tweet_count += len(new_tweets)
			# print("Downloaded {0} tweets".format(tweet_count))
			# max_id = new_tweets[-1].id
			if tweet_id_iter == None:
				break
			max_id = tweet_id_iter
		except TweepyException as e:
			print("some error : " + str(e))
			break
	
def isEnglish(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
        
if __name__ == '__main__':
	# This handles Twitter authentication and the connection to Twitter Streaming API
	l = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	TOPICS = sys.argv[1]
	for topic in open(TOPICS, 'r'):
		# if(isEnglish(topic)):    		
		# print(type(topic))
		print(type(topic.encode('utf-8').strip()))
		query_through_search(topic)


	
	
