#!/usr/bin/env python3

import reports
import os
import datetime

def __main__():
  desc_dir = "supplier-data/descriptions"
  report_path = "/tmp/processed.pdf"
  report_title = "Processed on {}".format(datetime.date.today())

  item_collector = {}
  for file in os.listdir(desc_dir):
    if file[-4:] == ".txt":
      with open(os.path.join(desc_dir, file), 'r') as f:
        content = f.readlines()
        item_collector.append("name: {}\nweight: {}\n\n".format(content[0], content[1]))
