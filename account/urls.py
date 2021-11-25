from django.urls import path
from . import views

urlpatterns = [
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
]