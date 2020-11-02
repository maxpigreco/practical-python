def portfolio_cost(filename):
	with open(filename, 'rt') as f:
		headers = next(f).split(',')
		cost = 0
		for line in f:
			row = line.split(',')
			round(int(row[1]) * float(row[2]), 2)
			cost = cost + (int(row[1]) * float(row[2]))
		return cost


cost = portfolio_cost('C:/Users/max/practical-python//Work/Data/portfolio.csv')
print('Total cost:', cost)
    
    
