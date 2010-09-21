from django.shortcuts import render_to_response
from django import template
from tri.slideshow.models import Slide

register = template.Library()
    
@register.inclusion_tag('slideshow/slideshow.html')
def slideshow():
    """A Slideshow"""
    slides = Slide.objects.all()
    return {'slides': slides}