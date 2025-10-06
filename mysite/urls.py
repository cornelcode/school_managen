from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Separate pages
    path('students/', views.students_page, name='students'),
    path('teachers/', views.teachers_page, name='teachers'),
    path('classes/', views.classes_page, name='classes'),
]
