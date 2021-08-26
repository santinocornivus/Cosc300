from re import template
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "accounts"
# This is a namespace used inside templates 

urlpatterns=[
    path('registration',UserRegisterView.as_view(),name="register"),
    path('login',CustomLoginView.as_view(),name="login"),
    path('',HomeView.as_view(),name="home"),

    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),
]

# PasswordResetView -- submit email form

# PasswordResetDoneView -- Email sent success message

# PasswordResetConfirmView -- Link to password Reset in email

# PasswordResetCompleteView -- Password successfully changed message