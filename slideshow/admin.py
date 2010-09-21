from django.contrib import admin
from tri.slideshow.models import Slide, Slideimage

class SlideAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Slide, SlideAdmin)
admin.site.register(Slideimage)