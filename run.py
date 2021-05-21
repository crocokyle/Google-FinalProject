#!/usr/bin/env python3

import os
import requests

txt_path = "supplier-data/descriptions"
url = "http://34.123.34.240/fruits/"


for txt in os.listdir(txt_path):
  if txt[-4:] == ".txt":
    line_list = []
    dictionary = {}
    with open(os.path.join(txt_path, txt), 'r') as file:
      for line in file.readlines():
        line_list.append(line[:-1])
 
      dictionary['name'] = line_list[0]
      dictionary['weight'] = int(line_list[1][:-4])
      dictionary['description'] = line_list[2]
      dictionary['image_name'] = txt[:-4] + ".jpeg"

    print(dictionary)
    x = requests.post(url, json=dictionary)
    if not x.ok:
      print(x.status_code)
      print(x.text)
