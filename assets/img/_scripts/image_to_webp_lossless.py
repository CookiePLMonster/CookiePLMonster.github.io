import os
import sys

from PIL import Image

for path in sys.argv[1:]:
	directory, filename = os.path.split(path)
	stem, ext = os.path.splitext(filename)
	with Image.open(path) as image:
		path = os.path.join(directory, stem + '.webp')
		image.save(path, lossless=True, quality=100, method=6)