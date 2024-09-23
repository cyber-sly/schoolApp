from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_student, name="register_student" ),
    path('scholarships/', views.scholarship_search, name="scholarship_search" ),
]
