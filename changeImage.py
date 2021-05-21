#!/usr/bin/env python3

import os
import tqdm
from PIL import Image

image_path = "~/supplier-data/images"

for pic in tqdm(os.listdir(image_path)):
   img = Image.open(os.path.join(image_path, pic)).convert("RGB").resize((600, 400))
