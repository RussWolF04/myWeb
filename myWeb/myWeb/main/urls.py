from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('training', views.training, name='training'),
    path('contacts', views.contacts, name='contacts'),
]
