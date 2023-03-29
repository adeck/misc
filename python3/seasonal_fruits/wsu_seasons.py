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

# the months are from 1 - 12
now_month_idx = date.today().month
now_month_str = calendar.month_name[now_month_idx]

# I need it zero-indexed, hence subtracting
now_month_idx = now_month_idx - 1

print(f'For the month of {now_month_str}, the following produce are in season:')
with open('data.csv', 'r') as f:
    header = False
    for line in (l.strip() for l in f.readlines()):
        if not header:
            assert line == 'Product;Months Harvested'
            header = True
            continue
        fruit, months = line.split(';')
        assert months[now_month_idx] in {'1', '0'}
        if months[now_month_idx] == '1':
            print(f'{months}: {fruit}')


