# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from forms import ImportRunResults
from exceptions.FormExceptions import InputError
from serverActions import userActions
from .models import RunResultsTable
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def indexView(request):
    loggedin_response = __redirect_if_not_logged_in(request)
    if loggedin_response:
        return loggedin_response

    return render(request, 'UserAccount/index.html')


def error404View(request):
    return render(request, 'MainSite/error404.html')


def loginView(request):
    # if user is logged in redirect him to user hompage
    if request.user.is_authenticated:
        return redirect('userAccount:userHome')

    if not request.POST:
        # if POST data is empty simply render only pure register form.
        return render(request, 'UserAccount/login.html')
    else:
        post = request.POST
        user = authenticate(username=post.get('username'), password=post.get('password'))
        if user is not None:
            login(request, user)
            # User is now logged in, so redirect to homepage! :)
            return redirect('userAccount:userHome')
        else:
            return render(request, 'UserAccount/login.html',
                          {'error_msg': 'Nie udało się zalogować! Upewnij się że wpisane hasło oraz login są poprawne'})
    return render(request, 'UserAccount/login.html')


def registerView(request):
    # if user is logged in redirect him to user hompage
    if request.user.is_authenticated:
        return redirect('userAccount:userHome')

    if not request.POST:
        # if POST data is empty simply render only pure register form.
        return render(request, 'UserAccount/register.html')
    else:
        try:
            userActions.createUser(request.POST)
            return render(request, 'UserAccount/register.html', {
                'info_msg': "Zarejestrowano użytkownika pomyślnie, pamiętaj by potwierdzić swój adres email."})
        except InputError as e:
            error_msg = "Wystąpił błąd podczas przetwarzania danych"

            if (e.msg == "not every required filed is set"):
                error_msg = "Nie wszystkie wymagane pola zostały wypełnione!"

            if (e.msg == "passwords are not equal!"):
                error_msg = "Pola \'Hasło\' i \'Powtórz hasło\' się nie zgadzają!"

            return render(request, 'UserAccount/register.html', {'error_msg': error_msg})
        except IntegrityError as e:
            error_msg = "Błąd zapisu do bazy danych."

            if (e.message == "UNIQUE constraint failed: auth_user.username"):
                error_msg = "Użytkownik o podanym nicku lub adresie email już istnieje!"

            return render(request, 'UserAccount/register.html', {'error_msg': error_msg})
        except Exception as e:
            if __debug__:
                return render(request, 'UserAccount/register.html', {'error_msg': e.message})
            return render(request, 'UserAccount/register.html',
                          {'error_msg': "Natąpił nieoczekiwany błąd. Przepraszamy!"})

    return render(request, 'UserAccount/register.html')


def profileDataView(request):
    loggedin_response = __redirect_if_not_logged_in(request)
    if loggedin_response:
        return loggedin_response

    msg = None
    userData = userData = userActions.readUserData(user_id=request.user.id)

    if not request.POST:
        # if POST data is empty simply render only pure register form.
        return render(request, 'UserAccount/profileOverview.html', {'message': msg, 'userData': userData})
    else:
        try:
            userActions.updateUserData(request.POST)
            userData = userActions.readUserData(user_id=request.user.id) # we must refresh data readed from database, because we have changed it
            msg = "Twoje dane zostały pomyślnie zaktualizowane"
        except InputError as e:
            msg = "Wystąpił błąd podczas przetwarzania danych"

            if (e.msg == "not every required filed is set"):
                msg = "Nie wszystkie wymagane pola zostały wypełnione!"

            if (e.msg == "passwords are not equal!"):
                msg = "Pola \'Hasło\' i \'Powtórz hasło\' się nie zgadzają!"

        except IntegrityError as e:
            msg = "Błąd zapisu do bazy danych."

        except Exception as e:
            if __debug__:
               msg = e.message

    return render(request, 'UserAccount/profileOverview.html', {'message': msg, 'userData': userData})


def resultsTableView(request):
    loggedin_response = __redirect_if_not_logged_in(request)
    if loggedin_response:
        return loggedin_response

    run_results_list = RunResultsTable.objects.order_by('time_overall')
    error_msg = None
    rows_per_page = 25
    page = 1
    int_user_id = None

    paginator = Paginator(run_results_list, rows_per_page)

    # find page with user on it, if id_user is given as GET parameter
    user_id = request.GET.get('user_id')
    if user_id is not None:
        try:
            int_user_id = int(user_id)
        except Exception:
            error_msg = "Podany numer użytkownika jest błędny."
            results = paginator.page(1)
            return render(request, 'UserAccount/eventResultsTable.html',
                          {'error_msg': error_msg, 'results_table': results,
                           'first_runner_position_on_page': (results.number - 1) * rows_per_page})

        user_position_in_database = None
        #find position in qeurySet, needed to display page (divided by pagination)  which contains our user
        for index, item in enumerate(run_results_list):
            tmp = item.runner_id_id
            if item.runner_id_id == int(user_id):
                user_position_in_database = index + 1
                break

        if user_position_in_database is None:
            error_msg = "Wynik użytkownika o numerze startowym " + str(user_id) + " nie istnieje w bazie."
            results = paginator.page(1)
        else:
            page = ((user_position_in_database - 1) / rows_per_page) + 1  # this gives page number where the user is


    else:
        page = request.GET.get('page')

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    return render(request, 'UserAccount/eventResultsTable.html', {'error_msg': error_msg, 'results_table': results,
                  'first_runner_position_on_page': (results.number - 1) * rows_per_page, 'searched_user_id': int_user_id})


def photosFromEventView(request):
    loggedin_response = __redirect_if_not_logged_in(request)
    if loggedin_response:
        return loggedin_response

    personal_url_photo = "http://www.fotomaraton.pl/event.php?Lang=PL&ToFind=%s&Event=PKR16" % str(request.user.id)
    return redirect(personal_url_photo)


def password_resetView(request):
    return render(request, 'UserAccount/password_reset.html')


def logout_action(request):
    logout(request)
    return redirect('home')


def __redirect_if_not_logged_in(request):
    if not request.user.is_authenticated:
        return redirect('userAccount:login')
    else:
        False

#################
#  admin views  #
#################

@staff_member_required
def runTableImport(request):
    msg = ''  # message to display on rendered page
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImportRunResults(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            msg = form.save
            if( msg == ""):
                msg = 'Sukces!'
            # display message about success
            return render(request, 'admin/ImportRunTableFromCSV.html', {'form': form, 'message': msg})

            # if a GET (or any other method) we'll create a blank form
        else:
            msg = 'Dane w formularzu nie są prawidłowe'
    else:
        form = ImportRunResults()

    return render(request, 'admin/ImportRunTableFromCSV.html', {'form': form, 'message': msg})

