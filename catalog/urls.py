from django.urls import path, include
from . import views


app_name = 'catalog'

urlpatterns = [
    path("home/", views.home_view, name='home'),
    path("contacts/", views.contacts_view, name='contacts')
]
