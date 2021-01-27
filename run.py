import sys
import os
import json

sys.path.insert(0, 'src/data')

from data import lists

def main(targets):

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        get_data(**data_cfg)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)