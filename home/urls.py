from django.contrib import admin
from django.urls import path, include
from home import views
from django.urls import path
from .views import contact
# from htmlapp.views import fronth,html_detail
from blogs.views import frontpage, post_detail, BlogPostLike, previous_post, next_post
urlpatterns = [
    # path('', views.index, name='home'),
    path('', frontpage, name='frontpage'),
    path('<slug:slug>/',post_detail, name='post_detail'),
    path('post-like/<int:pk>/',BlogPostLike, name='post_like'),  # Update the URL name
    path('post/previous/<slug:slug>/', previous_post, name='previous_post'),
    path('post/next/<slug:slug>/', next_post, name='next_post'),
    path('about', views.about, name='about'),
    
    path('project1', views.project1, name='blog'),
    path('projects', views.projects, name='projects'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('thanks', views.thanks, name='thanks'),
    path('DSA1',views.DSA1, name='dsa'),
    # path('login/',views.login,name='login'),
    # path('signup/',views.signup,name='signup'),
    # path('logout/',views.logout,name='logout'),
    
    path('Support' , views.Support ,name='support'),
    path('Cookie1',views.Cokies,name="Cokies"),
    path('Privacy',views.Privacy,name="Privacy"),
    path('certificate', views.certificate, name="certificate"),
     
    path('free_certificate', views.free_certificate, name="free_certificate"),
    path('web_dovelopment', views.web_dovelopment, name="web_dovelopment"),
    path('infromatic', views.infromatic, name="infromatic"),
    path('UIXI', views.UIXI, name="UIXI"),
    path('applicatoion_dov', views.applicatoion_dov, name="applicatoion_dov"),

]
