from django.urls import path

from auth_api import views as auth_views


urlpatterns = [
    path('register', auth_views.user_registration),
    path('login', auth_views.user_login),
    path('profile', auth_views.user_profile),
]