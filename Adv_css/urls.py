from django.urls import path
from Adv_css.views import frontt, css_detail,previous_post, next_post,BlogPostLike

urlpatterns = [
    path('', frontt, name='frontt'),  # Maps the root URL to the frontt view
    path('<slug:slug>/', css_detail, name='css_detail'),  # Maps URLs with a slug parameter to the css_detail view
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('post-like/<int:pk>/', BlogPostLike, name='csspost_like'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]

