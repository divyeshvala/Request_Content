
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register_view(request):
    if request.method == "POST": # means we got data from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2 :
            if User.objects.filter(username=username) :
                messages.info(request, 'username already taken')
            elif User.objects.filter(email=email):
                messages.info(request, 'email already taken')
            else :
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('user created')
                return redirect('login_view_url')      # <- here we pass name field of url pattern
        else :
            messages.info(request, "passwords not matching")

    # else
    return render(request, 'register.html', {})
    
# login view & log out view
def login_view(request):
    user = request.user
        
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('home_view')
        else :
            messages.info(request, 'Invalid credentials')

    return render(request, 'login_screen.html', {'user':user})

def logout_view(request):
    auth.logout(request)
    return redirect('home_view')


	

