Historical Population of the U.S. States - Spreadsheet (CSV)
============================================================

This repository contains a spreadsheet in CSV format of the historical population of the 50 states of the United States plus the District of Columbia by year from 1900 to the present.

[historical_state_population_by_year.csv](historical_state_population_by_year.csv)

Data is from the U.S. Census's Annual Estimates of the Population for the U.S. and States, and for Puerto Rico (http://www.census.gov/popest/) as published by the Federal Reserve Bank of St. Louis at https://fred.stlouisfed.org/release?rid=118 because fred.stlouisfed.org provides cleanly fetchable tables for 1900-present. Unfortunately fred.stlouisfed.org does not include Puerto Rico's population.

The columns of the spreadsheet are the state's USPS abbreviation, the year, and the population.

This repository also contains a Python 3 script `fetch.py` which fetches the data and produces the CSV file:

```sh
python3 fetch.py > historical_state_population_by_year.csv
```

Last updated in February 2020, which includes 2019 population.
