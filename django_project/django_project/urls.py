"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', include('django.contrib.auth.urls')),
    path('register/', users_views.register, name='register'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html',
         ),
         name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profile, name='profile'),
    path('', include('blog.urls'))
]

# urlpatterns = [
#     url('password-reset-confirm/<uidb64>/<token>/',
#         auth_views.PasswordResetConfirmView.as_view(
#             template_name='users/registration/password_reset_confirm.html',
#             success_url='users/password_reset_complete'),
#         name='password_reset_confirm'),
#     url(r'^admin/', admin.site.urls),
#     # url(r'^', include('django.contrib.auth.urls')),
#     url('register/', users_views.register, name='register'),
#     url('password-reset/done/',
#         auth_views.PasswordResetDoneView.as_view(
#             template_name='users/registration/password_reset_done.html'
#         ),
#         name='password_reset_done'),
#     url('password-reset/',
#         auth_views.PasswordResetView.as_view(
#             template_name='users/registration/password_reset.html',
#         ),
#         name='password_reset'),
#     url('password-reset-complete/',
#         auth_views.PasswordResetCompleteView.as_view(
#             template_name='users/registration/password_reset_complete.html',
#         ),
#         name='password_reset_complete'),
#     url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     url('profile/', users_views.profile, name='profile'),
#     url('', include('blog.urls'))
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
