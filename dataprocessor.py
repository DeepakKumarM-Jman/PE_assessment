from pandas import read_csv
import csv

df = read_csv('/app/src/basic-data.csv')
dfhead = df.head()
print(dfhead)

csv_data = dfhead.to_csv('/app/dest/output.csv', sep=',')
print('\nCSV String:\n', csv_data)