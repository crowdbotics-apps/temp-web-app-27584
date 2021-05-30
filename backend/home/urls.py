from django.urls import path, include
from .views import home,appleSignIn,newResetPassword,password_reset_request,password_reset_done1,sendjson
from home.api.v1.viewsets import GoogleLogin, AppleLogin
from django.conf.urls import url



urlpatterns = [
    path("", home, name="home"),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
    url(r'^rest-auth/apple/$', AppleLogin.as_view(), name='apple-login'),
    path("appleSignIn", appleSignIn, name="appleSignIn"),
    path("newResetPassword", newResetPassword, name="newResetPassword"),
    path("password_reset", password_reset_request, name="password_reset"),  
    path("password_reset_complete", password_reset_done1, name="password_reset_done1"),
    path('sendjson',sendjson,name='sendjson')  


]
