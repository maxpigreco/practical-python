'''
Write a function read_prices(filename) that reads a set of prices such
 as this into a dictionary where the keys of the dictionary are the 
 stock names and the values in the dictionary are the stock prices.
'''

# Exercise 2.6

import csv

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


# read_prices('Data/prices.csv')

