from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('messages_report/', views.messages_report, name="messages_report")
]
