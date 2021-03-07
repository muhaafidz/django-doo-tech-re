from django.urls import path
from . import views

urlpatterns = [
    ### Training Module
    path('', views.home_page, name="home"),
]