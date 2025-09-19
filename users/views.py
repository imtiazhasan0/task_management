from django.shortcuts import render, redirect
from users.forms import RegisterForm, CustomRegstrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def Sign_up(request):
    form = CustomRegstrationForm()
    if request.method == 'POST':
        form = CustomRegstrationForm(request.POST)
        if form.is_valid():
            form.save() 
        else:
            print("Form is not valid")

    context={
            'form': form
            }
    return render(request,'register.html', context)

def Sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def Sign_out(request):
    if request.method == 'POST':
        logout(request)
    return redirect('Sign_in')