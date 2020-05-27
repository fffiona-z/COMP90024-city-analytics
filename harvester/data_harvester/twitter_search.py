'''
    author: Group25
            Fangfei Zheng 965378 (China)
            Jingjiahui Lu 966172 (Melb)
            Xi Chen 983241(China)
            Haoran Zhang 960374 (China)
            Pengnan Zhao 883338(China)

'''

import json
import couchdb
import tweepy
from tweepy import OAuthHandler
import twitter_credentials


class TweetSearchHavester():

    def __init__(self,couch):
        #self.server_address=server_address
        self.couch = couch
    def run(self, ids, db_tweet2):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        for id in ids:
           self.get_all_tweets(id,api,db_tweet2)
    
    def get_all_tweets(self, user_id, api,db_tweet2):
        try:
            for tweetorig in tweepy.Cursor(api.user_timeline,id = user_id ).items(80):  #use item to adjust the number of tweets waiting to get
                tweet = tweetorig._json
                doc_id = tweet["id_str"]
                if doc_id not in db_tweet2:
                    print(tweet)
                    if tweet["place"] :
                        country =tweet["place"]["country_code"]
                        if country=='AU':
                                db_tweet2[doc_id] = {"tweet": tweet}
                                print("new tweet: "+doc_id)
        except Exception as e:
            
            print(e)
            pass



def run(server_address): 
    
    couchserver = couchdb.Server(server_address)
    db_tweet2_name = 'tweet4'

    if db_tweet2_name in couchserver:
        db_tweet2 = couchserver[db_tweet2_name]
    else:
        db_tweet2 = couchserver.create(db_tweet2_name)

    db = couchserver['user']    
    userInList=0;
    pendingUserList = list()
    getNewTweets = TweetSearchHavester(couchserver)
    while True:
        for id in db:
            data = db[id]
            if(not data['isProcessed']):
                pendingUserList.append(id)
                userInList+=1
            else: #already processed
                continue
            if(userInList > 30):
                userInList = 0
                getNewTweets.run(pendingUserList,db_tweet2)
                for id in pendingUserList:
                    data = db[id]
                    data['isProcessed'] = True
                    db.save(data)
                pendingUserList = list()
        print("done")
       
