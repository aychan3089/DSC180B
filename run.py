import sys
import os
import json

sys.path.insert(0, 'src/lib')

from data import get_data
from ratio import get_csvs
from metrics_dataviz import *

def main(targets):

    if targets == []:
        pass

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        get_data(**data_cfg)

    if 'ratio' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        get_csvs(**data_cfg)

    if 'metrics' in targets:
        pass

    if 'visualization' in targets:
        pass

    if 'test' in targets: 
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        sci_likes_over_months(["User4", "User5", "User6"], data_cfg['test_scientific_path'], data_cfg['test_output_path'], 5)
        misinfo_likes_over_months(["User1", "User2", "User3"], data_cfg['test_misinformation_path'], data_cfg['test_output_path'], 5)
        compare_sci_misinfo(["User4", "User1"], data_cfg['test_scientific_path'], data_cfg['test_misinformation_path'], data_cfg['test_output_path'], 5)
        max_all_sci(data_cfg['test_scientific_path'], data_cfg['test_output_path'], 5)
        max_all_misinfo(data_cfg['test_misinformation_path'], data_cfg['test_output_path'], 5)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)