from django.urls import path
from .views import sheet_front, detail_sheet,previous_post, next_post,BlogPostLike

urlpatterns = [
    path('', sheet_front, name='sheet_front'),  # Maps the root URL to the frontt view
    path('<slug:slug>/', detail_sheet, name='detail_sheet'),  # Maps URLs with a slug parameter to the css_detail view
    path('post-like/<int:pk>/', BlogPostLike, name='programpost_like'), 
    path('previous/<slug:slug>/', previous_post, name='previous_post'),
    path('next/<slug:slug>/', next_post, name='next_post'),
]
