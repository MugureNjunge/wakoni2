from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import UserRegisterForm, ProfileForm, NewBusinessForm, NewPostForm
from django.contrib.auth.decorators import login_required

def index(request):
    
    return render(request, 'index.html')

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Account created for { username }!!')
            return redirect('locality')

    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'sign-up.html', context)   

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('locality')
        
        else:
            messages.success(request,('You information is not valid'))
            return redirect('sign-in')

    else:
        return render(request,'sign-in.html')

def signout(request):  
    logout(request) 

    return redirect('sign-in') 

@login_required(login_url='/accounts/sign-in/')
def local(request):
    return render(request,"locality.html")       


@login_required(login_url='/accounts/sign-in/')
def UserProfile(request, username):
   
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        
        'profile':profile,
        
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/accounts/sign-in/')
def EditProfile(request):
    
    user = request.user.id
    # current_user=request.user
    profile = Profile.objects.get(user_id=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            # profile.user = current_user
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            profile.fullname = form.cleaned_data.get('fullname')
            profile.locality = form.cleaned_data.get('locality')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile', profile.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {
        'form':form,
    }
    return render(request, 'editprofile.html', context) 

def Police(request):
    current_user = request.user
    if request.method == 'GET':

       return render(request, 'police.html', {"current_user":current_user})

def Health(request):
    current_user = request.user
    if request.method == 'GET':

       return render(request, 'health.html', {"current_user":current_user})

@login_required(login_url='/accounts/sign-in/')
def NewBusiness(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('locality')
        
    else:
        form = NewBusinessForm()
    return render(request, 'new-business.html', {"form":form, "current_user":current_user})

def search(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_business = Business.search_by_businesses(search_term)
        message = search_term

        return render(request,'search.html',{"message":message,
                                             "searched_business":searched_business})
    else:
        message = "You haven't searched for any business"
        return render(request,'search.html',{"message":message})   

@login_required(login_url='/accounts/sign-in/')
def NewPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('locality')
        
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {"form":form, "current_user":current_user})           


