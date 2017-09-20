# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,StudentForm
from .models import Student

# Create your views here.

@login_required
def homepage(request):
    u=request.user
    student=Student.objects.get(user=u)
    form=StudentForm(instance=student)
    return render(request,'student/homepage.html',{'section': 'homepage','form':form})

@login_required
def info_basic(request):
    return render(request,'student/info_basic.html',{'section': 'info'})

@login_required
def info_profile(request):
    return render(request,'student/info_profile.html',{'section': 'info'})

@login_required
def info_ps(request):
    return render(request,'student/info_ps.html',{'section': 'info'})

@login_required
def info_recommend(request):
    return render(request,'student/info_recommend.html',{'section': 'info'})

@login_required
def info_other(request):
    return render(request,'student/info_other.html',{'section': 'info'})

@login_required
def info_files(request):
    return render(request,'student/info_files.html',{'section': 'info'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                         'student/register_done.html',
                         {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'student/register.html',
                 {'user_form': user_form})


