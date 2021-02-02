import sys
import os
import json

sys.path.insert(0, 'src/lib')

from data import get_data
from ratio import get_csvs

def main(targets):

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        get_data(**data_cfg)

    if 'ratio' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        get_csvs(**data_cfg)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)