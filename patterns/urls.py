from django.urls import path
from .views import pr_pattern,patt_detail,previous_post,next_post

urlpatterns = [
    path('', pr_pattern, name='pr_pattern'),
    path('<slug:slug>/', patt_detail, name='patt_detail'),
    # path('post-like/<int:pk>/', BlogPostLike, name='post_like'),  # Update the URL name
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]
