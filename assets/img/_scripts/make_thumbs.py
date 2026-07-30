import os
import sys

from PIL import Image

THUMB_SIZE = (1024, 1024)
JPEG_QUALITY = 85

def image_is_transparent(image: Image, opaque: int = 255) -> bool:
    if 'A' in image.mode:
        # see if minimum alpha channel is below opaque threshold
        return image.getextrema()[image.mode.index('A')][0] < opaque
    if image.mode != 'P' or 'transparency' not in image.info:
        # format doesn't support transparency
        return None
    transparency = image.info['transparency']
    colors = image.getcolors()
    # check each color in the image
    if isinstance(transparency, bytes):
        # transparency is one byte per palette entry
        for _, index in colors:
            if transparency[index] < opaque:
                return True
    else:
        # transparency is palette index of fully transparent
        for _, index in colors:
            if transparency == index:
                return True
    return None

for path in sys.argv[1:]:
	directory, filename = os.path.split(path)
    stem, ext = os.path.splitext(filename)
    with Image.open(path) as image:
        width, height = image.size
        if width > THUMB_SIZE[0] or height > THUMB_SIZE[1]:
            has_transparency = image_is_transparent(image)
            if has_transparency:
                thumb_ext = '.png'
            else:
                thumb_ext = '.jpg'
            thumb_path = os.path.join(directory, 'thumb')
            os.makedirs(thumb_path, exist_ok=True)
            thumb_path = os.path.join(thumb_path, stem + thumb_ext)

            image.thumbnail(THUMB_SIZE)
            # If has_transparency is False then the alpha channel exists but is all 255
            if has_transparency is False:
                image = image.convert('RGB')

            image.save(thumb_path, quality=JPEG_QUALITY, optimize=True, progressive=True, subsampling=0)
