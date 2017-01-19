#coding:utf8

import sqlite3
import os
import json
import csv
conn = sqlite3.connect('mreit.db')

c = conn.cursor()

# Create a table if it doesn't already exist
# c.execute('''CREATE TABLE mreit (date text, assets_type text, dpu_sen real, nav_rm real, period text, price_rm real, name text, yield text)''')

# Drop a table
# c.execute('DROP TABLE mreit')


# Get one
for result in c.execute('SELECT * FROM mreit WHERE name=?', ('YTL Hospitality Reit',)):
  print result




def write_to_csv(file_name, data):
  with open(file_name + '.csv', 'wb') as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerow(('date', 'assets_type', 'dpu_sen', 'nav_rm', 'period', 'price_rm', 'name', 'yield'))
    for row in data:
      writer.writerow(row)

dir_path = os.path.dirname(os.path.realpath(__file__))

# The data that you want to store in database
data = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
      # Read JSON files
      if file.endswith(".json"):
        # /Users/alextanhongpin/Google Drive/Programming/python/mreit-data/raw_txt/august-2016.txt
        file_path = os.path.join(root, file)
        date = file_path[file_path.find('/raw_json/') + len('/raw_json/'):len(file_path)].replace(".json", "")
        reits = json.load(open(file_path))
        csv_data = []
        for reit in reits:
          data.append((date, reit['Assets Type'], float(reit['DPU (sen)']), float(reit['NAV (RM)']), reit['Period'], float(reit['Price (RM)']), reit['REIT'], reit['Yield']))
          csv_data.append((date, reit['Assets Type'], float(reit['DPU (sen)']), float(reit['NAV (RM)']), reit['Period'].encode('utf8'), float(reit['Price (RM)']), reit['REIT'], reit['Yield']))
        write_to_csv(date, csv_data)




# print data

# # Insert a row of data
# c.executemany('INSERT INTO mreit VALUES (?,?,?,?,?,?,?,?)', data)
# # Save (commit) the changes
# conn.commit()
# conn.close()