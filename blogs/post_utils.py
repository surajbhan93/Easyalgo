from django.shortcuts import redirect, get_object_or_404
from .models import Post

def previous_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    previous_post = Post.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    if previous_post:
        return redirect('post_detail', slug=previous_post.slug)
    else:
        return redirect('frontpage')

def next_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    next_post = Post.objects.filter(pk__gt=post.pk).order_by('pk').first()
    if next_post:
        return redirect('post_detail', slug=next_post.slug)
    else:
        return redirect('frontpage')
