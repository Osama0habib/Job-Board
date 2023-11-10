from django.contrib.auth import authenticate, login 
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .form import SignupForm ,UserForm , ProfileForm
from .models import Profile


def signin(request):
    form = login();
    
    return render(request,'registration/login.html',{"form" : form})
def signup(request):  
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')
            user = authenticate(username=username ,password=password)
            login(user=user)
            return redirect('/accounts/profile ')
    else:
        form = SignupForm()    
    return render(request,'registration/signup.html',{"form" : form})


def profile(request):
    profile = Profile.objects.get(user =  request.user)
    return render(request,'account/profile.html',{'profile' : profile})


def profile_edit(request):
    profile = Profile.objects.get(user =  request.user)
    if request.method == 'POST' :
        userForm = UserForm(request.POST ,instance=request.user)
        profileForm = ProfileForm(request.POST,request.FILES,instance=profile,)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save();
            myProfile = profileForm.save(commit = False)
            myProfile.user = request.user
            myProfile.save() 
            return redirect(reverse_lazy('accounts:profile'))       
    else :
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)
    return render(request,'account/profile_edit.html',{'userForm' : userForm,'profileForm' : profileForm})
