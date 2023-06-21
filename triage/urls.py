from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_triage/', views.add_triage, name='add_triage'),
    path('patients_list/',views.patients_list,name='patients_list'),
    path('show_triage/<int:pk>/', views.show_triage, name='show_triage'),
    path('search/', views.search, name='search'),
        # Date Time field related library:
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),



]