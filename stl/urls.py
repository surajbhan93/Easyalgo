from django.urls import path
from .views import front_stl,stl_detail,previous_post,next_post,BlogPostLike

urlpatterns = [
    path('', front_stl, name='front_stl'),
    path('<slug:slug>/', stl_detail, name='stl_detail'),
    path('post-like/<int:pk>/', BlogPostLike, name='stl_like'),  # Update the URL name
    path('post/previous/<slug:slug>/', previous_post, name='previous_post'),
    path('post/next/<slug:slug>/', next_post, name='next_post'),
]
