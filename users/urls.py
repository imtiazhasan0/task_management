from django.contrib import admin
from django.urls import path
from users.views import Sign_up, Sign_in, Sign_out

urlpatterns = [
    path('sign-up/', Sign_up, name='sign-up'),
    path('sign-in/', Sign_in, name='sign_in'),
    path('sign-out/', Sign_out, name='sign_out'),
]