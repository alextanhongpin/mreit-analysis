#coding:utf8
from __future__ import division
import json
import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

def convertToJson(fileName): 
  f = open(fileName + '.txt')
  lines = [line.strip() for line in f.readlines() if line.strip() != '']

  # List of header title
  header = lines[:7]

  # List of Reits
  reits = []
  for i in range(int(len(lines[7:]) / 7)):
    index = 7 + i * 7
    reits.append(lines[index:index + 7])


  data = []

  for reit in reits:
    obj = {}
    for i, value in enumerate(reit):
      key = header[i]
      obj[key] = value
    data.append(obj)

  jsonData = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


  output = open(fileName + '.json', 'w')
  output.write(jsonData)
  output.truncate()
  output.close()

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".txt"):
          # /Users/alextanhongpin/Google Drive/Programming/python/mreit-data/raw_txt/august-2016.txt
          fileName = os.path.join(root, file).replace(".txt", "")
          convertToJson(fileName)
          out_dir = fileName.replace("raw_txt", "raw_json")
          out_dir = out_dir[:out_dir.find("/raw_json/") + len("/raw_json/")]
          if not os.path.exists(out_dir):
            os.makedirs(out_dir)
          shutil.copy(fileName + '.json', out_dir)
          os.remove(fileName + '.json')
