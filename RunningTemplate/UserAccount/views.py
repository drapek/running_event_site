#-*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render
from serverActions import userActions
from exceptions.FormExceptions import InputError

def IndexView(request):
    return render(request, 'UserAccount/index.html')

def error404View(request):
    return render(request, 'MainSite/error404.html')

def loginView(request):
    # TODO add user login logic

    # TODO if is already logged in, redirect to account homepage

    return render(request, 'UserAccount/login.html')

def registerView(request):
    # TODO if is already logged in, redirect to account homepage

    if not request.POST:
        # if POST data is empty simply render only pure register form.
        render(request, 'UserAccount/register.html')
    else:
        try:
            userActions.createUser(request.POST)
            return render(request, 'UserAccount/register.html', {'error_msg': error_msg})
        except InputError as e:
            error_msg = "Wystąpił błąd podczas przetwarzania danych"

            if( e.msg == "not every required filed is set"):
                error_msg = "Nie wszystkie wymagane pola zostały wypełnione!"

            if (e.msg == "passwords are not equal!"):
                error_msg = "Pola \'Hasło\' i \'Powtórz hasło\' się nie zgadzają!"

            return render(request, 'UserAccount/register.html', {'error_msg': error_msg})

    return render(request, 'UserAccount/register.html')

def profileDataView(request):
    return render(request, 'UserAccount/profileOverview.html')

def resultsTableView(request):
    return render(request, 'UserAccount/eventResultsTable.html')

def photosFromEventView(request):
    return HttpResponse("Redirection to photo service site")

def password_resetView(request):
    return render(request, 'UserAccount/password_reset.html')