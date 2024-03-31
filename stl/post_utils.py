from .models import stl

def previous_post(slug):
    current_post = stl.objects.get(slug=slug)
    previous_post = stl.objects.filter(pk__lt=current_post.pk).order_by('-pk').first()
    return previous_post

def next_post(slug):
    current_post = stl.objects.get(slug=slug)
    next_post =stl.objects.filter(pk__gt=current_post.pk).order_by('pk').first()
    return next_post