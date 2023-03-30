#!/usr/bin/env python3
#
#  This code isn't really necessary unless the underlying website data changes.
#   Leaving  it here just in case the underlying data changes.
#
#   This script reads data in the format of:
#       https://extension.wsu.edu/whatcom/seasonal-harvest-guide/
#   And outputs a CSV from the HTML table. CSV is of the format:
#       Months Harvested;Product
#   Where "Months Harvested" is a 12-character string of zeroes and ones.
#       1 -> it is harvested that month
#       0 -> it is not harvested that month
#   "Product" is just the name of the product.
#

import calendar
import logging
import urllib.request

from bs4 import BeautifulSoup

DATA_URL = 'https://extension.wsu.edu/whatcom/seasonal-harvest-guide/'
MONTHS = [m.upper() for m in calendar.month_abbr]
LOG = logging.getLogger('seasonal_fruits')

def main():
    # In reality, I downloaded the HTML and ran this offline.
    # But I'm commenting that out and having it be an online script to
    #   make it easier for future users.
#    with open('harvest_guide_page.html', 'r') as f:
    with urllib.request.urlopen(DATA_URL) as f:
        soup = BeautifulSoup(f, 'html.parser')
    print('Months Harvested;Product')
    for tr in soup.select_one('tbody').select('tr'):
        row = [''.join(td.stripped_strings) for td in tr.select('td')]
        LOG.debug(row)
        assert len(row) == 13
        if row == MONTHS:
            continue # header row
        product = row[0]
        months = ''.join(map(lambda e: {'': '0', '*': '1'}[e], row[1::]))
        print(f'{months};{product}')

if __name__ == '__main__':
    main()

