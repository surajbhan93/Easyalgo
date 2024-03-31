from django.shortcuts import render
from .post_utils import previous_post, next_post

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404
from .models import prepration_sheet
# add this line together with the other imports
from prepration_sheet.forms import CommentForm
# Create your views here.
def sheet_front(request):
    posts = prepration_sheet.objects.all()
    
    return render(request, 'prepration_sheet/sheet_front.html',{'posts':posts})

def detail_sheet(request, slug):
    post = get_object_or_404(prepration_sheet, slug=slug)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail_sheet', slug=post.slug)

    # Get the previous and next posts
    previous_post = prepration_sheet.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = prepration_sheet.objects.filter(pk__gt=post.pk).order_by('pk').first()

    context = {
        'post': post,
        'form': form,
        'number_of_likes': post.number_of_likes(),
        'post_is_liked': post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
        'previous_post': previous_post,
        'next_post': next_post,
    }

    return render(request, 'prepration_sheet/detail_sheet.html', context)

def BlogPostLike(request, pk):
    post = get_object_or_404(prepration_sheet, pk=pk)
    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('detail_sheet', kwargs={'slug': post.slug}))
