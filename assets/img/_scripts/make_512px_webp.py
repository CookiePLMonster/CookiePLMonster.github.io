import os
import sys

from PIL import Image

THUMB_SIZE = (512, 512)
WEBP_QUALITY = 85

for path in sys.argv[1:]:
    directory, filename = os.path.split(path)
    stem, ext = os.path.splitext(filename)
    with Image.open(path) as image:
        path = os.path.join(directory, stem + '.webp')

        image.thumbnail(THUMB_SIZE)
        image.save(path, lossless=False, quality=WEBP_QUALITY, method=6)
