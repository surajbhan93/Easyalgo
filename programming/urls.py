from django.urls import path
from .views import front_pr, pr_detail, previous_post, next_post,BlogPostLike


urlpatterns = [
    path('', front_pr, name='front_pr'),
    path('<slug:slug>/', pr_detail, name='pr_detail'),
    path('post-like/<int:pk>/', BlogPostLike, name='prpost_like'), 
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]
