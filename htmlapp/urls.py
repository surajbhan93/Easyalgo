from django.urls import path
from .views import fronth, html_detail,BlogPostLike, previous_post, next_post

urlpatterns = [
    path('', fronth, name='fronth'),
    path('<slug:slug>/', html_detail, name='html_detail'),
    path('post-like/<int:pk>/', BlogPostLike, name='htmlpost_like'),
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]
