import json
import pandas as pd
import time
import os

import config

def get_ratios(politician_file, filepath):
    '''
    creates a csv of ratios for 
    '''
    working_path = os.getcwd()
    os.chdir(filepath)
    
    check = politician_file + '.csv'
    
    # Checks to make sure the csv file does not already exist before calling on the API
    if check in os.listdir():
        print("The ratios for " + politician_list + " already exist.")
        os.chdir(working_path)
        return
    
    # Opens the text file of tweet ids found in the filepath
    text_file = open(politician_file + ".txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    #List containing dataframes consisting of 100 rows
    metrics_list = []

    for i in range(0, len(lines), 100):
        # Gets 100 tweet ids at a time and passes it to the call to the API
        # The API can only look up metrics for 100 tweets at a time
        partition = lines[i:i+100]
        partition_string = ','.join(partition)

        request = os.popen("curl 'https://api.twitter.com/2/tweets?ids=" + partition_string + "&tweet.fields=public_metrics' --header 'Authorization: Bearer " + config.bearer_token + "'").read()

        #Check for rate limit, if exceeded we sleep for 15 minutes to reset the limit
        #Then continues where it left off for the tweet ids
        if 'exceeded' in request:
            print("Rate Limit Exceeded. Sleeping for 15 Minutes.")
            time.sleep(60*15)
            request = os.popen("curl 'https://api.twitter.com/2/tweets?ids=" + partition_string + "&tweet.fields=public_metrics' --header 'Authorization: Bearer " + config.bearer_token + "'").read()

        #A string with json is returned from the API call, this converts it to Json
        to_json = json.loads(request)

        #Takes the data portion of the output and turns it into a dataframe
        #Appends the dataframe of 100 rows to a list containing the smaller dataframes
        metrics_data = pd.DataFrame.from_dict(to_json['data'])
        metrics_list.append(metrics_data)

    #Appends the small dataframes of 100 into a larger dataframe
    metrics = pd.concat(metrics_list, ignore_index=True)
    

    #Calculates and gets the ratios using our formula of (2 * replies) / (retweets + likes)
    #Adds the ratio column to the dataframe
    ratios_table = pd.concat([metrics, metrics['public_metrics'].apply(pd.Series)], axis=1)
    ratios = (ratios_table['reply_count'] * 2) / ((ratios_table['retweet_count']) + (ratios_table['like_count']))
    ratios = ratios.rename('ratio')
    ratios_table = pd.concat([ratios_table, ratios], axis=1)
    
    #Saves the ratios dataframe to a csv file so we can reduce the number of API calls we make
    ratios_table.to_csv(politician_file + '.csv', index=True)
    print("The csv for " + politician_file + " has been completed.")
    
    os.chdir(working_path)
    
    return ratios_table


def make_ratios(scientific_path, misinformation_path, scientific_politicians, misinformation_politicians):
    '''
    set up for creating ratios csvs from the tweet ids 
    '''
    for i in range(len(scientific_politicians)):
        get_ratios(scientific_politicians[i], scientific_path)

    for i in range(len(misinformation_politicians)):
        get_ratios(misinformation_politicians[i], misinformation_path)