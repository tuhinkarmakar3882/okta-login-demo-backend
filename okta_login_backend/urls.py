from django.urls import path

from okta_login_backend.views import login_callback

urlpatterns = [
    path('login/callback/', login_callback, name="login_callback"),
]
