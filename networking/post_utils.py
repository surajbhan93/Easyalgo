from .models import networking

def previous_post(slug):
    current_post = networking.objects.get(slug=slug)
    previous_post = networking.objects.filter(pk__lt=current_post.pk).order_by('-pk').first()
    return previous_post

def next_post(slug):
    current_post = networking.objects.get(slug=slug)
    next_post = networking.objects.filter(pk__gt=current_post.pk).order_by('pk').first()
    return next_post