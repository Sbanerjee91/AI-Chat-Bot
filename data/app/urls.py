from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_interface, name='chat_interface'),
    path('api/ask/', views.api_ask_ai, name='api_ask_ai'),
]