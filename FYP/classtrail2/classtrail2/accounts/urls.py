from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('teacher_register/', views.teacher_register.as_view(), name='teacher_register'),
    path('student_register/', views.student_register.as_view(), name='student_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('teacher_hub/', views.teacher_hub, name = 'teacher_hub'),
    path('manage_classes', views.manage_classes, name = 'manage_classes'),
]
