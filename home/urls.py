from django.urls import path
from .views import *
app_name = "home"
urlpatterns = [
    path('',MainList.as_view(),name="home" ),
]
