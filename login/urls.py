from django.urls import path
from django.conf import settings
from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('triage/', include(('triage.urls','triage'), namespace='triage')),
    path('change-password', views.changePassword,name="changePassword"),
    path('change-email',views.changeEmail,name="changeEmail"),
]