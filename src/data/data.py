import tweepy
import config
# Authenticate twitter
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

import time 
import datetime
import numpy as np
import os
import json

def get_tweets(politician_list, group_name, startDate, endDate):
    
    #Define our date range
    startDate = datetime.datetime.strptime(startDate, '%y/%m/%d')
    endDate = datetime.datetime.strptime(endDate, '%y/%m/%d')

    orig_dir = os.getcwd()
    
    #Creates a folder for each group that we've defined if one does not already exist
    if os.path.isdir(group_name) == False:
        os.mkdir(group_name)
    os.chdir(group_name)
    
    
    for i in range(len(politician_list)):
        
        #If we've already gathered data for this politician, continue to the next one in the list
        if os.path.isdir(politician_list[i]) == False:
    
            # Fetch twitter user id of an account you know the screen name
            user_name = politician_list[i]
            user_object = api.get_user(id=user_name)    
            user_id = user_object.id

            #Fetch tweet ids from a timeline within our date range
            tweets = []
            tmpTweets = api.user_timeline(user_id, count=200)
            for tweet in tmpTweets:
                #Appends tweets within our date range to the list of tweets
                if tweet.created_at < endDate and tweet.created_at > startDate:
                    tweets.append(tweet)

            try:
                #Keeps on iterating back through previous tweets while making sure its still within the defined date range
                while (tmpTweets[-1].created_at > startDate) and (len(tmpTweets) > 1):

                    #Next set of 200 tweets
                    tmpTweets = api.user_timeline(user_id, max_id = tmpTweets[-1].id, count=200)

                    #Append the next set if we haven't reached the end
                    if len(tmpTweets) != 1:
                        for tweet in tmpTweets:
                            if tweet.created_at < endDate and tweet.created_at > startDate:
                                tweets.append(tweet)

            #We can only get around 3,200 tweets for each politician    
            #If they are really active we won't be able to page back far enough and so the while loop will throw an error
            #This makes the function continue and writes the tweets we've already obtained to the politician's folder
            except IndexError:
                pass

            if len(tweets) > 0:
                #Creates a folder for each politician
                #Writes the timeline tweets to a jsonl file within the politicians folder
                filename = user_name + '.jsonl'
                foldername = user_name
                folder = os.path.join(foldername)
                file = os.path.join(folder, filename)
                os.mkdir(folder)
                with open(file, 'w') as f:
                    for item in tweets:
                        f.write("%s\n" % json.dumps(item._json))

                print("The data for " + politician_list[i] + " has been obtained")

            else: 
                print("There are no tweets that have been found. Please double check the username for: " + politician_list[i])

        else:
            print("The data for " + politician_list[i] + " already exists.")
            continue

    os.chdir(orig_dir)
        
def lists(scientific, misinformation, control_filepath, startDate, endDate):
    get_tweets(scientific, 'scientific', startDate, endDate)
    get_tweets(misinformation, 'misinformation', startDate, endDate)
    control_list = get_control_list(control_filepath)
    get_tweets(control_list, 'control', startDate, endDate)

def get_control_list(filepath):
    politician_file = open(filepath, "r")
    politician_list = politician_file.read().splitlines()
    return politician_list