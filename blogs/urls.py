from django.urls import path
from .views import frontpage, post_detail, BlogPostLike, previous_post, next_post

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('post-like/<int:pk>/', BlogPostLike, name='post_like'),  # Update the URL name
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]
