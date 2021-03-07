import sys
import os
import json

sys.path.insert(0, 'src/lib')

from data import get_data
from ratio import make_ratios
from metrics_dataviz import *

def main(targets):
    all_flag = False

    with open('config/data-params.json') as fh:
        data_cfg = json.load(fh)
    
    if targets == []:
        all_flag = True

    if 'data' in targets or all_flag:
        get_data(data_cfg['scientific_path'], data_cfg['misinformation_path'])

    if 'ratio' in targets or all_flag:
        make_ratios(data_cfg['scientific_path'], data_cfg['misinformation_path'], 
                    data_cfg['scientific_politicians'], data_cfg['misinformation_politicians'])

    if 'metrics' in targets or all_flag:
        sort_files(data_cfg['scientific_path'])
        sort_files(data_cfg['misinformation_path'])

        outpath = data_cfg['output_path']
        sci_path = data_cfg['scientific_path']
        misinfo_path = data_cfg['misinformation_path']
        sci_sort_path = data_cfg['scientific_sorted_path']
        misinfo_sort_path = data_cfg['misinformation_sorted_path']
        x_months = 4
        x_tweets = 200

        count_likes_over_months(sci_path, outpath, 'scientific')
        count_likes_over_months(misinfo_path, outpath, 'misinfo')

        avg_likes_over_months(sci_path, outpath, 'scientific', x_months)
        avg_likes_over_months(misinfo_path, outpath, 'misinfo', x_months)

        max_likes_over_months(sci_path, outpath, 'scientific', x_months)
        max_likes_over_months(misinfo_path, outpath, 'misinfo', x_months)

        cumu_likes_over_months(sci_path, outpath, 'scientific')
        cumu_likes_over_months(misinfo_path, outpath, 'misinfo')

        count_likes_over_tweets(sci_sort_path, outpath, 'scientific')
        count_likes_over_tweets(misinfo_sort_path, outpath, 'misinfo')

        avg_likes_over_tweets(sci_sort_path, outpath, 'scientific', x_tweets)
        avg_likes_over_tweets(misinfo_sort_path, outpath, 'misinfo', x_tweets)

        max_likes_over_tweets(sci_sort_path, outpath, 'scientific', x_tweets)
        max_likes_over_tweets(misinfo_sort_path, outpath, 'misinfo', x_tweets)

        cumu_likes_over_tweets(sci_sort_path, outpath, 'scientific')
        cumu_likes_over_tweets(misinfo_sort_path, outpath, 'misinfo')

    if 'visualization' in targets or all_flag:
        scientific_ratios_graph(data_cfg['scientific_path'], data_cfg['output_path'], data_cfg['scientific_politicians'])
        misinfo_ratios_graph(data_cfg['misinformation_path'], data_cfg['output_path'], data_cfg['misinformation_politicians'])

        sci_avg_likes_time_path = outpath + 'scientific_avg_likes_over_months.json'
        mis_avg_likes_time_path = outpath + 'misinfo_avg_likes_over_months.json'

        sci_largest_ratio(['Sen. Lisa Murkowski', 'Rep. Katie Porter'], sci_avg_likes_time_path, outpath)
        misinfo_largest_ratio(['Lindsey Graham', 'Tulsi Gabbard 🌺'], mis_avg_likes_time_path, outpath)
        both_largest_ratio(['Sen. Lisa Murkowski', 'Lindsey Graham'], sci_avg_likes_time_path, mis_avg_likes_time_path, outpath)
        

    if 'permute' in targets or all_flag:
        pass


    if 'test' in targets: 
        sci_likes_over_months(["User4", "User5", "User6"], data_cfg['test_scientific_path'], data_cfg['test_output_path'], 5)
        misinfo_likes_over_months(["User1", "User2", "User3"], data_cfg['test_misinformation_path'], data_cfg['test_output_path'], 5)
        compare_sci_misinfo(["User4", "User1"], data_cfg['test_scientific_path'], data_cfg['test_misinformation_path'], data_cfg['test_output_path'], 5)
        max_all_sci(data_cfg['test_scientific_path'], data_cfg['test_output_path'], 5)
        max_all_misinfo(data_cfg['test_misinformation_path'], data_cfg['test_output_path'], 5)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)