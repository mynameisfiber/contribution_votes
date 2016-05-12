"""
Read in legistlator metadata from
https://github.com/unitedstates/congress-legislators and filter down/index on
bioguide id for later correlation
    - mynameisfiber (2016/05/11)
"""
import pandas as pd
import yaml
from tqdm import tqdm

import os


def parse_legislators(data, start_year=None):
    for legis in tqdm(data):
        if start_year:
            first_term_year = min(int(t['start'].split('-', 1)[0])
                                  for t in legis['terms'])
            if first_term_year < start_year:
                continue
        yield (legis['id']['bioguide'], legis)


def read_legistlators(fd, start_year=None):
    curdata = yaml.load(open(abspath))
    yield from parse_legislators(curdata, start_year=start_year)


if __name__ == "__main__":
    datapath = '/data/datasets/politics/congress/congress-legislators/'
    datafiles = ['legislators-current.yaml', 'legislators-historical.yaml']
    data = {}
    for datafile in tqdm(datafiles):
        abspath = os.path.join(datapath, datafile)
        new_data = read_legistlators(abspath, 2008)
        data.update(new_data)
    print(len(data))
