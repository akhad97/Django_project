from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.conf.urls import url
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView
# from django.contrib.auth import login as dj_login

def landing_page(request):
    return render(request, 'portal/landing_page.html')

def student_signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            return redirect('login')
    else:
        form = StudentForm()
    context = {'form':form}
    return render(request, 'portal/student_signup.html', context)

def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            return redirect('login')
    else:
        form = TeacherForm()
    context = {'form':form}
    return render(request, 'portal/teacher_signup.html', context)

def loginPage(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_student:
                    login(request, user)
                    return redirect('student_dashboard')
                if user.is_teacher:
                    login(request, user)
                    return redirect('teacher_dashboard')
                else:
                    return render(request, 'portal/inactiv_account.html')
            else:
                return render(request, 'portal/inactiv_account.html')
    else:
        form = UserLoginForm()
        
    context = {'form':form}
    return render(request, 'portal/login.html', context)

def student_dashboard(request):
    documents = Document.objects.all()

    return render(request, 'portal/student_dashboard.html', {'documents': documents})




def teacher_dashboard(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_dashboard')
    else:
        form = DocumentForm()
    
    context = {'form':form}
    return render(request, 'portal/teacher_dashboard.html', context)

def edit_profile(request):
    if request.method == 'POST':
        user_profile = UserEditForm(data=request.POST or None, instance=request.user)
        if user_profile.is_valid():
            user_profile.save()
            return redirect('student_dashboard')
    else:
        user_profile = UserEditForm(instance=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'portal/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'portal/change_password.html', context)

def password_reset(request):
    return render(request, 'portal/password_reset_form.html')

def user_logout(request):
    logout(request)
    return redirect('/')
