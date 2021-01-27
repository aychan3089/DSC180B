import os 
import json
import ast
import matplotlib.pyplot as plt

s_path = '../src/data/scientific/'
c_path = '../src/data/conspiracy/'


# cumulative count
# {name: {tweet number: total likes}}
cumulative_likes_per_tweet = {}

# {name: num tweets}
num_tweets_per_account = {}

for subdir, dirs, files in os.walk(s_path):
    for file in files:
        filepath = os.path.join(subdir, file)
            
        with open(filepath, encoding='utf-8') as f:
            for line in f.readlines():
                # tweet = json.loads(line)
                tweet = ast.literal_eval(line)
                
                name = tweet['user']['name']
                
                if name not in cumulative_likes_per_tweet:
                    cumulative_likes_per_tweet[name] = {}
                    num_tweets_per_account[name] = 0
                    
                num_tweets_per_account[name] += 1
                likes = tweet['favorite_count'] 
                cumulative_likes = cumulative_likes_per_tweet.get(name).get(num_tweets_per_account[name] - 1, 0)
                cumulative_likes_per_tweet[name][num_tweets_per_account[name]] = likes + cumulative_likes


# running mean over cumulative tweets 
# {name: {tweet_number: average likes last x tweets}}
avg_likes_lastx_tweets = {}

# {name: num tweets}
num_tweets_per_account = {}

all_likes = []
x_tweets = 50

for subdir, dirs, files in os.walk(s_path):
    for file in files:
        filepath = os.path.join(subdir, file)
        
        with open(filepath, encoding='utf-8') as f:
            for line in f.readlines():
                tweet = ast.literal_eval(line)
                
                name = tweet['user']['name']
                
                if name not in avg_likes_lastx_tweets:
                    avg_likes_lastx_tweets[name] = {}
                    num_tweets_per_account[name] = 0
                    all_likes = []
                
                num_tweets_per_account[name] += 1
                likes = tweet['favorite_count']
                all_likes.append(likes)
                
                avg_likes = sum(all_likes[-x_tweets:]) // len(all_likes[-x_tweets:])
                avg_likes_lastx_tweets[name][num_tweets_per_account[name]] = avg_likes


# cumlative max 
# {name: {tweet_number: cumulative max}}
max_likes_per_tweet = {}

# {name: num tweets}
num_tweets_per_account = {}

for subdir, dirs, files in os.walk(s_path):
    for file in files:
        filepath = os.path.join(subdir, file)
        
        with open(filepath, encoding='utf-8') as f:
            for line in f.readlines():
                tweet = ast.literal_eval(line)
                
                name = tweet['user']['name']
                
                if name not in max_likes_per_tweet:
                    max_likes_per_tweet[name] = {}
                    num_tweets_per_account[name] = 0
                    
                num_tweets_per_account[name] += 1
                likes = tweet['favorite_count']

                max_likes = max(likes, max_likes_per_tweet[name].get(num_tweets_per_account[name] - 1, 0))
                max_likes_per_tweet[name][num_tweets_per_account[name]] = max_likes


# rolling max 
# {name: {tweet number: rolling max}}
max_likes_lastx_tweets = {}

# {name: num tweets}
num_tweets_per_account = {}

all_likes = []
x_tweets = 50

for subdir, dirs, files in os.walk(s_path):
    for file in files:
        filepath = os.path.join(subdir, file)
        
        with open(filepath, encoding='utf-8') as f:
            for line in f.readlines():
                tweet = ast.literal_eval(line)
                
                name = tweet['user']['name']
                
                if name not in max_likes_lastx_tweets:
                    max_likes_lastx_tweets[name] = {}
                    num_tweets_per_account[name] = 0
                    
                num_tweets_per_account[name] += 1
                likes = tweet['favorite_count']
                all_likes.append(likes)
                
                max_likes = max(all_likes[-x_tweets:])
                max_likes_lastx_tweets[name][num_tweets_per_account[name]] = max_likes


def convert_date(date):
    created_at = tweet['created_at'].split()
    month_conversion = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    return str(month_conversion[created_at[1]]) + '.' + created_at[-1]


# cumulative count over time 
# {name: {date: count}}
likes_over_time = {}

for subdir, dirs, files in os.walk(s_path):
    for file in files:
        filepath = os.path.join(subdir, file)
        
        with open(filepath, encoding='utf-8') as f:
            for line in f.readlines():
                tweet = ast.literal_eval(line)
                
                name = tweet['user']['name']
                
                if name not in likes_over_time:
                    likes_over_time[name] = {}
                    
                date = convert_date(tweet['created_at'])
                
                likes_over_time[name][date] = likes_over_time[name].get(date, 0) + tweet['favorite_count']

# cumulative max over time 
# {name: {date: max}}

# running mean over time 
# {name: {date: rolling mean}}

# running max over time
# {name: {date: rolling max}}