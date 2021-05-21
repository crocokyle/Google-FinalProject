#!/usr/bin/env python3

import reports
import os
import datetime

def parseData():
  desc_dir = "supplier-data/descriptions"
  report_path = "/tmp/processed.pdf"
  report_title = "Processed on {}".format(datetime.date.today())

  item_collector = []
  for file in os.listdir(desc_dir):
    if file[-4:] == ".txt":
      with open(os.path.join(desc_dir, file), 'r') as f:
        content = f.readlines()
        item_collector.append("name: {}\nweight: {}\n\n".format(content[0], content[1]))

  print("".join(item_collector))
  reports.generate_report(report_path, report_title, "".join(item_collector))

if __name__ == "__main__":
  parseData()
