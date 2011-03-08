from django.contrib import admin
from slideshow.models import Slide, Slideimage

class SlideimageAdmin(admin.ModelAdmin):
    exclude = ('created', 'modified',)

class SlideAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('created', 'modified',)
    
admin.site.register(Slide, SlideAdmin)
admin.site.register(Slideimage, SlideimageAdmin)