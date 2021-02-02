import json
import pandas as pd
import time
import os

import config

def get_metrics(politician_file, filepath):
    
    working_path = os.getcwd()
    os.chdir(filepath)
    
    check = politician_file + '.csv'
    
    if check in os.listdir():
        print("The ratios for " + politician_list + " already exist.")
        os.chdir(working_path)
        return
    
    text_file = open(politician_file + ".txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    metrics_list = []
    for i in range(0, len(lines), 100):
        partition = lines[i:i+100]
        partition_string = ','.join(partition)

        request = os.popen("curl 'https://api.twitter.com/2/tweets?ids=" + partition_string + "&tweet.fields=public_metrics' --header 'Authorization: Bearer " + config.bearer_token + "'").read()

        if 'exceeded' in request:
            print("Rate Limit Exceeded. Sleeping for 15 Minutes.")
            time.sleep(60*15)
            request = os.popen("curl 'https://api.twitter.com/2/tweets?ids=" + partition_string + "&tweet.fields=public_metrics' --header 'Authorization: Bearer " + config.bearer_token + "'").read()

        to_json = json.loads(request)

        metrics_data = pd.DataFrame.from_dict(to_json['data'])
        metrics_list.append(metrics_data)

    metrics = pd.concat(metrics_list, ignore_index=True)
    
    ratios_table = pd.concat([metrics, metrics['public_metrics'].apply(pd.Series)], axis=1)
    ratios = (ratios_table['reply_count'] * 2) / ((ratios_table['retweet_count']) + (ratios_table['like_count']))
    ratios = ratios.rename('ratio')
    ratios_table = pd.concat([ratios_table, ratios], axis=1)
    
    ratios_table.to_csv(politician_file + '.csv', index=True)
    print("The csv for " + politician_file + " has been completed.")
    
    os.chdir(working_path)
    
    return ratios_table

def get_csvs(scientific_path, misinformation_path, scientific_list, misinformation_list):

    for i in range(len(scientific_list)):
        get_metrics(scientific_list[i], scientific_path)

    for i in range(len(misinformation_list)):
        get_metrics(misinformation_list[i], misinformation_path)