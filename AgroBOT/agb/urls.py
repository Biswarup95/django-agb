from django.urls import path
from agb.views import home

urlpatterns = [
    path('',home, name="home"),
]