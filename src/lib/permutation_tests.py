import os
import json
import numpy as np 
from mlxtend.evaluate import permutation_test

def make_years():
    return {str(year):[] for year in range(2008, 2021)}

def group_likes_over_years(path, user=None):
    '''
    creates {year: [likes]} to be used for permutation tests 
    '''
    likes_over_years = make_years()

    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(subdir, file)
            
            if not file.endswith('.jsonl'):
                continue

            with open(filepath, encoding='utf-8') as f:
                for line in f.readlines():
                    tweet = json.loads(line)
                    
                    if user and user tweet['user'] != user:
                        # dont count tweet if user is not user we want 
                        continue 
                    
                    if tweet['full_text'][:2] == 'RT':
                        # dont count a tweet if it is a retweet 
                        continue 
                    
                    year = tweet['created_at'].split()[-1]
                    likes = tweet['favorite_count']
                    
                    if likes > 0:
                        likes_over_years[year].append(likes)
    return likes_over_years

def normalize_likes(likes_over_years):
    '''
    normalize likes over current year using (curr_year_likes - mean_lastyear_likes) / mean_last_year_likes
    ''' 
    normal_likes_over_years = {}
    years = [str(year) for year in range(2008, 2021)]
    
    for i in range(1, len(years)):
        prev_mean = np.mean(likes_over_years[years[i-1]])
        normal_likes_over_years[years[i]] = list(map(lambda x: (x - prev_mean) / prev_mean, likes_over_years[years[i]]))
        
    return normal_likes_over_years

def run_permutation_between(dist1, dist2, outpath):
    '''
    run permutation test between scientific and misinformation 
    '''
    years = [str(year) for year in range(2009, 2021)]
    s = ""
    for year in years:
        p_value = permutation_test(dist1[year],
                                   dist2[year],
                                   method='approximate',
                                   num_rounds=10000,
                                   seed=42)
        s += 'Scientific vs Misinformation permutation test for year '+ year + ': the p-value is  ' + str(p_value) + '.\n'
    
    with open(outpath, 'w+') as f:
        f.write(s)

def run_permutation_within(dist, category, outpath): 
    '''
    run permutation test within one group and compare year by year 
    '''
    years = [str(year) for year in range(2009, 2021)]
    s = ""
    for i in range(len(years)-1):
        p_value = permutation_test(dist[years[i]],
                                   dist[years[i+1]],
                                   method='approximate',
                                   num_rounds=10000,
                                   seed=42)
        s += '{0} {1} vs {0} {2} permutation test: the p-value is {3}. \n'.format(category, years[i], years[i+1], p_value)
    
    with open(outpath, 'w+') as f:
        f.write(s)