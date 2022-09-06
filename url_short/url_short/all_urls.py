from django.urls import path

from auth_api import views as auth_views
from url_api import views as url_views


urlpatterns = [
    path('register', auth_views.user_registration),
    path('login', auth_views.user_login),
    path('logout', auth_views.user_logout),
    path('profile', auth_views.user_profile),
    path('create', url_views.create_short_url),
]