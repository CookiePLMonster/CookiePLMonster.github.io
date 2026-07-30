import os
import sys

from PIL import Image

THUMB_SIZE = (1024, 1024)
WEBP_QUALITY = 85

for path in sys.argv[1:]:
	directory, filename = os.path.split(path)
	stem, ext = os.path.splitext(filename)
	with Image.open(path) as image:
		width, height = image.size
		thumb_path = os.path.join(directory, 'thumb')
		os.makedirs(thumb_path, exist_ok=True)
		thumb_path = os.path.join(thumb_path, stem + '.webp')

		image.thumbnail(THUMB_SIZE)
		image.save(thumb_path, lossless=False, quality=WEBP_QUALITY, method=6)
