import os
import json
from mlxtend.evaluate import permutation_test
from metrics import count_likes_over_months

def make_months():
    return {str(year):[] for year in range(2008, 2021)}

def group_likes_over_years(path):
    '''
    creates {year: [likes]} to be used for permutation tests 
    '''
    likes_over_years = make_months()

    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(subdir, file)
            
            if not file.endswith('.jsonl'):
                continue

            with open(filepath, encoding='utf-8') as f:
                for line in f.readlines():
                    tweet = json.loads(line)
                    
                    if tweet['full_text'][:2] == 'RT':
                        # dont count a tweet if it is a retweet 
                        continue 
                    
                    year = tweet['created_at'].split()[-1]
                    likes = tweet['favorite_count']

                    likes_over_years[year].append(likes)
    return likes_over_years