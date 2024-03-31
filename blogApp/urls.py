from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import login, signup, logout,ResetPasswordView,check_email_view,contact
from django.contrib.auth import views as auth_views
from allauth.socialaccount import views as socialaccount_views
# from .views import 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('cs1/', include('Adv_css.urls')),
    path('post/', include('blogs.urls')),  # Corrected path for the blogs app
    path('htmlapp/', include('htmlapp.urls')),
    path('front_pr/', include('programming.urls')),
    path('pattern/', include('patterns.urls')),
    path('cs_subject/', include('cs_subject.urls')),
    path('cp_sheet/', include('cp_sheet.urls')),
    path('mini_sheet/', include('mini_sheet.urls')),
    path('DBMS/', include('DBMS.urls')),
    path('contact/', contact, name='contact'),
    path('networking/', include('networking.urls')),
    path('prepration_sheet/', include('prepration_sheet.urls')),
    path('stl/', include('stl.urls')),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('check-email/', check_email_view, name='check-email'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
