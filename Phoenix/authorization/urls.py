from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'authorize'

urlpatterns = [
    path('', views.authorize_view, name="authorization"),
]
