#!/usr/bin/env python3
#
#  This code isn't really necessary unless the underlying website data changes.
#   Leaving  it here just in case the underlying data changes.
#
#   This script reads data in the format of:
#       https://extension.wsu.edu/whatcom/seasonal-harvest-guide/
#   And outputs a CSV from the HTML table. CSV is of the format:
#       Product;Months Harvested
#   Where "Months Harvested" is a 12-character string of zeroes and ones.
#       1 -> it is harvested that month
#       0 -> it is not harvested that month
#

from bs4 import BeautifulSoup
import urllib.request

DATA_URL = 'https://extension.wsu.edu/whatcom/seasonal-harvest-guide/'

def main():
    # In reality, I downloaded the HTML and ran this offline.
    # But I'm commenting that out and having it be an online script to
    #   make it easier for future users.
#    with open('harvest_guide_page.html', 'r') as f:
    with urllib.request.urlopen(DATA_URL) as f:
        soup = BeautifulSoup(f, 'html.parser')
    print('Product;Months Harvested')
    header_row = None
    for tr in soup.tbody:
        if is_empty(tr):
            continue
        if header_row is None:
            header_row = tr
        if tr == header_row:
            continue
        line = process_tr(tr)
        print(line)

def is_empty(elem):
    return elem.string is not None and elem.string.strip() == ''

def process_tr(tr):
    fruit = None
    months = ''
    for td in tr:
        if is_empty(td):
            continue
        td_strs = list(td.stripped_strings)
        assert len(td_strs) in {1, 0}
        if fruit is None:
            assert len(td_strs) == 1
            fruit = td_strs[0]
            continue
        months += str(len(td_strs))
    assert len(months) == 12
    #print(fruit)
    assert ';' not in fruit
    return f'{fruit};{months}'

if __name__ == '__main__':
    main()

