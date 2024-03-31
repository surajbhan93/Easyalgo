from .models import prepration_sheet

def previous_post(slug):
    current_post = prepration_sheet.objects.get(slug=slug)
    previous_post = prepration_sheet.objects.filter(pk__lt=current_post.pk).order_by('-pk').first()
    return previous_post

def next_post(slug):
    current_post = prepration_sheet.objects.get(slug=slug)
    next_post = prepration_sheet.objects.filter(pk__gt=current_post.pk).order_by('pk').first()
    return next_post
