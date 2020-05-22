# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:11:18 2020

@author: l
"""
import time
import twitter_search
import tweepy_streamer
import sys

def run(ip):
    server_path = 'http://admin:12345@'+ip+':5984/'
    #server_path = 'http://admin:12345@localhost:5984/'
    tweepy_streamer.run(server_path)
    time.sleep(200)
    twitter_search.run(server_path)
    

if __name__ == "__main__":

    #server_path = 'http://natlllu:12345@localhost:5984/'    
    #server_path = 'http://' + username +':' + password +'@'+ip+':5984/'
    ip = sys.argv[1]
<<<<<<< HEAD:data_harvester/run.py
    
=======
>>>>>>> ed6d0c1d092438280d2f933475961202d96c1ded:data harvester/run.py
    run(ip);
    


