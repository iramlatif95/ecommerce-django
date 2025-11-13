from django.shortcuts import render,redirect
from . forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('login_user')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})



def login_user(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Creates session
                return redirect('profile')  # Replace 'home' with your homepage URL name
    else:
        form = AuthenticationForm()
    
    return render(request, 'login_user.html',{'form':form})

@login_required  # Ensures only logged-in users can access
def profile(request):
    user = request.user  # Get the logged-in user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


    

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_user')
    return redirect('signup')  # Prevent GET logout without POST





# Create your views here.
