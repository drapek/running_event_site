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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from UserAccount import views as userAccountViews
urlpatterns = [
    url(r'^$', views.IndexView, name='home'),
    url(r'^event_description', views.eventDescriptionView, name='eventDescription'),
    url(r'^sponsors', views.sponsorsView, name='sponsors'),
    url(r'^userAccount/', include('UserAccount.urls')),
    url(r'^admin/importRunTable', userAccountViews.runTableImport, name='adminImportRunTable'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin', admin.site.urls),
    url(r'', views.error404View, name='404exception'),  # remember that this url must be the last!
]
