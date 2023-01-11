from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', main_page, name='mainPage'),
    path('relevance/', relevance, name='relevance'),
    path('geography/', geography, name='geography'),
    path('skills/', skills, name='skills'),
    path('recent_vacancies/', recent_vacancies, name='recentVacancies'),
]
