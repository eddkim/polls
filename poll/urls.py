from django.urls import path
from poll import views

urlpatterns = [
    #127.0.0.1:8000/poll/
    path('',views.index)
]