from django.http.response import HttpResponse
from django.shortcuts import render

def IndexView(request):
    return render(request, 'UserAccount/index.html')

def error404View(request):
    return render(request, 'MainSite/error404.html')

def loginView(request):
    # TODO add user login logic
    return render(request, 'UserAccount/login.html')

def registerView(request):
    # TODO add user register logic
    return render(request, 'UserAccount/register.html')

def profileDataView(request):
    return render(request, 'UserAccount/profileOverview.html')

def resultsTableView(request):
    return render(request, 'UserAccount/eventResultsTable.html')

def photosFromEventView(request):
    return HttpResponse("Redirection to photo service site")

def password_resetView(request):
    return render(request, 'UserAccount/password_reset.html')