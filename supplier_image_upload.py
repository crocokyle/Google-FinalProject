#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
image_path = "supplier-data/images"

for pic in os.listdir(image_path):
  if pic[-4:] == "jpeg":
    with open(os.path.join(image_path, pic), 'rb') as file:
      r = requests.psot(url, files={'file': file})
      if not r.ok:
        print(r.status)
        print(r.text)

