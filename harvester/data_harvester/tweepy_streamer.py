'''
    author: Group25
            Fangfei Zheng 965378 (China)
            Jingjiahui Lu 966172 (Melb)
            Xi Chen 983241(China)
            Haoran Zhang 960374 (China)
            Pengnan Zhao 883338(China)

'''

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import couchdb

import twitter_credentials

box = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]     
    
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self,server_address):
        self.server_address=server_address

    def stream_tweets(self, server_address,locations):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(server_address)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(locations=box)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    def __init__(self,server_address):
      #  self.fetched_tweets_filename = fetched_tweets_filename
        self.server_address=server_address
        self.couch = couchdb.Server(server_address)
        

    def on_data(self, data):
        try:
            db_tweet=self.couch['tweet4']
            db_user=self.couch['user']
            
            tweet = json.loads(data)
            doc_id = tweet["id_str"]
            if doc_id not in db_tweet:
                db_tweet[doc_id] = {"tweet": tweet}
            print("new tweet: "+doc_id)
            
            doc_id = tweet["user"]["id_str"] 
            if tweet["user"]["id_str"] not in db_user: 
                db_user[doc_id] = {"id":tweet["user"]["id"],"screen_name":tweet["user"]["screen_name"] ,"isProcessed":False}
                
            print(data)

            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)


def run(server_address):
    couchserver = couchdb.Server(server_address)
    #couchserver = couchdb.Server("http://admin:12345@172.26.130.200:5984/")

    db_tweet_name = 'tweet4'
    db_user_name = 'user'
    if db_tweet_name in couchserver:
        db_tweet = couchserver[db_tweet_name]
    else:
        db_tweet = couchserver.create(db_tweet_name)

    if db_user_name in couchserver:
        db_user = couchserver[db_user_name]
    else:
        db_user = couchserver.create(db_user_name)
        
    box = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235] 
    twitter_streamer = TwitterStreamer(server_address)
    twitter_streamer.stream_tweets(server_address,box)
