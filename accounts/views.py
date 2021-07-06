from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import LoginForm, UserRegistrationForm, \
                    UserEditForm, ProfileEditForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse("Invalid Login")
    else:   
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})
                

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
        return render(request, 'accounts/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
                            instance=request.user,
                            data=request.POST)

        profile_form = ProfileEditForm(
                            instance=request.user.profile,
                            data=request.POST,
                            files=request.FILES)
    
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
                                'successfully')
            return render(request,
                'accounts/dashboard.html',)
        
        else:
            messages.error(request, 'Error updating your profile')
            return render(request,
                'accounts/edit.html',)


    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                            instance=request.user.profile)
    
        return render(request,
                    'accounts/edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})