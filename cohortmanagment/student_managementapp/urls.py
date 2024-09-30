from django.urls import path
from .import views 
from .views import student_register, students_search
 
 
urlpatterns = [
    path('register/', views.student_register, name='student_register'),
    path('', views.students_search, name='student_list')
    
    
]
