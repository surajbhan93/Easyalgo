from .models import cs_subject
def previous_post(slug):
    current_post = cs_subject.objects.get(slug=slug)
    previous_post = cs_subject.objects.filter(pk__lt=current_post.pk).order_by('-pk').first()
    return previous_post

def next_post(slug):
    current_post = cs_subject.objects.get(slug=slug)
    next_post = cs_subject.objects.filter(pk__gt=current_post.pk).order_by('pk').first()
    return next_post