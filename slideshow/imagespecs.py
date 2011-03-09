# slideshow/imagespecs.py
# Sizes are up to you. I've done common size based on 960.gs 16 column view

from imagekit.specs import ImageSpec 
from imagekit import processors 

# first we define our thumbnail resize processor 
class ResizeThumb(processors.Resize): 
    width = 136
    height = 102 
    crop_horz_field = 1
    crop_vert_field = 1
    
# first we define our small resize processor 
class ResizeSmall(processors.Resize): 
    width = 100
    height = 100 
    crop_horz_field = 1
    crop_vert_field = 1

# first we define our medium resize processor 
class ResizeMedium(processors.Resize): 
    width = 136
    height = 102 
    crop_horz_field = 1
    crop_vert_field = 1

# first we define our large resize processor 
class ResizeLarge(processors.Resize): 
    width = 470
    height = 102 
    crop_horz_field = 1
    crop_vert_field = 1

# now we define a extra large size resize processor
class ResizeExtraLarge(processors.Resize):
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
    access_as = 'thumbnail' 
    pre_cache = True
    processors = [ResizeThumb, EnchanceThumb]
    
# now we can define our Small spec 
class Small(ImageSpec): 
    access_as = 'small' 
    pre_cache = True
    processors = [ResizeSmall]
    
# now we can define our Medium spec 
class Medium(ImageSpec): 
    access_as = 'medium' 
    pre_cache = True
    processors = [ResizeMedium]
    
# now we can define our Large spec 
class Large(ImageSpec): 
    access_as = 'medium' 
    pre_cache = True
    processors = [ResizeLarge]

# and our ExtraLarge spec
class ExtraLarge(ImageSpec):
    access_as = 'extralarge'
    pre_cache = True
    processors = [ResizeExtraLarge]