from django.shortcuts import render

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