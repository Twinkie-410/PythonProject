from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('main/', main_page, name='mainPage')
]
