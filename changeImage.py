#!/usr/bin/env python3

import os
from tqdm import tqdm
from PIL import Image

image_path = "supplier-data/images"

for pic in tqdm(os.listdir(image_path)):
   f_name = pic[:-4] + ".jpg"
   img = Image.open(os.path.join(image_path, pic)).convert("RGB").resize((600, 400)).save(os.path.join(image_path, f_name), "JPEG", quality=100)
