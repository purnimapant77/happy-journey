from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def retreats(request):
    return render(request, 'core/retreats.html')


def trekking(request):
    return render(request, 'core/trekking.html')


def gallery(request):
    return render(request, 'core/gallery.html')


def reviews(request):
    return render(request, 'core/reviews.html')


def blogs(request):
    return render(request, 'core/blogs.html')


def contact(request):
    return render(request, 'core/contact.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username/email or password.'

    return render(request, 'core/login.html', {'error': error})


def logout_view(request):
    auth_logout(request)
    return redirect('home')