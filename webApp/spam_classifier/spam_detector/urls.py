from django.urls import path

from . import views

urlpatterns = [
    path('predict/', views.predict, name='result'),
    path('', views.formclass, name='classifier')
]