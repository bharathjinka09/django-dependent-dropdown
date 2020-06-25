from django.urls import path

from . import views

urlpatterns = [
    path('', views.personform_page, name='personform_page'),
]
