from django.urls import path

from . import views

urlpatterns = [
    #path("logIn/", views.log_in, name="login"),
    path("signUp/", views.sign_up, name="sign_up"),
    path("successfullSignUp/", views.successfull_sign_up, name="successfull_sign_up"),
    path("successfullLogout/", views.successfull_logout, name="successfull_logout"),
]