from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher, ClassRoom
from datetime import datetime


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'school/login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    context = {'year': datetime.now().year}
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def students_page(request):
    students = Student.objects.all()
    context = {'students': students, 'year': datetime.now().year}
    return render(request, 'students.html', context)


@login_required(login_url='login')
def teachers_page(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers, 'year': datetime.now().year}
    return render(request, 'teachers.html', context)


@login_required(login_url='login')
def classes_page(request):
    classes = ClassRoom.objects.all()
    context = {'classes': classes, 'year': datetime.now().year}
    return render(request, 'classes.html', context)
