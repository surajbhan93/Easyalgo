from django.urls import path
from .views import front_mini,mini_detail,previous_post, next_post

urlpatterns = [
    path('', front_mini, name='front_mini'),
    path('<slug:slug>/', mini_detail, name='mini_detail'),
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
    # path('post-like/<int:pk>/', BlogPostLike, name='post_like'),  # Update the URL name
    # path('post/previous/<slug:slug>/', previous_post, name='previous_post'),
    # path('post/next/<slug:slug>/', next_post, name='next_post'),
]
