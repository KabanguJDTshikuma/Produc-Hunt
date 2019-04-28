from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST': # User has info, wants an account now
        # check if password match
        if request.POST['password1'] == request.POST['password2']:
            # check if the username not taken
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                # if not taken
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'] )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'password must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect'})

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # TODO need to route to home page and dont
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'accounts/login.html')

