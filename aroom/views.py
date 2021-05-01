from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html', {})

def log_in(request):
    if request.method == "POST":
        # check that user login with correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def log_out(request):
    print("Nitin")
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password != re_password:
            return render(request, 'signup.html')

        # creat user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
    return render(request, 'signup.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })