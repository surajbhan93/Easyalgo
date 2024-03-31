from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from blogs.forms import CommentForm
from blogs.models import Post
from django.core.paginator import Paginator
from .post_utils import previous_post, next_post

def frontpage(request):
    # Get all posts
    all_posts = Post.objects.all()
    
    # Number of posts per page
    posts_per_page = 8 # Adjust as needed
    
    # Initialize Paginator object
    paginator = Paginator(all_posts, posts_per_page)
    
    # Get current page number from request
    page_number = request.GET.get('page')
    
    # Get posts for the current page
    posts = paginator.get_page(page_number)
    return render(request, 'blogs/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        # If post with given slug doesn't exist, redirect to frontpage or handle error
        return redirect('frontpage')  # You can customize this behavior as needed

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)

    # Get previous and next posts
    previous_post = Post.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = Post.objects.filter(pk__gt=post.pk).order_by('pk').first()

    context = {
        'post': post,
        'form': form,
        'number_of_likes': post.number_of_likes(),
        'post_is_liked': post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'blogs/post_details.html', context)

def BlogPostLike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'slug': post.slug}))
