from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from segmi.views import home
from .forms import *
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form_p = ProfileRegisterForm(request.POST)
        if form.is_valid() and form_p.is_valid():
            form.save()
            myuser = form.save()
            username = form.cleaned_data.get('username')
            profile = form_p.save(commit=False)
            profile.user = myuser
            profile.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            messages.success(request, f'Account created for {username}!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
        form_p = ProfileRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'form_p': form_p})


@login_required
def profile(request):
    u_form = ProfileUpdateForm( request.POST, instance=request.user.profile)
    if request.method == 'POST':
        u_form = ProfileUpdateForm( request.POST, instance=request.user.profile)
        # form1 = ProfilePatient(request.POST, instance=request.user.profile)
        if request.user.profile.category == 'Patient':
            form1 = ProfilePatient(request.POST, instance=request.user.profile)
        elif request.user.profile.category == 'Doctor':
            form1 = ProfileDoctor(request.POST, instance=request.user)
        else:
            form1 = ProfileLab(request.POST, instance=request.user.profile)

    if u_form.is_valid() and form1.is_valid():
        u_form.save()
        form1.save()
        messages.success(request, f'Your account has been updated!')
        return redirect(home)


    else:
        u_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        print(request.user.profile)
        if request.user.profile.category=='Patient':
            form1 = ProfilePatient(request.POST,instance=request.user.profile)

        elif request.user.profile.category=='Doctor':
            form1 = ProfileDoctor(request.POST, instance=request.user)

        else:
            form1 = ProfileLab(request.POST,instance=request.user.profile)


    context = {
            'u_form': u_form,
            'form':form1
        }
    return render(request, 'users/profile.html',context)


@login_required
def myprofile(request):
    if request.user.profile.category=='Patient':
        context ={
            'category ': request.user.profile.category,
            'user_details':request.user.profile.user_details,
            'age ':request.user.profile.age,
            'gender': request.user.profile.gender,
            'disease': request.user.profile.disease,
        }

    elif request.user.profile.category=='Doctor':
        context ={
            'category ': request.user.profile.category,
            'user_details':request.user.profile.user_details,
            'license_number': request.user.profile.license_number,
            'degree':request.user.profile.degree,
            'age ':request.user.profile.age,
        }

    else:
        context ={
            'category ': request.user.profile.category,
            'user_details':request.user.profile.user_details,
            'license_number': request.user.profile.license_number,
            'labname': request.user.profile.labname,
            'labaddress': request.user.profile.labaddress,
        }
        
    return render(request, 'users/myprofile.html',context)