# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:11:18 2020

author: Group25
        Fangfei Zheng 965378 (China)
        Jingjiahui Lu 966172 (Melb)
        Xi Chen 983241(China)
        Haoran Zhang 960374 (China)
        Pengnan Zhao 883338(China)

"""
import time
import twitter_search
import tweepy_streamer
import sys

def run(server_path):
    #server_path = 'http://admin:12345@'+ip+':5984/'
#    server_path = 'http://admin:12345@localhost:5984/'
    #tweepy_streamer.run(server_path)
    twitter_search.run(server_path)
    

if __name__ == "__main__":

    server_path = 'http://admin:12345@localhost:5984/'    
    #server_path = 'http://' + username +':' + password +'@'+ip+':5984/'
    #ip = sys.argv[1]
    run(server_path);
    


