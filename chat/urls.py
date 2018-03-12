"""HTTP Routing for chat app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<room_name>/', views.RoomView.as_view(), name='room'),
]