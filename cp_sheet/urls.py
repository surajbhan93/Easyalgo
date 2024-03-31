from django.urls import path
from .views import front_cp,cp_detail, previous_post, next_post,BlogPostLike

urlpatterns = [
    path('', front_cp, name='front_cp'),
    path('<slug:slug>/', cp_detail, name='cp_detail'),
    path('post-like/<int:pk>/', BlogPostLike, name='cp_like'),  # Update the URL name
    path('post/previous/<slug:slug>/', previous_post, name='previous_post'),
    path('post/next/<slug:slug>/', next_post, name='next_post'),
]
