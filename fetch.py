# Downloads historical population of the 50 states plus DC from the
# U.S. Census's Annual Estimates of the Population for the U.S. and
# States, and for Puerto Rico (http://www.census.gov/popest/) as
# published by the Federal Reserve Bank of St. Louis at
# https://fred.stlouisfed.org/release?rid=118 because fred.stlouisfed.org
# provides cleanly fetchable tables for 1900-2017. Unfortunately it
# does not include Puerto Rico's population.
#
# Usage:
# python3 fetch.py > historical_state_population_by_year.csv

import csv
import io
import sys
import urllib.request

try:
	from tqdm import tqdm
except ImportError:
	def tqdm(arg, *rest, **kwrest): return arg

states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

W = csv.writer(sys.stdout)

for state in tqdm(states):
	url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}POP".format(state)
	resp = urllib.request.urlopen(url)
	for date, pop in csv.reader(io.TextIOWrapper(resp)):
		if date == "DATE": continue # skip header
		if not date.endswith("-01-01"): raise Exception(date)
		date = date.replace("-01-01", "")
		W.writerow([state, date, int(round(float(pop)*1000))])
