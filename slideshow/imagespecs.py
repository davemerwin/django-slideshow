# slideshow/imagespecs.py

from imagekit.specs import ImageSpec 
from imagekit import processors 

# first we define our thumbnail resize processor 
class ResizeThumb(processors.Resize): 
    width = 136
    height = 102 
    crop_horz_field = 1
    crop_vert_field = 1

# now we define a display size resize processor
class ResizeDisplay(processors.Resize):
    width = 940
    height = 300
    crop = True
    crop_horz_field = 1
    crop_vert_field = 1 

# now lets create an adjustment processor to enhance the image at small sizes 
class EnchanceThumb(processors.Adjustment): 
    contrast = 1.2 
    sharpness = 1.1 

# now we can define our thumbnail spec 
class Thumbnail(ImageSpec): 
    access_as = 'thumbnail_image' 
    pre_cache = True
    processors = [ResizeThumb, EnchanceThumb] 

# and our display spec
class Display(ImageSpec):
    access_as = 'display_image'
    pre_cache = True
    increment_count = True
    processors = [ResizeDisplay]