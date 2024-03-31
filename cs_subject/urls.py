from django.urls import path
from .views import front_cs,cd_detail, previous_post, next_post,BlogPostLike

urlpatterns = [
    path('', front_cs, name='front_cs'),  # Maps the root URL to the frontt view
    path('<slug:slug>/', cd_detail, name='cd_detail'),  # Maps URLs with a slug parameter to the css_detail view
    path('post-like/<int:pk>/', BlogPostLike, name='cs_like'), 
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]
