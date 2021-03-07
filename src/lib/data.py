import tweepy
import config
import time 
import datetime
import numpy as np
import os
import json

def rehydrate(directory_path):
    '''
    rehydrates the tweet ids in all txt files in the current directory 
    tweets are saved into a separate file with the same name into jsonl format 
    '''
    # Stores the current path so we can change back to it later
    cwd = os.getcwd()
    
    # Changes the path to the folder containing the files we wish to rehydrate
    os.chdir(directory_path)
    
    # Lists the files so we can iterate through them
    folder = os.listdir()
    
    for file in range(len(folder)):
        # Checks to make sure file ends in a txt extension 
        if folder[file][-4:] == '.txt':
            # Rehydrates the tweet ids using twarc
            os.system('twarc hydrate ' + folder[file] + ' > ' + folder[file][:-4] + '.jsonl')
            # print("Data for " + folder[file][:-4] + " has been obtained.")
        else:
            continue
            
    #Changes the directory to the original path
    os.chdir(cwd)
        
def get_data(scientific_path, misinformation_path):
    '''
    setup for rehyrating tweets for both our scientific and misinformation groups
    '''
    rehydrate(scientific_path)
    rehydrate(misinformation_path)