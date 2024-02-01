from . import views
from django.urls import path, include


urlpatterns = [
    path('',  views.message_page),
]
