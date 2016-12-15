from django.shortcuts import render

def IndexView(request):
    return render(request, 'MainSite/index.html')

def error404View(request):
    return render(request, 'MainSite/error404.html')

def eventDescriptionView(request):
    return render(request, 'MainSite/eventDescription.html')

def sponsorsView(request):
    return render(request, 'MainSite/sponsors.html')