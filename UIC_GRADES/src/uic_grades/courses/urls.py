from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('filter_courses/', views.filter_courses, name='filter_courses'),
]