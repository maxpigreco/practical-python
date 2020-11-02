# pcost.py

# total_cost = 0.0

# with open('../../Work/Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         nshares = int(row[1])
#         price = float(row[2])
#         total_cost += nshares * price

# print('Total cost', total_cost)

# print("---" * 10)
# print("This is my solution:")

# with open('C:/Users/max/practical-python//Work/Data/portfolio.csv', 'rt') as f:
#     headers = next(f).split(',')
#     # print(headers)
#     cost = 0
#     for line in f:
#         row = line.split(',')
#         print(f"Cost of {row[0]} stocks, is $ {round(int(row[1]) * float(row[2]), 2)}")
#         cost = cost + (int(row[1]) * float(row[2]))
#     print("The total cost of the portfolio is:", round(cost, 2))

import csv

with open('../../Work/Data/portfolio.csv', 'rt') as f:
	rows = csv.reader(f)
	headers = next(rows)
	print(headers)
	for row in rows:
		print(row)


import sys

def portfolio_cost(filename):
	with open(filename, 'rt') as f:
		headers = next(f).split(',')
		cost = 0
		for line in f:
			row = line.split(',')
			round(int(row[1]) * float(row[2]), 2)
			cost = cost + (int(row[1]) * float(row[2]))
		return cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost('../../Work/Data/portfolio.csv')
print('*** Total cost:', cost, '***')