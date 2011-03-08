from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from imagekit.models import ImageModel

class Slideimage(ImageModel):
    name = models.CharField(blank=True, max_length=100)
    original_image = models.ImageField(blank=True, upload_to="slide_images")
    created = models.DateTimeField(_('created'), default=datetime.now, blank=True)
    modified = models.DateTimeField(_('modified'), blank=True)
    
    class IKOptions:
        """Image options from the imagekit module"""
        spec_module = 'slideshow.imagespecs'
        image_field = 'original_image'
        admin_thumbnail_spec = 'admin_thumbnail'
        cache_filename_format = "%(specname)s/%(filename)s.%(extension)s"
        cache_dir = '.'

    class Meta:
        ordering = ('name',)
        verbose_name = _('Slide Image')
        verbose_name_plural = _('Slide Images')

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.modified = datetime.now()
        super(Slideimage, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.name

class Slide(models.Model):
    """
    An individual slide.
    
    The slide contains the name of the slide, the slide copy and a slide image.
    
    future considerations need to be made for video.
    """
    name = models.CharField(blank=True, max_length=100)
    header = models.CharField(blank=True, max_length=200)
    body = models.TextField(blank=True)
    image = models.ForeignKey(Slideimage, blank=True, null=True)
    url = models.URLField(blank=True, verify_exists=True, help_text="When this slide is clicked, where do you want the user to go?")
    url_text = models.CharField(blank=True, max_length=255, help_text="What do you want the URL to say?")
    slug = models.SlugField(max_length=255, blank=True)
    created = models.DateTimeField(_('created'), default=datetime.now, blank=True)
    modified = models.DateTimeField(_('modified'), blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        
    def save(self, force_insert=False, force_update=False):
        self.modified = datetime.now()
        super(Slide, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.name