from pandas import read_csv
import csv

df = read_csv('basic-data.csv')
dfhead = df.head()
print(dfhead)

csv_data = dfhead.to_csv('output.csv', sep=',')
print('\nCSV String:\n', csv_data)