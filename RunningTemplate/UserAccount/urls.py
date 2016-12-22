"""RunningTemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'userAccount'

urlpatterns = [
    # all these url are prefixed by userAccount/ eg. mysite.com/userAccount/login
    url(r'^$', views.IndexView, name='userHome'),
    url(r'^login', views.loginView, name='login'),
    url(r'^register', views.registerView, name='register'),
    url(r'^myProfile', views.profileDataView, name='userAccountData'),
    url(r'^resultsTable', views.resultsTableView, name='resultsTable'),
    url(r'^photosFromEvent', views.photosFromEventView, name='photosFromEvent'),
    url(r'^password_reset', views.password_resetView, name='password_reset'),
    url(r'', views.error404View, name='404exception'),  # remember that this url must be the last!
]
