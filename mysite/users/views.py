from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth import logout

def register_user(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, your account has been successfully created")
            return redirect('login')
    # form = UserCreationForm()
    form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

def profile(request):
    return render(request,'users/profile.html')