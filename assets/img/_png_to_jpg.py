import os
import sys

from PIL import Image

JPEG_QUALITY = 90

for filename in sys.argv[1:]:
	stem, ext = os.path.splitext(filename)
	if ext.lower() == '.png':
		jpg_path = stem + '.jpg'
		with Image.open(filename) as image:
			image = image.convert('RGB')
		image.save(jpg_path, quality=JPEG_QUALITY, optimize=True, progressive=True, subsampling=0)
