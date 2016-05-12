import pandas as pd
import yaml

import os


def parse_legislators(data, start_year=None):
    for legis in data:
        if start_year:
            first_term_year = int(legis['terms'][0]['start'].split('-', 1)[0])
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
    for datafile in datafiles:
        abspath = os.path.join(datapath, datafile)
        new_data = read_legistlators(abspath, 2008)
        data.update(new_data)
    print(len(data))
