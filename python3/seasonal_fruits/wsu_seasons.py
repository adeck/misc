#!/usr/bin/env python3
#
# What produce is in season this month in the Pacific northwest?
#   This script'll tell you, although it's only as good as the data in data.csv.
#
# Data adapted from:
#   https://extension.wsu.edu/whatcom/seasonal-harvest-guide/
#

import calendar
from datetime import date

def print_produce(month_idx: int):
    """month_idx must be a value in [1, 12]"""
    month_str = calendar.month_name[month_idx]

    print(f'For the month of {month_str}, the following produce are in season:')
    with open('data.csv', 'r') as f:
        rows = (l.strip().split(';') for l in f.readlines())
        assert next(rows) == ['Product', 'Months Harvested']
        for product, months in rows:
            assert len(months) == 12
            if months[month_idx - 1] == '1':
                print(f'{months}: {product}') 

if __name__ == '__main__':
    print_produce(date.today().month)

