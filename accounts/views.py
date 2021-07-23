from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required


from django.contrib.auth.models import User
from .models import Profile, Contact
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


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
                  'accounts/user/list.html',
                  {'section': 'people',
                   'users': users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'accounts/user/detail.html',
                  {'section': 'people',
                   'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                            user_from=request.user,
                            user_to=user)
            else:
                Contact.objects.filter(user_from=request.user,
                                user_to=user).delete()
            return JsonResponse({'status':'ok'})

        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    
    return JsonResponse({'status':'error'})