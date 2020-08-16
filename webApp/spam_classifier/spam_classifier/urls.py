"""spam_classifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spam_detector.urls'))
]


# handler404 = 'spam_detector.views.bad_request'

from functools import (
    partial,
)  # (using partial to pretend an exception has been raised)
from django.http import (
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
)

from spam_detector.views import handler404

urlpatterns += [
    # path("400/", partial(handler400, exception=HttpResponseBadRequest())),
    # path("403/", partial(handler403, exception=HttpResponseForbidden())),
    path("404/", partial(handler404, exception=HttpResponseNotFound())),
    # path("500/", handler500),  # "default_views.server_error" doesn't take an exception
]