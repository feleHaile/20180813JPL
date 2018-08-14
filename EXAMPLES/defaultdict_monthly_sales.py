#!/usr/bin/env python
#
from collections import defaultdict


MONTHS = '''
    Jan Feb Mar Apr May Jun
    Jul Aug Sep Oct Nov Dec
'''.split()


sales_data = defaultdict(lambda: 0) # <1>

# print(sales_data['wombat'])x
# print(sales_data['Rancho Cucamonga'])


with open('../DATA/sales_by_month.txt') as sbm_in:
    for line in sbm_in:
        month, raw_sales = line.split('|')
        sales = int(raw_sales)
        sales_data[month] += sales # <2>

for month in MONTHS:
    print("{}: {:5d}".format(month, sales_data[month])) # <3>

print(f"Total sales for year: {sum(sales_data.values())}")

