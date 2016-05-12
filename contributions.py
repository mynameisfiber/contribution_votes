"""
Reads data from lobbying contributions into a pandas dataframe.  Data directly
from the following source in it's raw XML format:

http://www.senate.gov/legislative/Public_Disclosure/contributions_download.htm
    - mynameisfiber (2016/05/11)
"""
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from tqdm import tqdm

from dateutil.parser import parse as DateParser
import os


FIELD_SPECS={
    'year': int,
    'amount': float,
    'registrantid': int,
    'clientid': int,
    'received': DateParser,
    'ContributionDate': DateParser,
}


def _dict_lower_keys(d):
    return {k.lower():v for k,v in d.items()}


def parse_contribution_filing(fd):
    dom = ET.fromstring(fd.read())
    for filing in tqdm(dom.findall('.//Filing')):
        for child in filing.findall('.//Contribution'):
            data = _dict_lower_keys(filing.attrib)
            data.update(_dict_lower_keys(child.attrib))
            for key, cast in FIELD_SPECS.items():
                try:
                    data[key] = cast(data[key])
                except KeyError:
                    pass
            yield data


def read_contribution_filings(datadir):
    for filename in tqdm(os.listdir(datadir)):
        if filename.endswith('.xml'):
            abspath = os.path.join(datadir, filename)
            filedata = parse_contribution_filing(open(abspath))
            yield from filedata


if __name__ == "__main__":
    datadir="/data/datasets/politics/lobby/contributions"
    raw_filings = read_contribution_filings(datadir)
    data = pd.DataFrame.from_dict(raw_filings)
    for field in ('contributiontype', 'honoree', 'id', 'contributor', 'type'):
        data[field] = data[field].astype('category')

