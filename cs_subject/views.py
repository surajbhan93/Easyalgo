from django.shortcuts import render
from .post_utils import previous_post, next_post
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render,redirect,get_object_or_404
from .models import cs_subject
# add this line together with the other imports
from cs_subject.forms import CommentForm
# Create your views here.
def front_cs(request):
    posts = cs_subject.objects.all()
    
    return render(request, 'cs_subject/front_cs.html',{'posts':posts})

def cd_detail(request, slug):
    post = get_object_or_404(cs_subject, slug=slug)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('cd_detail', slug=post.slug)

    # Get the previous and next posts
    previous_post = cs_subject.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = cs_subject.objects.filter(pk__gt=post.pk).order_by('pk').first()

    context = {
        'post': post,
        'form': form,
        'number_of_likes': post.number_of_likes(),
        'post_is_liked': post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
        'previous_post': previous_post,
        'next_post': next_post,
    }

    return render(request, 'cs_subject/cd_detail.html', context)

def BlogPostLike(request, pk):
    post = get_object_or_404(cs_subject, pk=pk)
    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('cd_detail', kwargs={'slug': post.slug}))
